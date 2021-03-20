import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
import helper_function.pccm_names as names
import pandas as pd
from reports.ffpe_db_new import NewBlock


class BlockInformation:

    def __init__(self, conn, cursor, file_number):
        self.file_number = file_number
        self.cursor = cursor
        self.conn = conn
        self.table_name = 'block_list'

    def get_block_id(self, col_filter_value):
        block_columns = ['file_number'] + names.block_list('all')
        block_list = sql.extract_multiple_value_select_column(self.conn, block_columns, table=self.table_name,
                                                              file_number=self.file_number, col_select='block_id',
                                                              col_filter='block_type',
                                                              col_filter_value=col_filter_value)
        block_id = ask.ask_list(str(col_filter_value) + ' block id information is to be entered for: ', block_list+
                                ['not available', 'Other'])
        block_list = ask.flatten_nested_list(block_list)
        if block_id not in set(block_list):
            number_of_blocks = 'not available'
        else:
            number_of_blocks = sql.get_value(col_name='number_of_blocks', table='block_list', pk_name='file_number',
                                             pk=self.file_number, cursor=self.cursor, error_statement="Enter number of "
                                                                                                      "blocks: ")
        return str(block_id), str(number_of_blocks)

    def get_block_pk (self, user_name, col_filter_value, col_select='block_id', col_filter='block_type'):
        #retrieves a list of block_ids that correspond to a particular col_filter (block_type, file_number etc)
        new_block = NewBlock(self.conn, self.cursor, user_name)
        block_columns = ['file_number'] + names.block_list('all')
        block_list = sql.extract_multiple_value_select_column(self.conn, block_columns, self.table_name,
                                                              self.file_number, col_select, col_filter,
                                                              col_filter_value)
        block_id = ask.ask_list(str(col_filter_value) + ' block id information is to be entered for: ', block_list +
                                ['not available', 'Other'])
        block_list = ask.flatten_nested_list(block_list)
        if block_id not in set(block_list):
            new_block.add_new_pk(self.file_number, block_type=col_filter_value)
            pk, number_of_blocks = self.get_block_information(block_id, block_data= ['pk', 'number_of_blocks'])
        else:
            sql_statement = ("SELECT pk FROM block_list WHERE (block_id = '" + block_id + "')")
            self.cursor.execute(sql_statement)
            pk_ = self.cursor.fetchall()
            pk = pk_[0][0]
            number_of_blocks = sql.get_value(col_name='number_of_blocks', table='block_list', pk_name='pk', pk=pk,
                                             cursor=self.cursor, error_statement="Enter number of blocks: ")
        return pk, str(block_id), number_of_blocks

    def get_block_information(self, block_id, block_data):
        if block_id == 'not available':
            search_col = 'file_number'
            search_val = self.file_number
        else:
            search_col = 'block_id'
            search_val = block_id
        sql_statement = ("SELECT DISTINCT " + ', '.join(block_data) + " FROM block_list WHERE " + search_col + "= '"
                         + search_val + "'")
        df = pd.read_sql(sql_statement, self.conn)
        block_details = []
        for col in block_data:
            block_detail = list(pd.unique(df[col].values))
            if len(block_detail) > 1:
                detail = ask.ask_list('Please choose the correct ' + col + ': ', block_detail + ['not available'])
                block_detail = detail
            block_details.append(block_detail)
        return ask.flatten_nested_list(block_details)

    def margin_info(self):
        specimen_resection_size = input('Size of specimen (resection size): ')
        margins = ask.check_number_input('Please input number of resection margin sizes to be entered: ',
                                         'Please only input number of margins not type')
        margin_size_df = pd.DataFrame(columns=['margin', 'size'])
        if margins != '0':
            for margin in range(0, int(margins)):
                margin_name = input('Name of margin: ')
                margin_distance = input('Margin Size: ')
                margin_size_df.loc[margin] = [margin_name, margin_distance]
            margin_size_df['margin_size_name'] = margin_size_df['margin'].str.cat(margin_size_df['size'], sep =": ")
            margin_size = '|'.join(list(margin_size_df['margin_size_name']))
        else:
            margin_size = 'no_margins_described'
        cut_margins = ask.check_number_input('Please input number of cut (shave) margin sizes to be entered: ',
                                         'Please only input number of margins not type')
        cut_margin_size_df = pd.DataFrame(columns=['cut_margin', 'size'])
        if cut_margins != '0':
            for cut_margin in range(0, int(cut_margins)):
                cut_margin_name = input('Name of cut_margin: ')
                cut_margin_distance = input('Cut Margin dimensions: ')
                cut_margin_size_df.loc[cut_margin] = [cut_margin_name, cut_margin_distance]
            cut_margin_size_df['cut_margin_size_name'] = cut_margin_size_df['cut_margin'].str.cat(
                cut_margin_size_df['size'], sep=": ")
            cut_margin_size = '|'.join(list(cut_margin_size_df['cut_margin_size_name']))
        else:
            cut_margin_size = 'cut_margins_not_present'
        margin_report = input('Please input description of margins (involved/free/unremarkable etc as given in the report: ')
        return specimen_resection_size,margin_size,cut_margin_size, margin_report



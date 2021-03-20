import pandas as pd
import os
import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
import helper_function.pccm_names as names
from additional_tables.block_description import block_location_format
import uuid


class FFPECSVData:
    def __init__(self, conn, cursor, folder_name, file_name):
        self.table = 'block_list'
        self.cursor = cursor
        self.folder_name = folder_name
        self.file_name = file_name
        self.conn = conn
        self.columns = ", ".join(names.name_ffpe_csv())

    def read_file(self):
        file_path = os.path.join(self.folder_name, self.file_name)
        new_data = pd.read_csv(file_path)
        new_data = new_data.dropna(axis=0, how='any', thresh=None, subset=['patient_name'], inplace=False)
        return new_data

    def write_file(self, new_data):
        for i in range(0, new_data.shape[0]):
            data_add = list(new_data.loc[i, :]) + [self.file_name]
            sql.insert(self.conn, self.cursor, self.table, self.columns, data_add)


class NewBlock:

    def __init__(self, conn, cursor, user_name):
        self.user_name = user_name
        self.table_name = 'block_list'
        self.conn = conn
        self.cursor = cursor
        self.columns = names.block_list('all')
        self.block_data = pd.DataFrame(columns=['pk'] + self.columns)

    def update_patient(self, file_number, block_id):
        block_df = self.block_data
        check = False
        while not check:
            print('update_patient')
            pk = uuid.uuid4().hex
            patient_name = self.get_value_and_check_value(col_name='patient_name', file_number=file_number,
                                                          input_statement='Please enter patient name: ',
                                                          integer=False)
            block_sr_number = self.get_value_and_check_value(col_name='block_sr_number', file_number=file_number,
                                                             input_statement='Please enter block serial number: ',
                                                             integer=True)
            if block_sr_number != 'block_not_available':
                block_location_check = sql.get_value_no_error('block_location', self.table_name, file_number,
                                                              'file_number', self.cursor)
                block_location = block_location_check
                print('block_location: '+ str(block_location))
                block_location_check = ask.ask_y_n('Is this correct?')
                while not block_location_check:
                    block_location = block_location_format()
                    block_location_check = self.check_block_value_not_exist(value_name='block_location',
                                                                     value=block_location, table=self.table_name)
                blocks_received_at_pccm = sql.check_db_value(col_name='blocks_received_at_pccm', table=self.table_name,
                                                             file_number=file_number, cursor=self.cursor,
                                                             error_statement='Please enter date blocks recieved at PCCM'
                                                                             ' (dd.mm.yyyy): ')
                block_type = ask.ask_list('Block type', ['biopsy', 'surgery'])
                if block_id == 'block_id':
                    block_id = self.check_block_value_in_db(input_statement='Please enter block id: ',
                                                            value_name='block_id', integer=False)

                number_of_blocks = ask.check_number_input('Please enter number of blocks recieved at PCCM: ',
                                                          'Number of blocks has to be a whole number or NA')
                block_series = input("Series of blocks recieved (Please separate series by ';'): ")
                current_block_location = ask.ask_list('Current location of block', names.block_list('location'))
                consent_discussed, consent = self.get_consent(file_number)
            else:
                block_type = ask.ask_list('Block type', ['biopsy', 'surgery'])
                if block_id == 'block_id':
                    block_id = self.check_block_value_in_db(input_statement='Please enter block id: ',
                                                            value_name='block_id', integer=False)
                block_location, blocks_received_at_pccm, number_of_blocks, block_series, current_block_location, \
                consent_discussed, consent = (block_sr_number, )*7
            data_list = [pk, file_number, patient_name, block_sr_number, block_location, block_type, block_id,
                         current_block_location, blocks_received_at_pccm, number_of_blocks, block_series, consent_discussed,
                         consent, self.user_name, sql.last_update()]
            block_df.loc[pk] = data_list
            check, block_df = sql.review_df_row(block_df)
        print("error check in update_patient")
        sql.print_df(block_df)
        return block_df

    def add_update_patient(self):
        block_df = self.block_data
        file_number = 'test'
        check_file = False
        while not check_file:
            print('add_update_patient')
            file_number = input("Enter File Number: ")
            print("File Number: " + file_number)
            check_file = ask.ask_y_n("Is this file number correct")
        check = False
        while not check:
            if sql.check_file_number_exist(self.cursor, file_number, self.table_name):
                print('add_update_patient_not_checck')
                pk = uuid.uuid4().hex
                patient_name = self.get_value_and_check_value(col_name='patient_name', file_number=file_number,
                                                              input_statement='Please enter patient name: ',
                                                              integer=False)
                block_sr_number = self.get_value_and_check_value(col_name='block_sr_number', file_number=file_number,
                                                                 input_statement='Please enter block serial number: ',
                                                                                                           integer=True)
                # block_location = 'block_location'
                block_location_check = sql.get_value_no_error(col_name='block_location', table=self.table_name,
                                                              pk=file_number, pk_name='file_number', cursor=self.cursor)
                if not block_location_check:
                    print('Block location already exists for another file_number')
                    while not block_location_check:
                        block_location = block_location_format()
                        block_location_check = sql.check_value_not_exist(self.cursor, value_name='block_location',
                                                                         value=block_location, table=self.table_name)
                else:
                    block_location = block_location_check
                blocks_received_at_pccm = sql.get_value_no_error(col_name='blocks_received_at_pccm',
                                                                 table=self.table_name, pk=file_number,
                                                                 pk_name='file_number', cursor=self.cursor)
                if not blocks_received_at_pccm:
                    blocks_received_at_pccm = ask.check_date_or_today('Please enter date blocks recieved at PCCM (or '
                                                                      'today): ')
                consent_discussed, consent = self.get_consent(file_number)
            else:
                pk = uuid.uuid4().hex
                patient_name = input('Please enter patient name: ')
                block_sr_number = self.check_block_value_in_db(input_statement='Please enter block serial number: ',
                                                               value_name='block_sr_number', integer=True)

                block_pccm = ask.ask_y_n('Have these blocks been recieved at PCCM?')
                block_location, blocks_received_at_pccm = ['NA', ] * 2
                if block_pccm:
                    block_location_check = False
                    while not block_location_check:
                        block_location = block_location_format()
                        block_location_check = sql.check_value_not_exist(self.cursor, value_name='block_location',
                                                                         value=block_location, table=self.table_name)
                    blocks_received_at_pccm = ask.check_date_or_today('Please enter date blocks recieved at PCCM (or '
                                                                      'today): ')
                consent_discussed, consent = self.get_consent(file_number)
            block_type = ask.ask_list('Block type', ['biopsy', 'surgery'])
            block_id = self.check_block_value_in_db(input_statement='Please enter block id: ', value_name='block_id',
                                                    integer=False)
            number_of_blocks = ask.check_number_input('Please enter number of blocks recieved at PCCM: ',
                                                      'Number of blocks has to be a whole number or NA')
            block_series = input("Series of blocks recieved (Please separate series by ';'): ")
            current_block_location = ask.ask_list('Current location of block', names.block_list('location'))
            data_list = [pk, file_number, patient_name, block_sr_number, block_location, block_type, block_id,
                         current_block_location, blocks_received_at_pccm, number_of_blocks, block_series, str(consent_discussed),
                         consent, self.user_name, sql.last_update()]
            # error check
            print("error check in loop 1")
            sql.print_df(block_df)
            block_df.loc[pk] = data_list
            print("error check in loop 2")
            sql.print_df(block_df)
            check, block_df = sql.review_df_row(block_df)
        # error check
        print("error check out of loop_to_db")
        sql.print_df(block_df)
        return block_df

    def add_data(self):
        add_block = True
        while add_block:
            data = self.add_update_patient()
            data.to_sql("block_list", self.conn, index=False, if_exists="append")
            add_block = ask.ask_y_n('Add another block?')

    def add_one(self, file_number, block_id='block_id'):
        data = self.update_patient(file_number, block_id)
        data.to_sql("block_list", self.conn, index=False, if_exists="append")

    def add_new_pk(self, file_number, block_id):
        data = self.update_patient(file_number, block_id)
        data.to_sql("block_list", self.conn, index=False, if_exists="append")

    def edit_data(self, file_number):
        print('view_multiple')
        enter = sql.view_multiple(self.conn, self.table_name, self.columns, file_number)
        if enter == "Add data":
            self.add_one(file_number)
        elif enter == "Edit data":
            col_pk = ['pk'] + self.columns
            sql_statement = ('SELECT ' + ", ".join(col_pk) + " FROM '" + self.table_name +
                             "' WHERE file_number = '" + file_number + "'")
            df = pd.read_sql(sql_statement, self.conn)
            sql.print_df(df)
            # check_delete = False
            # while not check_delete:
            check_delete, df = sql.edit_table(df, pk_col='block_id', df_col=self.columns[:-2],
                                                  update_by=self.user_name)
            if check_delete:
                sql.delete_rows(self.cursor, self.table_name, "file_number", file_number)
                data = self.add_update_patient()
                data.to_sql(self.table_name, self.conn, index=False, if_exists="append")
            else:
                sql.delete_rows(self.cursor, self.table_name, "file_number", file_number)
                df.to_sql(self.table_name, self.conn, index=False, if_exists="append")
        else:
            print('\n No edits will be made to this table\n')

    def check_block_value_in_db(self, input_statement, value_name, integer):
        check_value = False
        value = value_name
        while not check_value:
            if integer and value != 'block_not_available':
                value = ask.check_number_input(input_statement, error=value_name + 'has to be a number')
            else:
                value = input(input_statement)
            if value != 'block_not_available':
                check_value = sql.check_value_not_exist(self.cursor, value_name, value, self.table_name)
        return value

    def get_value_and_check_value(self, col_name, file_number, input_statement, integer):
        pk = file_number
        check = False
        value = col_name
        check_value = True
        while not check:
            value = sql.get_value_no_error(col_name, self.table_name, pk, 'file_number', self.cursor)
            if not value or not check_value:
                value = self.check_block_value_in_db(input_statement, value_name=col_name, integer=integer)
            print(col_name.capitalize(), ': ', value)
            check_value = ask.ask_y_n('Is this correct?')
            if check_value:
                check = True
        return value

    def get_consent(self, file_number):
        consent_discussed = sql.get_value_no_error('consent_discussed', self.table_name, file_number,
                                                   'file_number', self.cursor)
        consent = sql.get_value_no_error('consent', self.table_name, file_number, 'file_number', self.cursor)
        if not consent_discussed:
            consent_discussed = ask.ask_y_n('Has the consent form been discussed with the patient/family? ')
        if not consent and consent_discussed:
            consent = ask.ask_y_n('Did patient give consent?', yes_ans='consent_given',
                                  no_ans='consent_not_given')
        elif not consent and not consent_discussed:
            consent = 'consent_TBD'
        print('consent_discussed: ' + str(consent_discussed), 'consent: ' + consent)
        check = ask.ask_y_n('Is this correct?')
        if not check:
            check_review = False
            data = [str(consent_discussed), consent]
            col_list = ['consent_discussed', 'consent']
            while not check_review:
                consent_discussed = ask.ask_y_n('Has the consent form been discussed with the patient/family? ')
                consent = ask.ask_y_n('Did patient give consent?', yes_ans='consent_given', no_ans='consent_not_given')
                data = [str(consent_discussed), consent]
                check_review = sql.review_input(file_number, col_list, data)
            sql.update_multiple_key(conn=self.conn, cursor=self.cursor, table=self.table_name, columns=col_list,
                                    key_name='file_number', key_value=file_number, data=data)
        return str(consent_discussed), consent

    def check_block_value_not_exist(self, value_name, value, table):
        if value == 'no_block_available':
            return True
        else:
            sql_statement = "SELECT rowid FROM " + table + " WHERE " + value_name + " = ?"
            self.cursor.execute(sql_statement, (value,))
            data = self.cursor.fetchall()
            if len(data) == 0:
                return True
            else:
                print('This ' + value_name + ' already exists. Please check source and enter another value')
                return False
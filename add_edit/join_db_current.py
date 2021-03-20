import sqlite3
import sql.add_update_sql as sql
import pandas as pd
from helper_function.pccm_names import db_tables
import helper_function.table_dicts as table_dicts
from sql.add_update_sql import table_check
import os


class JoinDB:
    def __init__(self, db_collated, db_old):
        self.conn_new = sqlite3.connect(db_collated)
        self.conn_old = sqlite3.connect(db_old)
        self.cursor_new = self.conn_new.cursor()
        self.cursor_old = self.conn_old.cursor()


    def get_table_list(self) -> list:
        tables_to_print = []
        for table in db_tables():
            check = table_check(self.cursor_old, table)
            if check:
                tables_to_print.append(table)
        return tables_to_print


    def add_old_data_to_new_table(self, table, file_list):
        modules = table_dicts.table_module_dict(table)
        columns = []
        if not modules:
            modules = 'no_modules'
            columns = table_dicts.db_dict(table, modules)
        else:
            for module in modules:
                print(module)
                cols = table_dicts.db_dict(table, module)
                columns = columns + cols
        for file in file_list:
            for col in range(0, len(columns)):
                sql_list = ['SELECT ', columns[col], ' FROM ', table,
                            " WHERE file_number = '", file, "'"]
                sql_statement = ''.join(sql_list)
                data_old = self.cursor_old.execute(sql_statement)
                dat = data_old.fetchone()
                if not (dat is None):
                    dat = dat[0]
                print(dat)
                # for dat in data_old:
                sql.update_single(self.conn_new, self.cursor_new, table,
                                  column=columns[col], file_number=file,
                                  var=dat)
        print(str(len(file_list)) + 'files added to ' + table)


    def add_supp_table(self, table):
        sql_statement = 'SELECT * FROM ' + table
        df_old = pd.read_sql(sql_statement, self.conn_old)
        df_old.to_sql(table, self.conn_new, index=False,
                      if_exists='append')

    def add_file_number(self, table):
        sql_statement = 'SELECT file_number from ' + table
        file_number = self.cursor_old.execute(sql_statement)
        file_number = file_number.fetchall()
        file_list = []
        for file in file_number:
            file_var = file[0]
            sql.add_pk_fk_to_table(self.conn_new, self.cursor_new,
                                   col_name='file_number', pk=file_var,
                                   table=table)
            file_list.append(file_var)
        return file_list

    def add_data_to_supp_tables(self, file_list, table):
        sql_statement = 'SELECT * FROM ' + table
        df_old = pd.read_sql(sql_statement, self.conn_old)
        cols = df_old.columns
        df_new = pd.DataFrame(columns = cols)
        # df_new = pd.DataFrame(columns=['pk'] + cols)
        for i in range(0, len(df_old)):
            pk = sql.create_pk()
            dat = [pk], list(df_old.loc[i])
            df_new.loc[i] = dat
        df_new.to_sql(table, self.conn_new, index=False, if_exists='append')

    def add_select_data_to_main_tables(self, file_list, table):
        for file in file_list:
            sql.add_pk_fk_to_table(self.conn_new, self.cursor_new,
                                   col_name='file_number', pk=file,
                                   table=table)
        self.add_old_data_to_new_table(table, file_list)


    def add_select_data_to_supp_tables(self, file_list, table):
        sql_statement = 'SELECT * FROM ' + table
        df_old = pd.read_sql(sql_statement, self.conn_old)
        cols = df_old.columns
        # pk_add = False
        # if 'pk' not in cols:
            # pk_add = True
            # cols = ['pk'] + cols
        # df_new = pd.DataFrame(columns = cols)
        # df_new = pd.DataFrame(columns=['pk'] + cols)
        for file in file_list:
            query_stat = 'file_number == "' + file + '"'
            df = df_old.query(query_stat)
            # if pk_add:
                # df['pk'] = [sql.create_pk(),] * df.shape[0]
                # df = df[cols]
            df.to_sql(table, self.conn_new, index=False, if_exists='append')


def add_select_data_to_new_db(folder_path, file_name, data_sheet, db_new):
    file_path = os.path.join(folder_path, file_name)
    file_df = pd.read_excel(file_path, sheet_name=data_sheet)
    dbs = set(list(file_df['db_name']))
    for db in list(dbs):
        db_n = db + '.db'
        db_old = os.path.join(folder_path, db_n)
        joindb = JoinDB(db_collated=db_new, db_old=db_old)
        tabs = joindb.get_table_list()
        query_stat = 'db_name == "' + db + '"'
        db_df = file_df.query(query_stat)
        print(db_df.head())
        file_list = list(db_df['file_number'])
        for tab in tabs:
            print(tab)
            table_type = table_dicts.table_type_dict(tab)
            print(table_type)
            if table_type == ['pk_table']:
                joindb.add_select_data_to_supp_tables(file_list, tab)
                print(len(file_list), 'files added from ', db, ' to table ', tab)
            elif table_type == ['file_number_table']:
                joindb.add_select_data_to_main_tables(file_list, tab)
                print(len(file_list), 'files added from ', db, ' to table ', tab)


if __name__ == '__main__':
    folder_db = "D://WorkDocs//Documents//TilsProspectiveData"
    folder_db_new = os.path.join(folder_db, 'collated_data')
    db_name = 'PCCM_BreastCancerDB_2021_02_05.db'
    # create_table = MakeTable(folder_db_new, db_name)
    # create_table.makedb()
    db_new = os.path.join(folder_db_new, db_name)
    add_select_data_to_new_db(folder_path=folder_db,
                              file_name='2021_01_27_TILs_prospective_curation_sheet_da.xlsx',
                              data_sheet='ProspectiveCurationSheet',
                              db_new=db_new)


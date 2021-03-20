import sqlite3
import sql.add_update_sql as sql
import pandas as pd
from add_edit.db_names import DB_list, TablesList
from helper_function.pccm_names import db_tables
import helper_function.table_dicts as table_dicts
import os
from datetime import datetime as dt
from pccm_bcdb_create import MakeTable


class JoinDB():
    def __init__(self, db_new, db_old):
        self.conn_new = sqlite3.connect(db_new)
        self.conn_old = sqlite3.connect(db_old)
        self.cursor_new = self.conn_new.cursor()
        self.cursor_old = self.conn_old.cursor()

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
                sql_statement = 'SELECT ' + columns[col] + ' FROM '
                + table + " WHERE file_number = '" + file
                + "'"
                data_old = self.cursor_old.execute(sql_statement)
                data = data_old.fetchall()[0][0]
                sql.update_single(self.conn_new, self.cursor_new, table,
                                  column=columns[col], file_number=file,
                                  var=data)
        print(str(len(file_list)) + 'files added to ' + table)

    def get_table_list(self):
        sql_stat = 'SELECT name FROM sqlite_master WHERE TYPE = "TABLE"'
        tabs = self.cursor_old.execute(sql_stat)
        tabs = tabs.fetchall()
        tabs_list = [tab[0] for tab in tabs]
        return (tabs_list)

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
        df_new = pd.DataFrame(columns=['pk'] + cols)
        for i in range(0, len(df_old)):
            pk = sql.create_pk()
            dat = [pk], list(df_old.loc[i])
            df_new.loc[i] = dat
        df_new.to_sql(table, self.conn_new, index=False, if_exists='append')

    def add_data_to_main_tables(self, file_list, table):
        for file in file_list:
            sql.add_pk_fk_to_table(self.conn_new, self.cursor_new,
                                   col_name='file_number', pk=file,
                                   table=table)
        add_old_data_to_new_table(self, table, file_list)


def add_select_data_to_new_db(folder_path, file_name, data_sheet, db_new):
    file_path = os.path.join(folder_path, file_name)
    file_df = pd.read_excel(file_path, sheet_name=data_sheet)
    dbs = set(list(file_df['db_name']))
    for db in dbs:
        db_name = db + '.db'
        db_old = os.path.join(folder_path, db_name)
        joindb = JoinDB(db_new=db_new, db_old=db_old)
        query_stat = 'db_name == "' + db + '"'
        file_list = list(file_df.query(query_stat)['file_number'])
        tabs = self.get_table_list()
        for tab in tabs:
            table_type = table_dicts.table_type_dict(tab)
            if table_type == 'pk_id':
                joindb.add_data_to_supp_tables(file_list, tab)
            elif table_type == 'file_number_id':
                joindb.add_data_to_main_tables(file_list, tab)
            else:
                return (tab, 'not updated')

def add_select_data_to_new_db_table(folder_path, file_name, data_sheet, db_new):
    file_path = os.path.join(folder_path, file_name)
    file_df = pd.read_excel(file_path, sheet_name=data_sheet)
    file_df = file_df.query('copies == 1')
    dbs = set(list(file_df['db_name']))
    for db in dbs:
        db_name = db + '.db'
        db_old = os.path.join(folder_path, db_name)
        joindb = JoinDB(db_new=db_new, db_old=db_old)
        query_stat = 'db_name == "' + db + '"'
        file_list = list(file_df.query(query_stat)['file_number'])
        table_type = table_dicts.table_type_dict(table)
        if table_type == 'pk_id':
            joindb.add_data_to_supp_tables(file_list, table)
        elif table_type == 'file_number_id':
            joindb.add_data_to_main_tables(file_list, table)
        else:
            return (table, 'not updated')


if __name__ == '__main__':
    folder = 'Z://Clinical_Database//dB_Backup//Curated Database'
    folder_db = os.path.join(folder, 'all_db')
    db_name = 'All_PCCM_DB_' + dt.now().strftime("%Y_%m_%d") + '.db'
    create_table = MakeTable(folder, db_name)
    create_table.makedb()
    db_new = os.path.join(folder_db, db_name)
    for table in db_tables():
        add_data = add_select_data_to_new_db_table(folder_path='Z://Clinical_Database//dB_Backup//Curated Database',
                                             file_name='2021_02_22_2021_curation_db_all.xlsx',
                                             data_sheet=table,
                                             db_new=db_new)

# file_list = []
# for table in tables:
#     joinDb = JoinDB(db_new, db_old, table)
#     file_list = add_file_number()
#     file_all.append(file_list)
#     file_list = set.difference_update(file_all)

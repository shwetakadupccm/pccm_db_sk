from pccm_bcdb_create import CreateTable
import sql.add_update_sql as sql
import sqlite3
import pandas as pd
import os
import helper_function.pccm_names as names
import helper_function.table_dicts as td
from add_edit.join_db_current import JoinDB
import datetime


class UpdateColumns:

    def __init__(self, folder_path, dB, table):
        self.dB = dB
        self.dB_path = os.path.join(folder_path, dB)
        self.conn = sqlite3.connect(self.dB_path)
        self.cursor = self.conn.cursor()
        self.table = table

    def get_table_list(self):
        sql_stat = 'SELECT name FROM sqlite_master WHERE TYPE = "TABLE"'
        tabs = self.cursor.execute(sql_stat)
        tabs = tabs.fetchall()
        tabs_list = [tab[0] for tab in tabs]
        return (tabs_list)

    def get_input_data(self):
        sql_stat = 'SELECT * FROM ' + self.table
        try:
            df = pd.read_sql_query(sql_stat, self.conn)
        except pd.io.sql.DatabaseError:
            df = None
            old_col = None
        old_col = df.columns[1:]
        return (df, old_col)

    def create_table(self):
        create = CreateTable(self.cursor)
        modules = td.table_module_dict(self.table)
        col_names = td.db_dict(self.table, modules)
        create.create_table(self.table, file_number='file_number',
                            col_names=col_names)

    def add_data(self, old_col, df):
        if df is not None:
            dat_rows = df.shape[0]
            print(df.shape)
            # joinDb = JoinDB(db_new=self.dB_path, db_old=self.dB_path,
            #                 table=self.table)
            # file_list = join_db.add_file_number()
            for row in range(dat_rows):
                dat = list(df.loc[row])
                file_number = dat[0]
                print(file_number)
                dat_add = dat[1:]
                print(dat_add)
                sql.add_pk_fk_to_table(self.conn, self.cursor, self.table,
                                       col_name='file_number', pk=file_number)
                sql.update_multiple(self.conn, self.cursor, self.table,
                                    columns=old_col, file_number=file_number,
                                    data=dat_add)

    def drop_old_table(self):
        sql_stat = 'DROP TABLE ' + self.table
        try:
            self.cursor.execute(sql_stat)
        except pd.io.sql.DatabaseError:
            return


class DataList:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_tables_db(self, db_name):
        db_path = os.path.join(self.folder_path, db_name)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_stat = "SELECT name FROM sqlite_master WHERE TYPE = 'table'"
        tabs = cursor.execute(sql_stat)
        tabs = tabs.fetchall()
        return(tabs, conn)

    def output_last_update(self, df, w):
        tabs = list(df['table'])
        tabs = set(tabs)
        for table in tabs:
            query_stat = "table == '" + table + "'"
            df_tab = df.query(query_stat)
            df_tab.to_excel(w, sheet_name=table, index=False, header=True)
        w.save()

    def get_last_update_data(self):
        df_all = pd.DataFrame()
        for db in os.listdir(self.folder_path):
            if db.endswith('.db'):
                tabs, conn = self.get_tables_db(db)
                df = self.get_file_last_update(conn, tabs, db)
                df_all = pd.concat([df_all, df], ignore_index=True)
        output_date = datetime.datetime.today()
        output_file = output_date.strftime('%Y_%m_%d') + '_data_list.xlsx'
        w = pd.ExcelWriter(os.path.join(self.folder_path, output_file))
        df_all.to_excel(w, sheet_name='all')
        self.output_last_update(df_all, w)    
        print(output_file, 'created')

    @staticmethod
    def get_file_last_update(conn, tabs, db_name):
        df_all = pd.DataFrame(columns=['table', 'file_number', 'last_update',
                                       'update_by', 'db_name'])
        for tab in tabs:
            table = tab[0]
            print(table)
            if table in names.db_tables():
                sql_stat = 'SELECT file_number, last_update, update_by FROM ' + table
                print(sql_stat)
                df = pd.read_sql_query(sql_stat, conn)
                print(df.shape)
                df['table'] = [table] * df.shape[0]
                df['db_name'] = [db_name] * df.shape[0]
                cols = ['table', 'file_number', 'update_by', 'last_update',
                        'db_name']
                df = df[cols]
                print(df)
                df_all = pd.concat([df_all, df], ignore_index=True, axis=0)
        return(df_all)


def get_data_list():
    folder_path = 'Z://Clinical_Database//dB_Backup//Curated Database//all_db'
    data_list = DataList(folder_path)
    data_list.get_last_update_data()

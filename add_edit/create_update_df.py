import sqlite3
import os
import pandas as pd
from sql.add_update_sql import table_check
import datetime
import helper_function.pccm_names as names

def weekly_data(conn, cursor, table):

    file_number_table = pd.DataFrame(columns=('File_number', table))
    if table_check(cursor, table) == 1:
        sql = ("SELECT File_number, update_by, last_update FROM '" + table + 
        "'")
        df_all = pd.read_sql(sql, conn)
        df_all[table]= True
        df_dup = df_all.drop_duplicates(keep= 'first')
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(0, 8)]
        dates_toget = []
        for index in date_list:
            dates = index.strftime("%Y-%b-%d")
            dates_toget.append(dates)
        df_update = pd.DataFrame(columns=['File_number', 'update_by', 'last_update'])
        index = 0
        for i in dates_toget:
            sql = ("SELECT File_number, update_by, last_update FROM '" + table + "' WHERE last_update LIKE '"+i+"%'")
            df_index = pd.read_sql(sql, conn)
            if len(df_index) > 0:
                for j in range(0, len(df_index)):
                    df_update.loc[index]= list(df_index.loc[j])
                    index = index +1
        updates = [len(df_all), len(df_update)]
        file_number_table = df_dup.loc[:,['File_number', table]]
    else:
        updates = "does not exist in the database so far"
    return updates, file_number_table

# add capability to send list of files added, with yes/no in each table, should be for all files added.
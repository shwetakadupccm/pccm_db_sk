import pandas as pd
import sqlite3
import os
import helper_function.pccm_names as pccm_names
import sql.add_update_sql as sql
from datetime import datetime

#create new table
path_all = 'D:/repos/pccm_db/main/DB/DB_with_real_data/PCCM_BreastCancerDB_all_data.db'
os.path.isfile(path_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()
table = "Biopsy_Report_Data"
file_number = "File_number"
if sql.table_check(cursor_all, table) == 0:
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    module_names = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
    for index in module_names:
        col_name = pccm_names.names_biopsy(index)
        sql.add_columns(cursor_all, table, col_name)

#read from excel with same col names and distribution as in table

file_to_read = "D:/Documents/IISER/Prashanti_docs/Breast_Cancer_FFPE_blocks_database_Biopsy_dk08062018.xlsx"
data = pd.read_excel(file_to_read,header=1, dtype = 'object' ,usecols= 'A:AB')
update_by = "dk from ruhi/shaheen data"
module_names = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + pccm_names.names_biopsy(index)
columns = ", ".join(col_list)
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    data_list.append(update_by)
    data_list.append(sql.last_update())
    sql.insert(conn_all, cursor_all, table, columns, data_list)

#for surgery_report
table = "Surgery_Block_Report_Data"
if sql.table_check(cursor_all, table) == 0:
    cursor_all.execute('CREATE TABLE {tn}({nf})' .format(tn=table, nf=file_number))
    module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
    for index in module_names:
        col_name = pccm_names.names_surgery(index)
        sql.add_columns(cursor_all, table, col_name)

#add data

file_to_read = "D:/Documents/IISER/Prashanti_docs/Breast_Cancer_FFPE_blocks_database_Surgery_dk08062018.xlsx"
data = pd.read_excel(file_to_read,header=1, dtype = 'object' ,usecols= 'A:BB')
update_by = "dk from ruhi/shaheen data"
module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + pccm_names.names_surgery(index)
columns = ", ".join(col_list)
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    data_list.append(update_by)
    data_list.append(sql.last_update())
    sql.insert(conn_all, cursor_all, table, columns, data_list)


# get col_names from older pccm_names files:
# 2018-09-28
import helper_function.pccm_names as pccm_names
import sql.add_update_sql as sql
#read from excel with same col names and distribution as in table
table = 'follow_up_Data'
file_to_read = "D:/OneDrive/iiser_data/Prashanti_docs/Database_files/2018_10_09/Rituja_data/" \
               "PCCM_BreastCancerDB_Rituja_2018-10-11_2018-10-11.xlsx"
data = pd.read_excel(file_to_read, header=0, dtype = 'object' ,usecols= 'A:L', sheet_name='Follow_up_Data')
col_list = ["File_number"]
col_list = col_list + pccm_names.name_follow_up()
columns = ", ".join(col_list)
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    sql.insert(conn_all, cursor_all, table, columns, tuple(data_list))

#add mock block list table
import pandas as pd
import sql.add_update_sql as sql

table = 'block_list'
file_to_read = "D:/OneDrive/iiser_data/Prashanti_docs/Database_files/Block_data_biopsy_surgery/" \
               "2019_03_06_mock_block_list.xlsx"
data = pd.read_excel(file_to_read, header=0, dtype = 'object' ,usecols= 'A:K', sheet_name='Sheet2')
data[['last_update']] = sql.last_update()
col_list = ["file_number"]
col_list = col_list + pccm_names.block_list()
columns = ", ".join(col_list)
#convert dates to objects
data[['blocks_received_at_pccm']] = sql.last_update()
data[['update_by']] = 'dk'
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    sql.insert(conn, cursor, table, columns, tuple(data_list))


to_do = {'55/17', '257/16', '270/14', '222/12', '443/15', '283/12', '651/15', '593/15', '574/15', '571/15', '55/10',
         '264/12', '518/16','201/17','346/17','555/16','334/17','351/17','297/17','367/17','335/17',
         '607/16','434/16','517/16','427/15','312/16','506/16','880/16','72/16','297/16', '268/15', '630/16', '3/15',
         '460/16', '362/13', '535/14', '279/13', '46/13', '174/12', '329/16', '80/14', '259/17', '312/17', '201/13',
         '136/14', '346/16'}

to_delete = {'test','Test',' 375/14'}
import sqlite3
import os
import pandas as pd
folders = "d:/repos/pccm_db/main/DB/from_linux/"
file = 'PCCM_BreastCancerDB_all_data_clean_28052018.db'
path_all = os.path.join(folders, file)
os.path.isfile(path_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()
table = ["Patient_Information_History", "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions"]
#table = ['Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
x = []
for index in table:
    sql = "SELECT File_number FROM '"+index+"'"
    df = pd.read_sql(sql, conn_all)
    df_list= list(df['File_number'])
    df_del = ['test 434/16','test 335/17','test 351/17','test 346/16','test 312/17','test 259/17']
 #   for i in df_list:
 #       if i not in to_do:
 #           df_del.append(i)
    if df_del != []:
        x = x + df_del
        for j in df_del:
            sql = "DELETE FROM '"+index+"' WHERE File_number = '"+j+"'"
            cursor_all.execute(sql)
conn_all.commit()


# delete duplicate rows
table = 'x'
for index in table:
sql = ('DELETE FROM '+table+' WHERE rowid NOT IN (SELECT MIN(rowid)FROM '+table+' GROUP BY File_number)')
cursor_all.execute(sql)

table = ["Neo_Adjuvant_Therapy", 'Adjuvant_ChemoTherapy']
df_del = ['test','test1','test 434/16','test 335/17','test 351/17','test 346/16','test 312/17','test 259/17']
for index in table:
    for j in df_del:
        sql = "DELETE FROM '" + index + "' WHERE File_number = '" + j + "'"
        cursor.execute(sql)


from helper_function.pccm_names import db_tables
from sql.add_update_sql import table_check
from helper_function.ask_y_n_statement import ask_option, ask_y_n
from add_edit.output_excel import print_table
import os
import sqlite3
import pandas as pd

file_all = 'PCCM_BreastCancerDB_all_data_cleaned_dk.db'
folders = 'D:/Documents/IISER/Prashanti_docs/QSync/RESEARCH/Clinical_Database/PCCM Clinical Data/2018/08/07'
path = os.path.join(folders, file_all)
conn = sqlite3.connect(path)
cursor = conn.cursor()
tables_to_print = []
for table in db_tables():
    check = table_check(cursor, table)
    if check:
        tables_to_print.append(table)

table = tables_to_print
df_del = ['test','test1','test 434/16','test 335/17','test 351/17','test 346/16','test 312/17','test 259/17']
for index in table:
    for j in df_del:
        sql = "DELETE FROM '" + index + "' WHERE File_number = '" + j + "'"
        cursor.execute(sql)

print('This database contains the following tables:')
i = 1
for table in tables_to_print:
    print(str(i) + ". " + table)
    i = i+1
ex_file = 'Output_all_data_dk_clean_2018-08-09.xlsx'
ex_path = os.path.join(folders, ex_file)

writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
print('This database contains the following tables:')
i = 1
for table in tables_to_print:
    print(str(i) + ". " + table)
    i = i+1
to_print = ask_option("Do you want to print all tables or only select tables?",
                      ["All tables", "Select tables"])
if to_print == "All tables":
    for tables in tables_to_print:
        print_table(conn, writer, tables)
elif to_print == "Select tables":
    for table in tables_to_print:
        to_print = ask_y_n("Do you want to print " + table)
        if to_print:
            print_table(conn, writer, table)
writer.save()

#delete duplicates
#tables = ["HormoneTherapy_Survival"]
for table in tables_to_print:
    sql = ('DELETE FROM '+table+' WHERE rowid NOT IN (SELECT MIN(rowid)FROM '+table+' GROUP BY File_number)')
    cursor.execute(sql)

#add nact/act tables to main file

file = 'PCCM_BreastCancerDB_Manasi_test2018-07-23.db'
folders = 'D:/Documents/IISER/Prashanti_docs/QSync/RESEARCH/Clinical_Database/PCCM Clinical Data/2018/08/07'
path = os.path.join(folders, file)
conn = sqlite3.connect(path)
cursor = conn.cursor()

file_all = 'PCCM_BreastCancerDB_all_data.db'
path_all  = os.path.join(folders, file_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()

table = ["Neo_Adjuvant_Therapy", 'Adjuvant_ChemoTherapy']
for index in table:
    sql = "SELECT * FROM '"+index+"'"
    df_ = pd.read_sql(sql, conn)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

#add data to Patient info etc..
from helper_function.pccm_names import db_tables
from sql.add_update_sql import table_check
from helper_function.ask_y_n_statement import ask_option, ask_y_n
from add_edit.output_excel import print_table
import helper_function.table_dicts as table_dicts
import os
import sqlite3
import pandas as pd
from sql.add_update_sql import update_multiple

file_all = 'PCCM_BreastCancerDB_Rituja_2018-10-11.db'
folder_all = 'd:/OneDrive/repos/pccm_db/main/DB'
path = os.path.join(folder_all, file_all)
conn_all = sqlite3.connect(path)
cursor_all = conn_all.cursor()

file_1 = 'PCCM_BreastCancerDB_Rituja_2018-09-17.db'
folders = 'D:/OneDrive/iiser_data/Prashanti_docs/Database_files/2018_10_09/Rituja_data'
path_1 = os.path.join(folders, file_1)
conn_1 = sqlite3.connect(path_1)
cursor_1 = conn_1.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Adjuvant_ChemoTherapy',
          'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_1)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

index = 'Neo_Adjuvant_Therapy'
sql_tumour_size = "ALTER TABLE '" + index + "' ADD COLUMN 'Tumour_size'"
cursor_1.execute(sql_tumour_size)
sql_tumour_size_2 = "UPDATE '" + index + "' SET Tumour_size = Tumour_size_cm"
cursor_1.execute(sql_tumour_size_2)
sql = "SELECT * FROM '" + index + "'"
df_ = pd.read_sql(sql, conn_1)
df_ = df_.drop(columns=['Tumour_size_cm'])
df_.to_sql(index, conn_all, index=False, if_exists="append")

file_2 = 'PCCM_BreastCancerDB_2018-09-27.db'
path_2 = os.path.join(folders, file_2)
conn_2 = sqlite3.connect(path_2)
cursor_2 = conn_2.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_2)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

file_3 = 'PCCM_BreastCancerDB_2018-09-28.db'
path_3 = os.path.join(folders, file_3)
conn_3 = sqlite3.connect(path_3)
cursor_3 = conn_3.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_3)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

file_4 = 'PCCM_BreastCancerDB_2018-10-01.db'
path_4 = os.path.join(folders, file_4)
conn_4 = sqlite3.connect(path_4)
cursor_4 = conn_4.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_4)
    df_.to_sql(index, conn_all, index=False, if_exists="append")




file_5 = 'PCCM_BreastCancerDB_2018-10-08.db'
path_5 = os.path.join(folders, file_5)
conn_5 = sqlite3.connect(path_5)
cursor_5 = conn_5.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_5)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

file_6 = 'PCCM_BreastCancerDB_Rituja_2018-10-10.db'
path_6 = os.path.join(folders, file_6)
conn_6 = sqlite3.connect(path_6)
cursor_6 = conn_6.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_6)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

tables = ["Patient_Information_History", 'Radiology', "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']

for index in tables:
    sql = ('DELETE FROM '+index+' WHERE rowid NOT IN (SELECT MIN(rowid)FROM '+index+' GROUP BY File_number)')
    cursor_all.execute(sql)


conn_all.commit()
conn_all.close()

file_rituja = 'PCCM_BreastCancerDB_all_data_rituja.db'
folders_rituja = 'D:/Documents/IISER/Prashanti_docs/QSync/RESEARCH/Clinical_Database/PCCM Clinical Data/2018/08/07'
path_rituja = os.path.join(folders_rituja, file_rituja)
conn_rituja = sqlite3.connect(path)
cursor_rituja = conn_rituja.cursor()
tables = ["Patient_Information_History", "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding']

modules = table_dicts.table_module_dict(table)
columns = []
if modules == []:
    columns = table_dicts.db_dict(table, modules)
else:
    for module in modules:
        cols = table_dicts.db_dict(table, module)
        columns = columns + cols
col_list = table_dicts.create_col_list(columns)
files = ['499/15', '657/16', '509/15']
for table in tables:
    for file in files:
        sql = "SELECT * FROM '" + table + "'"
        df_ = pd.read_sql(sql, conn_nutan)
        df_.to_sql(index, conn_all, index=False, if_exists="append")


## change column name
    sql_tumour_size = "ALTER TABLE '" + index + "' ADD COLUMN 'Tumour_size'"
    cursor_1.execute(sql_tumour_size)
    sql_tumour_size_2 = "UPDATE '" + index + "' SET Tumour_size = Tumour_size_cm"
    cursor_1.execute(sql_tumour_size_2)
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_1)
    df_ = df_.drop(columns=['Tumour_size_cm'])
    df_.to_sql(index, conn_all, index=False, if_exists="append")

to_delete = {'test','Test',' 375/14'}
folders = "d:/repos/pccm_db/main/DB/from_linux/"
file = 'PCCM_BreastCancerDB_all_data_clean_28052018.db'
path_all = os.path.join(folders, file)
os.path.isfile(path_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()
table = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy',
          'Adjuvant_ChemoTherapy', 'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in table:
    sql = "SELECT File_number FROM '"+index+"'"
    df = pd.read_sql(sql, conn_all)
    df_list= list(df['File_number'])
    df_del = ['test','Test',' 375/14']
    if df_del != []:
        for j in df_del:
            sql = "DELETE FROM '" + index + "' WHERE File_number = '" + j + "'"
            cursor_all.execute(sql)
conn_all.commit()
conn_all.close()


file_all = 'PCCM_BreastCancerDB_Rohini_2018-10-10.db'
folder_all = 'D:/OneDrive/iiser_data/Prashanti_docs/Database_files/2018_10_09'
path = os.path.join(folder_all, file_all)
conn_all = sqlite3.connect(path)
cursor_all = conn_all.cursor()

file_1 = 'PCCM_BreastCancerDB_2018-10-08.db'
folders = 'D:/OneDrive/iiser_data/Prashanti_docs/Database_files/2018_10_09'
path_1 = os.path.join(folders, file_1)
conn_1 = sqlite3.connect(path_1)
cursor_1 = conn_1.cursor()
tables = ["Patient_Information_History", 'Radiology', "Follow_up_Data", "HormoneTherapy_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding', 'NACT_Tox_table','NACT_Drug_Table', 'Neo_Adjuvant_Therapy','Adjuvant_ChemoTherapy',
          'Chemo_Tox_table', 'Chemo_Drug_Table']
for index in tables:
    sql = "SELECT * FROM '" + index + "'"
    df_ = pd.read_sql(sql, conn_1)
    df_.to_sql(index, conn_all, index=False, if_exists="append")

# delete NACT entry for Rohini
tables = 'Neo_Adjuvant_Therapy', 'NACT_Tox_table', 'NACT_Drug_Table'
for table in tables:
    sql = "SELECT File_number FROM '"+table+"'"
    df = pd.read_sql(sql, conn_all)
    df_list= list(df['File_number'])
    df_del = ['163/12', '57/15', '396/17']
    if df_del != []:
        for j in df_del:
            sql = "DELETE FROM '" + table + "' WHERE File_number = '" + j + "'"
            cursor_all.execute(sql)
conn_all.commit()
conn_all.close()

sql = "DROP TABLE 'Follow_up_Data'"
cursor_all.execute(sql)
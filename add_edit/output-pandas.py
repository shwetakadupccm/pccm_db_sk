import pandas as pd
import helper_function.pccm_names as names
import os
import sqlite3

folders = 'D:/repos/pccm_db/main/DB/from_linux'
file = "PCCM_BreastCancerDB_all_data.db"
ex_file = 'Output_radiology_12062018.xlsx'
path = os.path.join(folders, file)
ex_path = os.path.join(folders, ex_file)
conn = sqlite3.connect(path)

table = "radiotherapy"
col_list = ["File_number"] + names.names_radiation()
sql = ('SELECT ' + ", ".join(col_list[:-2]) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
df.to_excel(writer, sheet_name=table)

table = "hormonetherapy_recurrence_survival"
col_list = ["File_number"] + names.names_longterm("hormone") + names.names_longterm("metastasis")
sql = ('SELECT ' + ", ".join(col_list[:-2]) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name="Hormone_RecurrenceSurvival")


table = "follow_up_data"
col_list = ["File_number"] + names.name_follow_up()
sql = ('SELECT ' + ", ".join(col_list[:-2]) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table)

table = "patient_information_history"
col_list_bio = names.names_info("bio_info")

col_list = ["File_number"] + col_list_bio + names.names_info("phys_act") + names.names_info("habits") + \
           names.names_info("nut_supplements") + names.names_info("family_details") + names.names_info("med_history") + \
           names.names_info("cancer_history") + names.names_info("family_cancer") + names.names_info("breast_symptoms")
sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table)
writer.save()


#######################################33

table = "Biopsy_Report_Data"
module_names = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + names.names_biopsy(index)
sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table, index=False)
#writer.save()

table = "Surgery_Block_Report_Data"
module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + names.names_surgery(index)
sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table, index=False)
writer.save()

table = "Radiology"
sql = "SELECT File_number FROM '"+table+"'"
df = pd.read_sql(sql, conn)
df_list= list(df['File_number'])

module_names = ["mammography", "tomosynthesis", "abvs", "sonomammo",
                    "mri_breast"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + names.names_radio(index)
sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table, index=False)
writer.save()


table = "Surgery_Report"
sql = "SELECT File_number FROM '"+table+"'"
df = pd.read_sql(sql, conn)
df_list= list(df['File_number'])
module_names = ["surgery_information", "node_excision","post_surgery"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + names.names_surgery_information(index)
sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
df = pd.read_sql(sql, conn)
df.to_excel(writer, sheet_name=table, index=False)
writer.save()
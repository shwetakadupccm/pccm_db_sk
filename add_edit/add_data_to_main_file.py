import sqlite3
from sql.add_update_sql import add_columns, table_check
from datetime import date
import os
import helper_function.pccm_names as pccm_names
import pandas as pd

folder = "d:/repos/pccm_db/main/DB/DB_with_real_data"
db_name = 'PCCM_BreastCancerDB_all_data.db'
path = os.path.join(folder, db_name)
conn_all = sqlite3.connect(path)
cursor_all = conn_all.cursor()
file_number = "file_number"
table = "patient_information_history"
if table_check(cursor_all, table) == 0:
    cursor_all.execute('CREATE TABLE {tn}({nf})'\
                   .format(tn=table, nf=file_number))
    module_names = ["bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                    "cancer_history", "family_cancer", "det_by", "breast_symptoms"]
    for index in module_names:
        col_name = pccm_names.names_info(index)
        add_columns(cursor_all, table, col_name)
table = "radiotherapy"
if table_check(cursor_all, table) == 0:
    column = ", ".join(pccm_names.names_radiation())
    cols_file = "file_number, "+column
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))

table = "follow_up_data"
if table_check(cursor_all, table) == 0:
    column = ", ".join(pccm_names.name_follow_up())
    cols_file = "file_number, " + column
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))

table = "hormonetherapy_recurrence_survival"
if table_check(cursor_all, table) == 0:
    column = "file_number"
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    module_names = ["hormone", "metastasis"]
    for index in module_names:
        col_name = pccm_names.names_longterm(index)
        add_columns(cursor_all, table, col_name)

table = "General_Medical_History"
if table_check(cursor_all, table) == 0:
    columns2 = "file_number, Condition, Diagnosis_date, Treatment"
    cursor_all.execute('CREATE TABLE {tn}({nf})' \
                   .format(tn=table, nf=columns2))

table = "Family_Cancer_History"
if table_check(cursor_all, table) == 0:
    columns3 = 'file_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
    cursor_all.execute('CREATE TABLE {tn}({nf})' \
                   .format(tn=table, nf=columns3))

table = "Previous_Cancer_History"
if table_check(cursor_all, table) == 0:
    columns4 = "file_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation," \
               "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone," \
               "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy," \
               "Type_HomeRemedy,Duration_HomeRemedy"
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns4))

table = "Nutritional_Supplements"
if table_check(cursor_all, table) == 0:
    columns5 = "file_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns5))

table = "Physical_Activity"
if table_check(cursor_all, table) == 0:
    columns7 = "file_number, Type_activity, Frequency_activity"
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns7))

table = "Breast_Feeding"
if table_check(cursor_all, table) == 0:
    columns8 = "file_number, Child_number, Feeding_duration, Breast_usage_feeding"
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns8))

folder_patient = 'D:/repos/pccm_db/main/DB/'
db_patient = 'PCCM_BreastCancerDB_added_name_and_update1_2018-04-18.db'
path_patient = os.path.join(folder_patient, db_patient)
conn_patient = sqlite3.connect(path_patient)
cursor_patient = conn_patient.cursor()

#clean_up data for wrong/test entries
to_do = {'55/17', '257/16', '270/14', '222/12', '443/15', '283/12', '651/15', '593/15', '574/15', '571/15'}

table = ["Patient_Information_History", "Follow_up_Data", "HormoneTherapy_Recurrence_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding']
for index in table:
    sql = "SELECT file_number FROM '"+index+"'"
    df = pd.read_sql(sql, conn_patient)
    df_list= list(df['file_number'])
    df_del = []
    for i in df_list:
        if i not in to_do:
            df_del.append(i)
    if df_del != []:
        for j in df_del:
            sql = "DELETE FROM '"+index+"' WHERE file_number = '"+j+"'"
            cursor_patient.execute(sql)

table = ["Patient_Information_History", "Follow_up_Data", "HormoneTherapy_Recurrence_Survival", "RadiotherapyOptions",
         "General_Medical_History", "Family_Cancer_History", 'Previous_Cancer_History', 'Nutritional_Supplements',
         'Physical_Activity', 'Breast_Feeding']
for index in table:
    sql = "SELECT * FROM '"+index+"'"
    df = pd.read_sql(sql, conn_patient)
    df_= df.drop_duplicates()
    df_.to_sql(index, conn_all, index=False, if_exists="append")


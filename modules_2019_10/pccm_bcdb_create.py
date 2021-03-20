import sqlite3
from sql.add_update_sql import add_columns, table_check
from datetime import datetime
import os
import modules.pccm_names as pccm_names


folder = "d:/repos/pccm_db/main/DB"
db_name = 'PCCM_BreastCancerDB_FFPE_check_2019-05-11.db'
db_name = "PCCM_BreastCancerDB_" + datetime.now().strftime("%Y_%m_%d") + '.db'

path = os.path.join(folder, db_name)

conn = sqlite3.connect(path)
cursor = conn.cursor()
file_number = "file_number"
table = "patient_information_history"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    module_names = ["bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                    "cancer_history", "family_cancer", "det_by", "breast_symptoms", 'other_test']
    for index in module_names:
        col_name = pccm_names.names_info(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = "biopsy_path_report_data"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf='pk'))
    module_names = ["biopsy_report_info", "biopsy_details", 'ihc_biopsy_data', 'review_biopsy']
    for index in module_names:
        col_name = pccm_names.names_biopsy(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = 'surgery_path_report_data'
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})' .format(tn=table, nf='fk'))
    module_names = ["surgery_block_information_0", "surgery_block_information_1", "surgery_block_information_2",
                    "surgery_block_information_3"]
    for index in module_names:
        col_name = pccm_names.names_surgery(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = "block_data"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf='fk'))
    col_name = pccm_names.names_surgery('block_data')[1:]
    add_columns(cursor, table, col_name)
    print(table + ' created')

table = "radiology"
if table_check(cursor, table) == 0:
    module_names = ["mammography", "abvs", "sonomammo",
                    "mri_breast"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_radio(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = 'pet_reports'
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})' .format(tn=table, nf='pk'))
    module_names = ['pet_report_identifier', 'pet_report_findings', 'pet_breast_cancer']
    for index in module_names:
        col_name = pccm_names.names_pet(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = "surgery_report"
if table_check(cursor, table) == 0:
    module_names = ["surgery_information", "node_excision", "post_surgery"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_surgery_information(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = "general_medical_history"
if table_check(cursor, table) == 0:
    columns2 = "file_number, Condition, Diagnosis_date, Treatment"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns2))
    print(table + ' created')

table = "family_cancer_history"
if table_check(cursor, table) == 0:
    columns3 = 'file_number, type_cancer, relation_to_patient, type_relation, age_at_detection_yrs'
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns3))
    print(table + ' created')

table = "previous_cancer_history"
if table_check(cursor, table) == 0:
    columns4 = "file_number, type_cancer, year_diagnosis, surgery, type_surgery, duration_surgery, radiation," \
               "type_radiation,duration_radiation,chemotherapy,type_chemotherapy,duration_chemotherapy,hormone," \
               "type_hormone,duration_hormone,alternative,type_alternative,duration_alternative,homeremedy," \
               "type_homeremedy,duration_homeremedy"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns4))
    print(table + ' created')

table = "nutritional_supplements"
if table_check(cursor, table) == 0:
    columns5 = "file_number, type_nutritional_supplements, quantity_nutritional_supplements_per_day, " \
               "duration_nutritional_supplements"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns5))
    print(table + ' created')

table = "physical_activity"
if table_check(cursor, table) == 0:
    columns7 = "file_number, type_activity, frequency_activity"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns7))
    print(table + ' created')

table = "breast_feeding"
if table_check(cursor, table) == 0:
    columns8 = "file_number, child_number, feeding_duration, breast_usage_feeding"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns8))
    print(table + ' created')

table = "nact_tox_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_nact(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    print(table + ' created')

table = "nact_drug_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_nact(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    print(table + ' created')

table = "neo_adjuvant_therapy"
if table_check(cursor, table) == 0:
    module_names = ["neo_adjuvant_therapy", "clip_information"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_nact(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = "adjuvant_chemotherapy"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cols_file = "file_number, " + column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))
    print(table + ' created')


table = "chemo_tox_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    print(table + ' created')

table = "chemo_drug_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    print(table + ' created')

table = "radiotherapy"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_radiation())
    cols_file = "file_number, "+column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))
    print(table + ' created')

table = "follow_up_data"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.name_follow_up())
    cols_file = "file_number, " + column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))
    print(table + ' created')

table = "hormonetherapy_survival"
if table_check(cursor, table) == 0:
    column = "file_number"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    module_names = ["hormone", "metastasis"]
    for index in module_names:
        col_name = pccm_names.names_longterm(index)
        add_columns(cursor, table, col_name)
    print(table + ' created')

table = 'block_list'
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.block_list('all'))
    cols_file = "pk, " + column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))
    print(table + ' created')
conn.commit()
print(path + " file created")
conn.close()

import sqlite3
import sql.add_update_sql as sql
import pandas as pd
from add_edit.db_names import DB_list, Tables, FilesSubtype
from add_edit.output_excel import get_col_list


def add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name, cols_set_new):
    file_added = []
    for file in file_list:
        for col in range(0, len(cols_set_old)):
            sql_statement = 'SELECT ' + cols_set_old[col] + ' FROM ' + table_old + " WHERE " + file_number_name + \
                            " = '" + file + "'"
            data_old = cursor_old.execute(sql_statement)
            if data_old != []:
                data = data_old.fetchall()[0][0]
                sql.update_single(conn_new, cursor_new, table, column=cols_set_new[col], file_number=file, var=data)
                print(file, 'added to new database')
                file_added = file_added + [file]
    print (str(len(file_added)) + 'files added to ' + table)


def add_supp_table (table_old, conn_old, col_new, conn_new, table):
    sql_statement = 'SELECT * FROM ' + table_old
    df_old = pd.read_sql(sql_statement, conn_old)
    df_old.columns = col_new
    df_old.to_sql(table, conn_new, index=False, if_exists='append')


def add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table):
    sql_statement = 'SELECT ' + file_number_name + ' from ' + table_old
    file_number = cursor_old.execute(sql_statement)
    file_number = file_number.fetchall()
    file_list = []
    for file in file_number:
        file_var = file[0]
        sql.add_pk_fk_to_table(conn_new, cursor_new, col_name='file_number', pk=file_var, table=table)
        file_list.append(file_var)
    return file_list

def update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_names_new, col_names_old):
    df_old = pd.read_excel(file_name_excel, sheet_name=sheet, index_col=0)
    df_old = df_old.astype(str)
    file_number_old = list(df_old.index)
    table_name = Tables.sheet_name[sheet]
    print(table_name)
    sql_statement = 'SELECT file_number from ' + table_name
    file_number = cursor_new.execute(sql_statement)
    file_number_sql = file_number.fetchall()
    file_list_sql = []
    for file in file_number_sql:
        file_var = file[0]
        file_list_sql.append(file_var)
    file_to_add = list(set(file_number_old) - set(file_list_sql))
    if len(file_to_add)>0:
        for file in file_to_add:
            print(file)
            sql.add_pk_fk_to_table(conn_new, cursor_new, col_name='file_number', pk=file, table=table_name)
            data = df_old.loc[file]
            for col in range(0, len(col_names_old)):
                sql.update_single(conn_new, cursor_new, table_name, col_names_new[col], file,
                                  data.loc[col_names_old[col]])
                print(file, ' added to ', table_name, col_names_new[col])
    else:
        print('No new files to add')

conn_new = sqlite3.connect(DB_list.new_db)
conn_old = sqlite3.connect(DB_list.old_db)

cursor_new = conn_new.cursor()
cursor_old = conn_old.cursor()

sql_statement = "SELECT name FROM sqlite_master WHERE type='table'"
tables = cursor_old.execute(sql_statement)
table_list = tables.fetchall()
table_list

pccm_names_file = "F:\pccm_db_backup\pccm_db_2019_07_09\modules\pccm_names.py"
table_name = 'patient_information_history'
table_old =  table_name
file_number_name = 'file_number'


file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table_name)

cols_set_old = ['nutritional_supplements_y_n', 'type_nutritional_supplements', 'quantity_nutritional_supplements',
                    'duration_nutritional_supplements']
col_set_new =['nutritional_supplements_y_n', 'type_nutritional_supplements', 'quantity_nutritional_supplements',
                    'duration_nutritional_supplements']


add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table_name, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['physical_activity_y_n', 'type_physical_activity', 'frequency_physical_activity']
col_set_new =['physical_activity_y_n', 'type_physical_activity', 'frequency_physical_activity']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['any_other_medical_history_y_n', 'type_any_other_medical_history',
                    'diagnosis_date_any_other_medical_history', 'treatment_any_other_medical_history']
col_set_new =['any_other_medical_history_y_n', 'type_any_other_medical_history',
                    'diagnosis_date_any_other_medical_history', 'treatment_any_other_medical_history']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['previous_cancer_history_y_n', 'type_previous_cancer', 'year_diagnosed_previous_cancer',
                    'treatment_previous_cancer', 'treatment_type_previous_cancer', 'treatment_duration_previous_cancer']
col_set_new =['previous_cancer_history_y_n', 'type_previous_cancer', 'year_diagnosed_previous_cancer',
                    'treatment_previous_cancer', 'treatment_type_previous_cancer', 'treatment_duration_previous_cancer']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['marital_status', 'siblings', 'sisters', 'brothers', 'children', 'daughters', 'sons',
                    'menarche_yrs', 'menopause_status', 'age_at_menopause_yrs', 'date_last_menstrual_period',
                    'period_type', 'number_pregnancies', 'pregnancy_to_term', 'number_abortions', 'age_first_child',
                    'age_first_pregnancy', 'age_last_child', 'age_last_pregnancy', 'two_births_in_year',
                    'breast_feeding', 'child_breast_feeding', 'duration_breast_feeding', 'breast_usage_breast_feeding',
                    'fertility_treatment_y_n', 'type_fertility_treatment', 'details_fertility_treatment',
                    'cycles_fertility_treatment', 'success_fertility_treatment', 'type_birth_control_used',
                    'details_birth_control', 'duration_birth_control']
col_set_new =['marital_status', 'siblings', 'sisters', 'brothers', 'children', 'daughters', 'sons',
                    'menarche_yrs', 'menopause_status', 'age_at_menopause_yrs', 'date_last_menstrual_period',
                    'period_type', 'number_pregnancies', 'pregnancy_to_term', 'number_abortions', 'age_first_child',
                    'age_first_pregnancy', 'age_last_child', 'age_last_pregnancy', 'two_births_in_year',
                    'breast_feeding', 'child_breast_feeding', 'duration_breast_feeding', 'breast_usage_breast_feeding',
                    'fertility_treatment_y_n', 'type_fertility_treatment', 'details_fertility_treatment',
                    'cycles_fertility_treatment', 'success_fertility_treatment', 'type_birth_control_used',
                    'details_birth_control', 'duration_birth_control']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['rb_symptoms', 'rb_symptoms_duration', 'lb_symptoms', 'lb_symptoms_duration', 'rb_other_symptoms',
                    'rb_other_symptoms_duration', 'lb_other_symptoms', 'lb_other_symptoms_duration',
                    'patient_metastasis_symptoms']
col_set_new =['rb_symptoms', 'rb_symptoms_duration', 'lb_symptoms', 'lb_symptoms_duration', 'rb_other_symptoms',
                    'rb_other_symptoms_duration', 'lb_other_symptoms', 'lb_other_symptoms_duration',
                    'patient_metastasis_symptoms']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

col_set_new =['diet', 'alcohol_y_n', 'alcohol_consumption_age_yrs', 'quantity_alcohol_per_week',
                    'duration_alcohol', 'comments_alcohol', 'tobacco_y_n', 'exposure_mode', 'type_passive',
                    'type_tobacco', 'tobacco_consumption_age_yrs', 'tobacco_frequency', 'quantity_tobacco_per_week',
                    'duration_tobacco', 'comments_tobacco', 'other_deleterious_habits']
cols_set_old = ['diet', 'alcohol_y_n', 'alcohol_consumption_age_yrs', 'quantity_alcohol_per_week',
                    'duration_alcohol', 'comments_alcohol', 'tobacco_y_n', 'exposure_mode', 'type_passive',
                    'type_tobacco', 'tobacco_consumption_age_yrs', 'tobacco_frequency', 'quantity_tobacco_per_week',
                    'duration_tobacco', 'comments_tobacco', 'other_deleterious_habits']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)
cols_set_old = ['current_breast_cancer_detected_by', 'current_breast_cancer_detected_date']
col_set_new =['current_breast_cancer_detected_by', 'current_breast_cancer_detected_date']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['familycancer_history_y_n', 'type_degreerelation_typerelation_age_familycancer']
col_set_new =['familycancer_history_y_n', 'type_degreerelation_typerelation_age_familycancer']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['mr_number', 'name', 'aadhaar_card', 'firstvisit_date', 'permanent_address', 'current_address',
                    'phone', 'email_id', 'gender', 'age_at_first_visit_yrs', 'diagnosis_age_yrs', 'date_of_birth',
                    'place_birth', 'height_cm', 'weight_kg', 'bmi']
col_set_new =['mr_number', 'name', 'aadhaar_card', 'firstvisit_date', 'permanent_address', 'current_address',
                    'phone', 'email_id', 'gender', 'age_at_first_visit_yrs', 'diagnosis_age_yrs', 'date_of_birth',
                    'place_birth', 'height_cm', 'weight_kg', 'bmi']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['usg_abdomen', 'diagnosis_usg_abdomen', 'details_diagnosis_usg_abdomen', 'cect_abd_thorax',
                    'visceral_metastasis_cect_abd_thorax', 'details_visceral_metastasis_cect_abd_thorax', 'pet_scan',
                    'visceral_metastasis_pet_scan', 'detail_visceral_metastasis_pet_scan',
                    'skeletal_metastasis_pet_scan', 'detail_skeletal_metastasis_pet_scan', 'bone_scan',
                    'skeletal_metastasis_bone_scan', 'detail_skeletal_metastasis_bone_scan',
                    'update_by', 'last_update']
col_set_new =['usg_abdomen', 'diagnosis_usg_abdomen', 'details_diagnosis_usg_abdomen', 'cect_abd_thorax',
                    'visceral_metastasis_cect_abd_thorax', 'details_visceral_metastasis_cect_abd_thorax', 'pet_scan',
                    'visceral_metastasis_pet_scan', 'detail_visceral_metastasis_pet_scan',
                    'skeletal_metastasis_pet_scan', 'detail_skeletal_metastasis_pet_scan', 'bone_scan',
                    'skeletal_metastasis_bone_scan', 'detail_skeletal_metastasis_bone_scan',
                    'update_by', 'last_update']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)
#-----------------------------#

table = 'general_medical_history'
table_old =  'general_medical_history'
col_old = 'file_number', 'Condition', 'Diagnosis_date', 'Treatment'
col_new = ['file_number', 'Condition', 'Diagnosis_date', 'Treatment']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'family_cancer_history'
table_old =  'family_cancer_history'
col_old = "File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs"
col_new = ['file_number', 'type_cancer', 'relation_to_patient', 'type_relation', 'age_at_detection_yrs']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'previous_cancer_history'
table_old =  'previous_cancer_history'
col_old = "File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation," \
               "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone," \
               "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy," \
               "Type_HomeRemedy,Duration_HomeRemedy"
col_new = ["file_number", 'type_cancer', 'year_diagnosis', 'surgery', 'type_surgery', 'duration_surgery', 'radiation',
           'type_radiation', 'duration_radiation' ,'chemotherapy', 'type_chemotherapy', 'duration_chemotherapy',
           'hormone', 'type_hormone' , 'duration_hormone', 'alternative', 'type_alternative', 'duration_alternative',
           'homeremedy', 'type_homeremedy', 'duration_homeremedy']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'nutritional_supplements'
table_old =  'nutritional_supplements'
col_old = "File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
col_new = ['file_number', 'type_nutritional_supplements', 'quantity_nutritional_supplements_per_day', \
               'duration_nutritional_supplements']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'physical_activity'
table_old =  'physical_activity'
col_old = "File_number, Type_activity, Frequency_activity"
col_new = ['file_number', 'type_activity', 'frequency_activity']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'breast_feeding'
table_old =  'breast_feeding'
col_old = "File_number, Child_number, Feeding_duration, Breast_usage_feeding"
col_new = ['file_number', 'child_number', 'feeding_duration', 'breast_usage_feeding']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'nact_tox_table'
table_old =  'nact_tox_table'
col_old = "File_number", "Drug_Administered", "Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment", \
          "Cycle_Toxicity", "ChangedTreatment_Toxicity"
col_new = ['file_number', 'drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity', 'changedtreatment_toxicity']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'nact_drug_table'
table_old =  'nact_drug_table'
col_old = ['File_number', 'Drug', 'Number_cycle', 'Cycle_frequency_per_week', 'Drug_dose', 'Dose_unit']
col_new = ['file_number', 'drugs_administered', 'number_cycle', 'cycle_frequency_per_week', 'drug_dose', 'dose_unit']
add_supp_table (table_old, conn_old, col_new, conn_new, table)


pccm_names_file = 'D:/repos/pccm_db_backup/pccm_db_2019_07_15/helper_function/pccm_names.py'
table = 'neo_adjuvant_therapy'
table_old =  'neo_adjuvant_therapy'
file_number_name = 'file_number'

file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table)

cols_set_old = ['nact_status', 'place_nact', 'details_nact', 'plan_nact', 'date_start_nact',
                    'patient_weight_nact', 'nact_drugs_administered', 'number_cycles_nact', 'cycle_weekly_frequency',
                    'drugs_totaldose', 'drugs_unit', 'toxicity_type', 'toxicity_grade', 'toxicity_treatment',
                    'toxicity_response', 'toxicity_at_cycle', 'nact_change_due_to_toxicity',
                    'tumour_response_check_method', 'tumour_response_nact', 'tumour_size', 'tumour_size_unit',
                    'nact_response_impression', 'nact_response_node', 'date_tumour_size_checked',
                    'nact_completion_status', 'nact_end_date', 'trastuzumab_use_nact', 'trastuzumab_regime_nact',
                    'trastuzumab_courses_taken_nact', 'hormone_therapy_nact', 'hormone_therapy_type_nact', 'hormone_therapy_duration',
                    'horomone_therapy_side_effects', 'update_by', 'last_update']
col_set_new =['nact_status', 'place_nact', 'details_nact', 'plan_nact', 'date_start_nact',
                    'patient_weight_nact', 'nact_drugs_administered', 'number_cycles_nact', 'cycle_weekly_frequency',
                    'drugs_totaldose', 'drugs_unit', 'toxicity_type', 'toxicity_grade', 'toxicity_treatment',
                    'toxicity_response', 'toxicity_at_cycle', 'nact_change_due_to_toxicity',
                    'tumour_response_check_method', 'tumour_response_nact', 'tumour_size', 'tumour_size_unit',
                    'nact_response_impression', 'nact_response_node', 'date_tumour_size_checked',
                    'nact_completion_status', 'nact_end_date', 'trastuzumab_use_nact', 'trastuzumab_regime_nact',
                    'trastuzumab_courses_taken_nact', 'hormone_therapy_nact', 'hormone_therapy_type_nact', 'hormone_therapy_duration',
                    'horomone_therapy_side_effects', 'update_by', 'last_update']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['clip_number', 'clip_date', 'clip_insertion_after_cycle']
col_set_new =['clip_number', 'clip_date', 'clip_insertion_after_cycle']
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

table = 'adjuvant_chemotherapy'
table_old =  'adjuvant_chemotherapy'
file_number_name = 'file_number'

file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table)

cols_set_old = ['chemotherapy_status', 'place_chemotherapy', 'details_chemotherapy', 'plan_chemotherapy',
                    'date_start_chemotherapy', 'patient_weight_chemotherapy', 'drugs_administered',
                    'number_cycles_chemotherapy', 'cycle_weekly_frequency', 'drugs_totaldose', 'drugs_unit',
                    'toxicity_type', 'toxicity_grade', 'toxicity_treatment', 'toxicity_response', 'toxicity_at_cycle',
                    'chemotherapy_change_due_to_toxicity', 'chemotherapy_completion_status',
                    'chemotherapy_end_date', 'trastuzumab_use_chemotherapy', 'trastuzumab_regime_chemotherapy',
                    'trastuzumab_courses_taken_chemotherapy', 'ovary_status', 'hormone_therapy_chemotherapy',
                    'hormone_therapy_type_chemotherapy', 'hormone_therapy_duration_chemotherapy',
                    'horomone_therapy_side_effects_chemotherapy', 'update_by', 'last_update']

col_set_new = ['chemotherapy_status', 'place_chemotherapy', 'details_chemotherapy', 'plan_chemotherapy',
                'date_start_chemotherapy', 'patient_weight_chemotherapy', 'drugs_administered',
                'number_cycles_chemotherapy', 'cycle_weekly_frequency', 'drugs_totaldose', 'drugs_unit',
                'toxicity_type', 'toxicity_grade', 'toxicity_treatment', 'toxicity_response', 'toxicity_at_cycle',
                'chemotherapy_change_due_to_toxicity', 'chemotherapy_completion_status',
                'chemotherapy_end_date', 'trastuzumab_use_chemotherapy', 'trastuzumab_regime_chemotherapy',
                'trastuzumab_courses_taken_chemotherapy', 'ovary_status', 'hormone_therapy_chemotherapy',
                'hormone_therapy_type_chemotherapy', 'hormone_therapy_duration_chemotherapy',
                'horomone_therapy_side_effects_chemotherapy', 'update_by', 'last_update']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

table = 'chemo_tox_table'
table_old =  'chemo_tox_table'
col_old = ['file_number', 'drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity', 'changedtreatment_toxicity']
col_new = ['file_number', 'drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity', 'changedtreatment_toxicity']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'chemo_drug_table'
table_old =  'chemo_drug_table'
col_old = ['File_number', 'Drug', 'Number_cycle', 'Cycle_frequency_per_week', 'Drug_dose', 'Dose_unit']
col_new = ['file_number', 'drug', 'number_cycle', 'cycle_frequency_per_week', 'drug_dose', 'dose_unit']
add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = 'radiology'
table_old =  'radiology'
file_number_name = 'file_number'

file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table)

cols_set_old = ['mammography', 'mammography_date', 'mammography_place', 'mammography_indication',
                'mammography_breast', 'mammography_massnumber', 'mammography_masslocation', 'mammography_massshape',
                'mammography_massmargin', 'mammography_massnipple_cm', 'mammography_masssize',
                'mammography_masssize_unit', 'mammography_calcificationnumber', 'mammography_calcificationlocation',
                'mammography_calcificationtype', 'mammography_calcification_comments',
                'mammography_skin_involvement', 'mammography_node_description','mammography_node_size',
                'mammography_node_size_unit', 'mammography_birad', 'mammography_impression', 'tomography_y_n']

col_set_new =  ['mammography', 'mammography_date', 'mammography_place', 'mammography_indication',
                'mammography_breast', 'mammography_massnumber', 'mammography_masslocation', 'mammography_massshape',
                'mammography_massmargin', 'mammography_massnipple_cm', 'mammography_masssize',
                'mammography_masssize_unit', 'mammography_calcificationnumber', 'mammography_calcificationlocation',
                'mammography_calcificationtype', 'mammography_skin_involvement', 'mammography_calcification_comments',
                'mammography_node_description','mammography_node_size',
                'mammography_node_size_unit', 'mammography_birad', 'mammography_impression', 'tomography_y_n']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['automated_breast_volume_scanner_abvs', 'date_abvs', 'accession_abvs', 'lesion_abvs',
                    'lesion_location_abvs', 'size_abvs', 'distance_abvs', 'distance_pectmajor_abvs', 'diagnosis_abvs']

col_set_new =  ['automated_breast_volume_scanner_abvs', 'date_abvs', 'accession_abvs', 'lesion_abvs',
                    'lesion_location_abvs', 'size_abvs', 'distance_abvs', 'distance_pectmajor_abvs', 'diagnosis_abvs']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['sonomammography_status', 'sonomammo_date', 'sonomammo_breast', 'sonomammo_mass', 'sonomammo_mass_number',
                    'sonomammo_mass_location', 'sonomammo_mass_clock', 'sonomammo_mass_shape', 'sonomammo_mass_margin',
                    'sonomammo_mass_echo', 'sonomammo_mass_size', 'sonomammo_mass_size_unit', 'sonomammo_calc',
                    'sonomammo_calc_type', 'sonomammo_vascularity', 'sonomammo_birad', 'sonomammo_node_description',
                    'sonomammo_node_size', 'sonomammo_node_size_unit', 'sonomammo_impression', 'update_by',
                    'last_update']

col_set_new =  ['sonomammography_status', 'sonomammo_date', 'sonomammo_breast', 'sonomammo_mass', 'sonomammo_mass_number',
                    'sonomammo_mass_location', 'sonomammo_mass_clock', 'sonomammo_mass_shape', 'sonomammo_mass_margin',
                    'sonomammo_mass_echo', 'sonomammo_mass_size', 'sonomammo_mass_size_unit', 'sonomammo_calc',
                    'sonomammo_calc_type', 'sonomammo_vascularity', 'sonomammo_birad', 'sonomammo_node_description',
                    'sonomammo_node_size', 'sonomammo_node_size_unit', 'sonomammo_impression', 'update_by',
                    'last_update']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['mri_status', 'date_mri', 'accession_number_mri', 'mri_breast', 'fibroglandular_tissue_mri',
                'background_paranchymal_enhancement_level_mri', 'background_paranchymal_enhancement_symmetry_mri',
                'focus_mri', 'mass_mri', 'number_mass_mri', 'mass_location_mri', 'mass_shape_mri',
                'mass_margin_mri', 'mass_internal_enhancement_char_mri', 'asso_features_nipple_retraction_mri',
                'asso_features_nipple_invasion_mri', 'asso_features_skin_retraction_mri',
                'asso_features_skin_thickening_mri', 'asso_features_axillary_adenopathy_mri',
                'asso_features_pectoralismuscle_invasion_mri', 'asso_features_chestwall_invasion_mri',
                'asso_features_architectural_distortion_mri', 'asso_features_skin_invasion_mri',
                'fat_lesion_mri', 'kinetics_initial_mri', 'kinetics_delayed_mri',
                'non_enhanced_features_mri', 'implant_mri', 'lesion_mri',
                'lesion_location_mri', 'lesion_depth_mri', 'lesion_size_mri',
                'distancefromskin_mri', 'distancefrompectmaj_mri', 'mri_birad',
                'user_name_mri', 'last_update_mri']

col_set_new =  ['mri_status', 'date_mri', 'accession_number_mri', 'mri_breast', 'fibroglandular_tissue_mri',
                'background_paranchymal_enhancement_level_mri', 'background_paranchymal_enhancement_symmetry_mri',
                'focus_mri', 'mass_mri', 'number_mass_mri', 'mass_location_mri', 'mass_shape_mri',
                'mass_margin_mri', 'mass_internal_enhancement_char_mri', 'asso_features_nipple_retraction_mri',
                'asso_features_nipple_invasion_mri', 'asso_features_skin_retraction_mri',
                'asso_features_skin_thickening_mri', 'asso_features_axillary_adenopathy_mri',
                'asso_features_pectoralismuscle_invasion_mri', 'asso_features_chestwall_invasion_mri',
                'asso_features_architectural_distortion_mri', 'asso_features_skin_invasion_mri',
                'fat_lesion_mri', 'kinetics_initial_mri', 'kinetics_delayed_mri',
                'non_enhanced_features_mri', 'implant_mri', 'lesion_mri',
                'lesion_location_mri', 'lesion_depth_mri', 'lesion_size_mri',
                'distancefromskin_mri', 'distancefrompectmaj_mri', 'mri_birad',
                'user_name_mri', 'last_update_mri']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

table = "radiotherapy"
table_old = "radiotherapy"
file_number_name = 'file_number'

file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table)

cols_set_old = ['radiation_received', 'radiation_date', 'radiation_type', 'imrt_dcrt', 'radiation_acute_toxicity',
                'radiation_delayed_toxicity', 'radiation_finish_date', 'radiation_location', 'radiation_oncologist',
                'update_by', 'last_update']

col_set_new =  ['radiation_received', 'radiation_date', 'radiation_type', 'imrt_dcrt', 'radiation_acute_toxicity',
                'radiation_delayed_toxicity', 'radiation_finish_date', 'radiation_location', 'radiation_oncologist',
                'update_by', 'last_update']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

table = "follow_up_data"
table_old = "follow_up_data"

col_old = ['file_number', 'follow_up_period', 'follow_up_status', 'follow_up_mammography_date', 'follow_up_mammography',
           'follow_up_usg_date', 'follow_up_usg', 'follow_up_other_test', 'follow_up_other_test_date',
           'follow_up_other_result', 'follow_up_treatment', 'follow_up_treatment_result', 'update_by', 'last_update']

col_new =  ['file_number', 'follow_up_period', 'follow_up_status', 'follow_up_mammography_date', 'follow_up_mammography',
           'follow_up_usg_date', 'follow_up_usg', 'follow_up_other_test', 'follow_up_other_test_date',
           'follow_up_other_result', 'follow_up_treatment', 'follow_up_treatment_result', 'update_by', 'last_update']

add_supp_table (table_old, conn_old, col_new, conn_new, table)


col_old_9 = ['File_number', 'Follow_up_Period', 'Follow_up_status', 'Follow_up_Mammography', 'Follow_up_USG', 'Follow_up_other_test',
       'Follow_up_other_result', 'update_by', 'last_update']

col_new =  ['file_number','follow_up_period', 'follow_up_status', 'follow_up_mammography', 'follow_up_usg',
            'follow_up_other_test', 'follow_up_other_result', 'update_by', 'last_update']

add_supp_table (table_old, conn_old, col_new, conn_new, table)

table = "hormonetherapy_survival"
table_old = "hormonetherapy_survival"
file_number_name = 'file_number'

file_list  = add_file_number (file_number_name, table_old, cursor_old, conn_new, cursor_new, table)

cols_set_old = ['hormone_indicated', 'hormone_recieved', 'hormone_date', 'hormone_type', 'hormone_duration_years',
                    'hormone_discontinued', 'hormone_ovary_surpression', 'hormone_therapy_outcome', 'hormone_followup',
                    'horomone_recurrence']

col_set_new =  ['hormone_indicated', 'hormone_recieved', 'hormone_date', 'hormone_type', 'hormone_duration_years',
                    'hormone_discontinued', 'hormone_ovary_surpression', 'hormone_therapy_outcome', 'hormone_followup',
                    'horomone_recurrence']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

cols_set_old = ['metastasis_exam', 'date_last_followup', 'time_to_recurrence', 'nature_of_recurrence',
                    'distant_site', 'patient_status_last_followup', 'update_by', 'last_update']

col_set_new =  ['metastasis_exam', 'date_last_followup', 'time_to_recurrence', 'nature_of_recurrence',
                    'distant_site', 'patient_status_last_followup', 'update_by', 'last_update']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)
conn_new.commit()
conn_new.close()
conn_old.close()

# get samples from excel sheet:
conn_new = sqlite3.connect(DB_list.new_db)
cursor_new = conn_new.cursor()
file_name_excel = DB_list.file_name

sheet = 'Patient_Information_History'

col_names_old = ['MR_number', 'Name', 'Aadhaar_Card', 'FirstVisit_Date', 'Permanent_Address', 'Current_Address',
                 'Phone', 'Email_ID', 'Gender', 'Age_at_First_Visit_yrs', 'Diagnosis_Age_yrs', 'Date_of_Birth',
                 'Place_Birth', 'Height_cm', 'Weight_kg', 'BMI']
col_names_new = ['mr_number', 'name', 'aadhaar_card', 'firstvisit_date', 'permanent_address', 'current_address',
                    'phone', 'email_id', 'gender', 'age_at_first_visit_yrs', 'diagnosis_age_yrs', 'date_of_birth',
                    'place_birth', 'height_cm', 'weight_kg', 'bmi']

update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_names_new, col_names_old)


sheet = 'Neo_Adjuvant_Therapy'
cols_set_old = ['NACT_status', 'Place_NACT', 'Details_NACT', 'Plan_NACT', 'Date_start_NACT',
                'Patient_weight_NACT', 'Drugs_Administered', 'Number_Cycles_NACT', 'Drugs_Frequency', 'Drugs_TotalDose',
                'Drugs_unit', 'Toxicity_Type', 'Toxicity_Grade', 'Toxicity_Treatment', 'Toxicity_Response',
                'Toxicity_at_Cycle', 'NACT_change_due_to_Toxicity', 'Tumour_Response_Check_Method',
                'Tumour_Response_NACT', 'Tumour_dimension_NACT', 'Tumour_size_unit_NACT', 'Date_tumour_size_checked',
                'NACT_completion_status', 'NACT_end_date', 'Trastuzumab_use_NACT', 'Trastuzumab_regime_NACT',
                'Trastuzumab_courses_taken_NACT', 'Hormone_therapy_NACT', 'Hormone_therapy_type_NACT',
                'Hormone_therapy_duration', 'Horomone_therapy_side_effects', 'update_by', 'last_update'
]
col_set_new =['nact_status', 'place_nact', 'details_nact', 'plan_nact', 'date_start_nact',
                    'patient_weight_nact', 'nact_drugs_administered', 'number_cycles_nact', 'cycle_weekly_frequency',
                    'drugs_totaldose', 'drugs_unit', 'toxicity_type', 'toxicity_grade', 'toxicity_treatment',
                    'toxicity_response', 'toxicity_at_cycle', 'nact_change_due_to_toxicity',
                    'tumour_response_check_method', 'tumour_response_nact', 'tumour_size', 'tumour_size_unit',
                    'date_tumour_size_checked', 'nact_completion_status', 'nact_end_date', 'trastuzumab_use_nact',
                    'trastuzumab_regime_nact', 'trastuzumab_courses_taken_nact', 'hormone_therapy_nact',
                    'hormone_therapy_type_nact', 'hormone_therapy_duration', 'horomone_therapy_side_effects',
              'update_by', 'last_update']

update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_set_new, cols_set_old)


sheet = 'Adjuvant_ChemoTherapy'

cols_set_old = ['Chemotherapy_status', 'Place_Chemotherapy', 'Details_Chemotherapy', 'Plan_Chemotherapy',
                'Date_start_Chemotherapy', 'Patient_weight_Chemotherapy', 'Drugs_Administered',
                'Number_Cycles_Chemotherapy', 'Frequency_Cycles_Chemotherapy', 'Drugs_TotalDose', 'Drugs_unit',
                'Toxicity_Type', 'Toxicity_Grade', 'Toxicity_Treatment', 'Toxicity_Response', 'Toxicity_at_Cycle',
                'Chemotherapy_change_due_to_Toxicity', 'Chemotherapy_completion_status', 'Chemotherapy_end_date',
                'Trastuzumab_use_Chemotherapy', 'Trastuzumab_regime_Chemotherapy',
                'Trastuzumab_courses_taken_Chemotherapy', 'Ovary_Status', 'Hormone_therapy_Chemotherapy',
                'Hormone_therapy_type_Chemotherapy', 'Hormone_therapy_duration_Chemotherapy',
                'Horomone_therapy_side_effects_Chemotherapy', 'update_by', 'last_update']

col_set_new = ['chemotherapy_status', 'place_chemotherapy', 'details_chemotherapy', 'plan_chemotherapy',
                'date_start_chemotherapy', 'patient_weight_chemotherapy', 'drugs_administered',
                'number_cycles_chemotherapy', 'cycle_weekly_frequency', 'drugs_totaldose', 'drugs_unit',
                'toxicity_type', 'toxicity_grade', 'toxicity_treatment', 'toxicity_response', 'toxicity_at_cycle',
                'chemotherapy_change_due_to_toxicity', 'chemotherapy_completion_status',
                'chemotherapy_end_date', 'trastuzumab_use_chemotherapy', 'trastuzumab_regime_chemotherapy',
                'trastuzumab_courses_taken_chemotherapy', 'ovary_status', 'hormone_therapy_chemotherapy',
                'hormone_therapy_type_chemotherapy', 'hormone_therapy_duration_chemotherapy',
                'horomone_therapy_side_effects_chemotherapy', 'update_by', 'last_update']

update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_set_new, cols_set_old)


sheet = 'Radiology'

cols_set_old = ['Mammography', 'Mammography_Date', 'Mammography_Place', 'Mammography_Indication', 'Mammography_Breast',
                'Mammography_MassNumber', 'Mammography_MassLocation', 'Mammography_MassShape', 'Mammography_MassMargin',
                'Mammography_MassNipple_cm', 'Mammography_MassSize', 'Mammography_MassSize_unit',
                'Mammography_CalcificationNumber', 'Mammography_CalcificationLocation', 'Mammography_CalcificationType',
                'Mammography_Skin_Lesion', 'Mammography_Birad', 'Mammography_Impression', 'Tomography_y_n',
                'Automated_Breast_Volume_Scanner_ABVS', 'Date_ABVS', 'Accession_ABVS', 'Lesion_ABVS',
                'Lesion_Location_ABVS', 'Size_ABVS', 'Distance_ABVS', 'Distance_PectMajor_ABVS', 'Diagnosis_ABVS',
                'SonoMammography', 'Sonomammo_Date', 'Sonomammo_Breast', 'Sonomammo_Mass', 'Sonomammo_Mass_Number',
                'Sonomammo_Mass_Location', 'Sonomammo_Mass_Clock', 'Sonomammo_Mass_Shape', 'Sonomammo_Mass_Margin',
                'Sonomammo_Mass_Echo', 'Sonomammo_Mass_Size', 'Sonomammo_Mass_Size_Unit', 'Sonomammo_Calc',
                'Sonomammo_Calc_Type', 'Sonomammo_Vascularity', 'Sonomammo_Birad', 'Sonomammo_Impression', 'update_by',
                'last_update', 'MRI', 'Date_MRI_Breast', 'AccessionNumber_MRI_Breast', 'MRI_Breast',
                'Fibroglandular_Tissue_MRI_Breast', 'Background_Paranchymal_Enhancement_Level_MRI_Breast',
                'Background_Paranchymal_Enhancement_Symmetry_MRI_Breast', 'Focus_MRI_Breast', 'Mass_MRI_Breast',
                'Number_Mass_MRI_Breast', 'Mass_Location_MRI_Breast', 'Mass_Shape_MRI_Breast', 'Mass_Margin_MRI_Breast',
                'Mass_Internal_Enhancement_Char_MRI_Breast', 'Asso_features_Nipple_retraction_MRI_Breast',
                'Asso_features_Nipple_invasion_MRI_Breast', 'Asso_features_Skin_retraction_MRI_Breast',
                'Asso_features_Skin_thickening_MRI_Breast', 'Asso_features_Axillary_adenopathy_MRI_Breast',
                'Asso_features_PectoralisMuscle_Invasion_MRI_Breast', 'Asso_features_ChestWall_Invasion_MRI_Breast',
                'Asso_features_Architectural_distortion_MRI_Breast', 'Asso_features_Skin_Invasion_MRI_Breast',
                'Fat_Lesion_MRI_Breast', 'Kinetics_Initial_MRI_Breast', 'Kinetics_Delayed_MRI_Breast',
                'Non_Enhanced_Features_MRI_Breast', 'Implant_MRI_Breast', 'Lesion_MRI_Breast',
                'Lesion_Location_MRI_Breast', 'Lesion_Depth_MRI_Breast', 'Lesion_Size_MRI_Breast',
                'DistancefromSkin_MRI_Breast', 'DistanceFromPectMaj_MRI_Breast', 'Category_BI_RADS_MRI_Breast',
                'user_name_mri', 'last_update_mri']

col_set_new =  ['mammography', 'mammography_date', 'mammography_place', 'mammography_indication',
                'mammography_breast', 'mammography_massnumber', 'mammography_masslocation', 'mammography_massshape',
                'mammography_massmargin', 'mammography_massnipple_cm', 'mammography_masssize',
                'mammography_masssize_unit', 'mammography_calcificationnumber', 'mammography_calcificationlocation',
                'mammography_calcificationtype', 'mammography_skin_involvement', 'mammography_birad', 'mammography_impression',
                'tomography_y_n', 'automated_breast_volume_scanner_abvs', 'date_abvs', 'accession_abvs', 'lesion_abvs',
                'lesion_location_abvs', 'size_abvs', 'distance_abvs', 'distance_pectmajor_abvs', 'diagnosis_abvs',
                'sonomammography_status', 'sonomammo_date', 'sonomammo_breast', 'sonomammo_mass',
                'sonomammo_mass_number', 'sonomammo_mass_location', 'sonomammo_mass_clock', 'sonomammo_mass_shape',
                'sonomammo_mass_margin', 'sonomammo_mass_echo', 'sonomammo_mass_size', 'sonomammo_mass_size_unit',
                'sonomammo_calc', 'sonomammo_calc_type', 'sonomammo_vascularity', 'sonomammo_birad',
                'sonomammo_impression', 'update_by', 'last_update', 'mri_status', 'date_mri', 'accession_number_mri',
                'mri_breast', 'fibroglandular_tissue_mri', 'background_paranchymal_enhancement_level_mri',
                'background_paranchymal_enhancement_symmetry_mri', 'focus_mri', 'mass_mri', 'number_mass_mri',
                'mass_location_mri', 'mass_shape_mri', 'mass_margin_mri', 'mass_internal_enhancement_char_mri',
                'asso_features_nipple_retraction_mri', 'asso_features_nipple_invasion_mri',
                'asso_features_skin_retraction_mri', 'asso_features_skin_thickening_mri',
                'asso_features_axillary_adenopathy_mri', 'asso_features_pectoralismuscle_invasion_mri',
                'asso_features_chestwall_invasion_mri', 'asso_features_architectural_distortion_mri',
                'asso_features_skin_invasion_mri', 'fat_lesion_mri', 'kinetics_initial_mri', 'kinetics_delayed_mri',
                'non_enhanced_features_mri', 'implant_mri', 'lesion_mri', 'lesion_location_mri', 'lesion_depth_mri',
                'lesion_size_mri', 'distancefromskin_mri', 'distancefrompectmaj_mri', 'mri_birad', 'user_name_mri',
                'last_update_mri']

update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_set_new, cols_set_old)


sheet = "RadiotherapyOptions"

cols_set_old = ['Radiation_received', 'Radiation_date', 'Radiation_type', 'IMRT_DCRT', 'Radiation_acute_toxicity',
                'Radiation_Delayed_Toxicity', 'Radiation_finish_date', 'Radiation_location', 'Radiation_Oncologist',
                'update_by', 'last_update']

col_set_new =  ['radiation_received', 'radiation_date', 'radiation_type', 'imrt_dcrt', 'radiation_acute_toxicity',
                'radiation_delayed_toxicity', 'radiation_finish_date', 'radiation_location', 'radiation_oncologist',
                'update_by', 'last_update']

add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table, cols_set_old, file_number_name,
                          col_set_new)

sheet = "Follow-up"

cols_set_old = ['File_number', 'Follow_up_Period', 'Follow_up_status', 'Follow_up_Mammography_Date',
                'Follow_up_Mammography', 'Follow_up_USG_Date', 'Follow_up_USG', 'Follow_up_other_test',
                'Follow_up_other_test_date', 'Follow_up_other_result']

col_set_new =  ['file_number', 'follow_up_period', 'follow_up_status', 'follow_up_mammography_date', 'follow_up_mammography',
           'follow_up_usg_date', 'follow_up_usg', 'follow_up_other_test', 'follow_up_other_test_date',
                'follow_up_other_result','update_by', 'last_update']

df_old = pd.read_excel(file_name_excel, sheet_name=sheet, index_col=0)
df_old = df_old.astype(str)
file_number_old = list(df_old.index)
table_name = Tables.sheet_name[sheet]
print(table_name)
sql_statement = 'SELECT file_number from ' + table_name
file_number = cursor_new.execute(sql_statement)
file_number_sql = file_number.fetchall()
file_list_sql = []
for file in file_number_sql:
    file_var = file[0]
    file_list_sql.append(file_var)
file_to_add = list(set(file_number_old) - set(file_list_sql))
print(file_to_add)
df_data = pd.read_excel(file_name_excel, sheet_name=sheet, index_col=False)
df_data.columns = col_set_new
table_name = 'follow_up_data'
for file in file_to_add:
     query_statement = "file_number == '" + file + "'"
     data_to_add = df_data.query(query_statement)
     data_to_add.to_sql(table_name, conn_new, index=False, if_exists='append')
     print(str(data_to_add.shape), 'added for file ' , file)

sheet = "HormoneTherapy_Survival"

cols_set_old = ['Hormone_Indicated', 'Hormone_Recieved', 'Hormone_Date', 'Hormone_Type', 'Hormone_duration_years',
                'Hormone_Discontinued', 'Hormone_Ovary_Surpression', 'Hormone_Therapy_Outcome', 'Hormone_followup',
                'Horomone_recurrence', 'Metastasis_exam', 'Date_last_followup', 'Time_to_recurrence',
                'Nature_of_recurrence', 'Distant_site', 'Patient_status_last_followup', 'update_by', 'last_update']

col_set_new =  ['hormone_indicated', 'hormone_recieved', 'hormone_date', 'hormone_type', 'hormone_duration_years',
                    'hormone_discontinued', 'hormone_ovary_surpression', 'hormone_therapy_outcome', 'hormone_followup',
                    'horomone_recurrence', 'metastasis_exam', 'date_last_followup', 'time_to_recurrence', 'nature_of_recurrence',
                    'distant_site', 'patient_status_last_followup', 'update_by', 'last_update']

update_from_excel (file_name_excel, sheet, conn_new, cursor_new, col_set_new, cols_set_old)

conn_new.commit()
conn_new.close()

#add specific files to a new db
file_list = FilesSubtype.tnbc
research = False
table_name = 'patient_information_history'
table_old = table_name
cols_set_old = get_col_list(table_name, research)[1:]
file_number_name = 'file_number'
col_set_new = cols_set_old
for file in file_list:
    sql.add_pk_fk_to_table(conn_new, cursor_new, col_name='file_number', pk=file, table=table_name)
add_old_data_to_new_table(cursor_old, conn_new, cursor_new, file_list, table_old, table_name, cols_set_old, file_number_name,
                          col_set_new)

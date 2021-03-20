import sqlite3
import sql.add_update_sql as sql
from datetime import datetime
import os
import helper_function.pccm_names as pccm_names
import helper_function.ask_y_n_statement as ask

class CreateTable:

    def __init__(self, cursor):
        self.cursor = cursor

    def create_table_pk(self, table, col_names, pk='pk'):
        print(table)
        print(col_names)
        if sql.table_check(self.cursor, table) == 0:
            self.cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, 
            nf=pk))
            [sql.add_columns(self.cursor, table, col) for col in col_names]
            print(table + ' created')
        else:
            print('Table already exists')

    def create_table(self, table, file_number, col_names):
        print(table)
        print(col_names)
        if sql.table_check(self.cursor, table) == 0:
            self.cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf='file_number'))
            [sql.add_columns(self.cursor, table, col) for col in col_names]
            print(table + ' created')
            # print('Table already exists')


class MakeTable:

    def __init__(self, db_folder, name):
        self.folder = db_folder
        self.db_name = name
        self.path = os.path.join(self.folder, self.db_name)
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()

    
    def makedb(self):
        db_create = CreateTable(self.cursor)
        file_number = "file_number"
        table = "patient_information_history"
        module_list = ["bio_info", "phys_act", "habits", "nut_supplements",
                       "family_details", "med_history", "cancer_history",
                       'family_cancer', 'det_by', "breast_symptoms",
                       'other_test']
        col_names = [pccm_names.names_info(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number=file_number, 
                               col_names=col_list)

        table = "biopsy_path_report"
        module_list = ["biopsy_report_info", "biopsy_details", 'ihc_biopsy_data', 'review_biopsy']
        col_names = [pccm_names.names_biopsy(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table_pk(table, col_list)

        table = 'surgery_path_report_data'
        module_list = ["surgery_block_information_0", "surgery_block_information_1", "surgery_block_information_2",
                       "surgery_block_information_3"]
        col_names = [pccm_names.names_surgery(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table_pk(table, col_list, pk='fk')

        table = "block_data"
        col_names = pccm_names.names_surgery('block_data')[1:]
        db_create.create_table_pk(table, col_names, pk='fk')

        table = "mammography"
        col_names = pccm_names.names_radio(table)
        db_create.create_table_pk(table, col_names)

        table = 'abvs'
        col_names = pccm_names.names_radio(table)
        db_create.create_table_pk(table, col_names)

        table = 'ultrasound'
        col_names = pccm_names.names_radio(table)
        db_create.create_table_pk(table, col_names)

        table = 'mri'
        col_names = pccm_names.names_radio(table)
        db_create.create_table_pk(table, col_names)

        table = 'pet_reports'
        module_list = ['pet_report_identifier', 'pet_report_findings', 'pet_breast_cancer']
        col_names = [pccm_names.names_pet(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table_pk(table, col_list)

        table = "surgery_report"
        module_list = ["surgery_information", "node_excision", "post_surgery"]
        col_names = [pccm_names.names_surgery_information(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "general_medical_history"
        col_names = ['condition', 'diagnosis_date', 'treatment']
        # col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "family_cancer_history"
        col_names = ['type_cancer', 'relation_to_patient', 'type_relation', 'age_at_detection_yrs']
        # col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "previous_cancer_history"
        col_names = ['type_cancer', 'year_diagnosis', 'surgery', 'type_surgery', 'duration_surgery', 'radiation',
                     'type_radiation','duration_radiation', 'chemotherapy','type_chemotherapy', 'duration_chemotherapy',
                     'hormone', 'type_hormone', 'duration_hormone', 'alternative', 'type_alternative', 'duration_alternative',
                     'homeremedy', 'type_homeremedy', 'duration_homeremedy']
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "nutritional_supplements"
        col_names = ['type_nutritional_supplements', 'quantity_nutritional_supplements_per_day',
                     'duration_nutritional_supplements']
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "physical_activity"
        col_names = ['type_activity', 'frequency_activity']
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "breast_feeding"
        col_names = ['child_number', 'feeding_duration', 'breast_usage_feeding']
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "nact_tox_table"
        col_names = pccm_names.names_nact(table)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "nact_drug_table"
        col_names = pccm_names.names_nact(table)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "neo_adjuvant_therapy"
        module_list = ["neo_adjuvant_therapy", "clip_information"]
        col_names = [pccm_names.names_nact(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = "adjuvant_chemotherapy"
        col_names = pccm_names.names_chemotherapy(table)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "chemo_tox_table"
        col_names = pccm_names.names_chemotherapy(table)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "chemo_drug_table"
        col_names = pccm_names.names_chemotherapy(table)
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "radiotherapy"
        col_names = pccm_names.names_radiation()
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "follow_up_data"
        col_names = pccm_names.name_follow_up()
        db_create.create_table(table, file_number='file_number', col_names=col_names)

        table = "hormonetherapy_survival"
        module_list = ["hormone", "metastasis"]
        col_names = [pccm_names.names_longterm(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number='file_number', col_names=col_list)

        table = 'block_list'
        col_names = pccm_names.block_list('all')
        db_create.create_table_pk(table, col_names=col_names, pk='pk')

        table = "clinical_exam"
        module_list = ['clinical_exam_initial', 'nipple_cytology']
        col_names = [pccm_names.name_clinical(module) for module in module_list]
        col_list = ask.flatten_nested_list(col_names)
        db_create.create_table(table, file_number=file_number, col_names=col_list)

        self.conn.commit()
        print(self.path + " file created")
        self.conn.close()


if __name__ == '__main__':
    folder = 'd:/repos/pccm_db/main/DB'
    db_name = 'PCCM_DB_' + datetime.now().strftime("%Y_%m_%d") + '.db'
    create_table = MakeTable(folder, db_name)
    create_table.makedb()

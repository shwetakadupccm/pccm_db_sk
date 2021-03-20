import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
from helper_function.pccm_names import names_pet as names
import pandas as pd
from helper_function.option_lists import PetReport, MultiTest
import uuid


class PetReportData:

    def __init__(self, conn, cursor, file_number, user_name):
        self.table_name = 'pet_reports'
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.module_list = ['pet_report_identifier', 'pet_report_findings', 'pet_breast_cancer']
        self.col_list_all = names(self.module_list[0]) + names(self.module_list[1]) + names(self.module_list[2])
        self.print_statements = ['\nPET report identifier\n',
                                 '\nPET report findings\n',
                                 '\nPET breast cancer details\n']

    def pet_report_identifier(self):
        module_name = self.module_list[0]
        check = False
        report_identifier = ['NA']*12
        while not check:
            pet_scan_date = ask.check_date('Please enter PET report date: ')
            pet_scan_number = input('Please enter PET scan number as given on the report: ')
            pet_scan_source = input('Please enter the facility at which PET scan was done: ')
            pet_scan_reg_number = input("Please enter PET report registration number: ")
            pet_scan_history = input('Please input patient history as given on report: ')
            pet_carcinoma_status = ask.ask_option('Please enter breast cancer status', MultiTest.carcinoma_status)
            pet_cancer_location = ask.ask_list('What is the location of the cancer', MultiTest.breast_cancer)
            pet_recurrence = ask.ask_y_n('Does the patient have a previously detected recurrence/mets?')
            if pet_recurrence:
                pet_recurrence_known = input('Please describe the recurrence/metastasis: ')
            else:
                pet_recurrence_known = 'no_known_recurrence_or_metastasis'
            pet_procedure_body_region = ask.ask_list("Region of body monitored by PET scan", PetReport.body_region)
            pet_procedure_fdg_dose_mci = ask.check_number_input("Please enter dose of 18F-FDG used in mCi. ",
                                                                "(Please enter only dose. If given in other units "
                                                                "enter under additional notes.): ")
            pet_procedure_bsl = input("Please enter basal sugar level with units as given: ")
            pet_scanner_name = ask.ask_list('Please enter name of scanner', PetReport.machine_name)
            pet_procedure_additional_notes = input('Please enter additional notes, if any for PET scan and patient '
                                                   'conditions: ')
            report_identifier = [self.file_number, pet_scan_date, pet_scan_number, pet_scan_source, pet_scan_reg_number,
                                 pet_scan_history, pet_carcinoma_status, pet_cancer_location, pet_recurrence_known,
                                 pet_procedure_body_region, pet_procedure_fdg_dose_mci, pet_procedure_bsl,
                                 pet_scanner_name, pet_procedure_additional_notes]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, report_identifier)
        return report_identifier

    def pet_report_findings(self):
        module_name = self.module_list[1]
        report_findings = ['NA', ] * 21
        report_list = []
        check = False
        while not check:
            pet_general_findings = input('Please enter general findings of PET scan: ')
            for region in PetReport.pet_regions:
                print('\n' + region.title() + ' Report\n')
                normal_report = input('Please enter normal features of ' + str(region) + ' region. Separate features by'
                                                                                         ' ";": ')
                abnormal = ask.ask_y_n('Are there any abnormal features in ' + str(region) + ' region?')
                if abnormal:
                    abnormal_report = input('Please enter abnormal features of ' + str(region) + 'region. Separate '
                                                                                                 'features by ";": ')
                else:
                    abnormal_report = 'no_abnormal_features'
                report_list = report_list + [normal_report, abnormal_report]
            pet_head_neck_normal_report, pet_head_neck_abnormal_report, pet_thorax_normal_report, \
            pet_thorax_abnormal_report, pet_abdomen_pelvis_normal_report, pet_abodmen_pelvis_abnormal_report, \
            pet_musculoskeletal_normal_report, pet_musculoskeletal_abnormal_report = report_list
            pet_impression = input('Please enter PET impressions statements: ')
            pet_primary_disease = ask.ask_y_n('Does the report describe a primary untreated breast cancer?',
                                              yes_ans='primary_disease', no_ans='not_primary_disease')
            pet_local_spread = ask.ask_y_n_na('Does the report describe local/regional spread of the disease?',
                                              yes_ans='local_spread_present', no_ans='no_local_spread',
                                              na_ans='local_spread_resolved')
            pet_recurrence = ask.ask_y_n_na('Does the report describe recurrence of the disease?',
                                            yes_ans='recurrence_present', no_ans='no_recurrence_present',
                                            na_ans='possible_recurrence')
            pet_distant_metastasis = ask.ask_y_n_na('Does the report describe distant metastasis of the disease?',
                                                    yes_ans='metastasis', no_ans='no_metastasis',
                                                    na_ans='possible_metastasis')
            report_findings = [pet_general_findings, pet_head_neck_normal_report, pet_head_neck_abnormal_report,
                               pet_thorax_normal_report, pet_thorax_abnormal_report, pet_abdomen_pelvis_normal_report,
                               pet_abodmen_pelvis_abnormal_report, pet_musculoskeletal_normal_report,
                               pet_musculoskeletal_abnormal_report, pet_impression, pet_primary_disease,
                               pet_local_spread, pet_recurrence, pet_distant_metastasis]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, report_findings)
        return report_findings


    def pet_breast_cancer(self):
        module_name = self.module_list[2]
        breast_report = ['NA', ] * 7
        check = False
        while not check:
            pet_breast = ask.ask_y_n('Does this report describe a breast cancer?')
            if pet_breast:
                print('\nPlease describe primary breast lesion\n')
                pet_breast_lesion_size = input('Dimensions of breast lesion/s: ')
                pet_breast_lesion_size_unit = ask.ask_list('Unit of breast lesion size', ['mm', 'cm'])
                pet_breast_lesion_suv = ask.check_number_input('Please enter SUV max of breast lesion: ',
                                                               'Please enter only SUV not description')
                pet_breast_lesion_location = input('Please enter description of lesion location: ')
                pet_breast_lesion_type = input('Please input description of lesion: ')
                pet_breast_lesion_comments = input('Please input any additional notes for breast lesion: ')
                pet_breast_nodes = ask.ask_y_n('Does the report describe breast related nodes?')
                if pet_breast_nodes:
                    pet_breast_nodes_description = input('Please enter nodes description as given: ')
                else:
                    pet_breast_nodes_description = 'nodes_not_described'
                pet_breast_skin = ask.ask_y_n('Does the PET report describe any skin changes?')
                if pet_breast_skin:
                    pet_breast_lesion_skin = input('Please enter description of skin changes: ')
                else:
                    pet_breast_lesion_skin = 'skin_changes_not_described'
            else:
                pet_breast_lesion_size, pet_breast_lesion_size_unit, pet_breast_lesion_suv, pet_breast_lesion_location,\
                pet_breast_lesion_type, pet_breast_lesion_comments, pet_breast_nodes_description, \
                pet_breast_lesion_skin = ['no_breast_cancer', ] * 8
            breast_report = [pet_breast_lesion_size, pet_breast_lesion_size_unit, pet_breast_lesion_suv,
                             pet_breast_lesion_location, pet_breast_lesion_type, pet_breast_lesion_comments,
                             pet_breast_nodes_description, pet_breast_lesion_skin]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list[:-2], breast_report)
        data_list = breast_report + [self.user_name, sql.last_update()]
        return data_list

    def add_data(self):
        pk = uuid.uuid4().hex
        sql.add_pk_fk_to_table(self.conn, self.cursor, self.table_name, col_name='pk', pk=pk)
        pet_present = ask.ask_y_n("Does the patient file contain a PET/CT report to be entered?")
        if not pet_present:
            data_length = len(self.col_list_all) - 3
            data = [self.file_number] + ['pet_report_not_present'] * data_length + [self.user_name, sql.last_update()]
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, self.col_list_all, key_name='pk', key_value=pk,
                                    data=data)
        else:
            print(self.print_statements[0])
            col_list = names(self.module_list[0])
            enter = ask.ask_y_n("Enter " + self.print_statements[0])
            if enter:
                data = self.pet_report_identifier()
                sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                        data=data)
            col_list = names(self.module_list[1])
            enter = ask.ask_y_n("Enter " + self.print_statements[1])
            if enter:
                data = self.pet_report_findings()
                sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                        data=data)
            enter = ask.ask_y_n("Enter " + self.print_statements[2])
            col_list = names(self.module_list[2])
            if enter:
                data = self.pet_breast_cancer()
                sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                        data=data)

    def edit_data(self):
        enter = sql.view_multiple(self.conn, self.table_name, self.col_list_all, self.file_number)
        if enter == "Add data":
            self.add_data()
        elif enter == "Edit data":
            col_list_all = self.col_list_all
            sql_statement = ('SELECT ' + ", ".join(col_list_all) + " FROM '" + self.table_name +
                             "' WHERE file_number = '" + self.file_number + "'")
            df = pd.read_sql(sql_statement, self.conn)
            sql.print_df(df)
            pk, value_row_to_edit = sql.retrieve_with_pk_to_edit(df, value_col='pet_scan_date', table=self.table_name,
                                                                 cursor=self.cursor, pk=False)
            print('value_row_to_edit: ', value_row_to_edit)
            if not value_row_to_edit:
                sql.delete_rows(self.cursor, self.table_name, col_name="file_number", col_data=self.file_number)
                self.add_data()
            else:
                print('edit_data_pk')
                self.edit_data_pk(pk, value_row_to_edit)
        else:
            print('\n No edits will be made to this t able\n')

    def edit_data_pk(self, pk, value_row_to_edit):
        print(self.print_statements[0])
        col_list = names(self.module_list[0])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=pk,
                                    columns=col_list, col_name='pet_scan_date', col_value=value_row_to_edit)
        if enter:
            data = self.pet_report_identifier()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                    data=data)
        print(self.print_statements[1])
        col_list = names(self.module_list[1])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=pk,
                                    columns=col_list, col_name='pet_scan_date', col_value=value_row_to_edit)
        if enter:
            data = self.pet_report_findings()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                    data=data)
        print(self.print_statements[2])
        col_list = names(self.module_list[2])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=pk,
                                    columns=col_list, col_name='pet_scan_date', col_value=value_row_to_edit)
        if enter:
            data = self.pet_breast_cancer()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=pk,
                                    data=data)
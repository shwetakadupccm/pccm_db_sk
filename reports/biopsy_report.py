import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
import helper_function.pccm_names as names
from reports.block_information import BlockInformation
from additional_tables.block_description import BlockDescription, breast_cancer_subtype
from helper_function.option_lists import PathReports
import helper_function.ask_y_n_statement as ask
 

class BiopsyData:
    def __init__(self, conn, cursor, file_number, pk, block_id, number_of_blocks, user_name):
        self.table_name = names.ffpe_db_tables()[1]
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.block_type = 'biopsy'
        self.pk = pk
        self.biopsy_block_id, self.biopsy_number_of_blocks = block_id, number_of_blocks

    def biopsy_report_info(self):
        module = 'biopsy_report_info'
        col_list = names.names_biopsy(module)
        check = False
        data_list = [self.file_number] + (['To be done'] * 18)
        while not check:
            block_list_table = BlockInformation(self.conn, self.cursor, self.file_number)
            block_data = ['block_sr_number', 'block_location', 'current_block_location', 'blocks_received_at_pccm',
                          'block_series']
            block_sr_number, block_location, current_block_location, blocks_received_at_pccm, biopsy_block_series = \
                block_list_table.get_block_information(block_id=self.biopsy_block_id, block_data=block_data)
            fnac = ask.ask_list('FNAC done for breast lesion?', ['fnac_breast_yes', 'fnac_breast_no'])
            if fnac == 'fnac_breast_no':
                fnac_breast, fnac_breast_date, fnac_slide_id, fnac_diagnosis, fnac_diagnosis_comments = (fnac,) * 5
            else:
                fnac_breast = ask.ask_list('FNAC location', ['left_breast', 'right_breast',
                                                             'requires_specialist_input'])
                fnac_breast_date = ask.check_date('Date of FNAC test: ')
                fnac_slide_id = input('Enter FNAC slide ID: ')
                fnac_diagnosis = input('Enter diagnosis for FNAC breast as given in report: ')
                fnac_diagnosis_comments = input('Enter additional comments for FNAC diagnosis: ')
            biopsy_date = ask.check_date('Date of Biopsy: ')
            reason_path_report = ask.ask_list('Reason for pathology report', ['diagnosis', 'bilateral_diagnosis',
                                                                              'review_biopsy', 'nact_follow up',
                                                                              'recurrence_diagnosis',
                                                                              'revision_surgery',
                                                                              'requires_specialist_input'])
            biopsy_site = ask.ask_list('Biopsy_site', ['left_breast', 'right_breast', 'left_axilla', 'right_axilla',
                                                       'requires_specialist_input'])
            biopsy_report_pccm = ask.ask_list("Is the biopsy report available?", ["biopsy_report_pccm_yes",
                                                                                  "biopsy_report_pccm_no",
                                                                                  'doctors_notes_available',
                                                                                  'path_history_notes',
                                                                                  'requires_specialist_input'])
            if biopsy_report_pccm != 'biopsy_report_pccm_no':
                biopsy_block_source = ask.ask_option('Source of Biopsy Block', PathReports.path_labs)
                biopsy_lab_id = input("Biopsy Lab ID/SID: ")
            else:
                biopsy_block_source, biopsy_lab_id = ('NAv',)*2
            biopsy_ihc_report_pccm = ask.ask_list("Is the IHC report available?", ["biopsy_ihc_report_pccm_yes",
                                                                                   "biopsy_ihc_report_pccm_no",
                                                                                   'doctors_notes_available',
                                                                                   'path_history_notes_available',
                                                                                   'requires_specialist_input'])
            data_list = [self.file_number, block_sr_number, block_location, current_block_location,
                         blocks_received_at_pccm, fnac_breast, fnac_breast_date, fnac_slide_id, fnac_diagnosis,
                         fnac_diagnosis_comments, reason_path_report, biopsy_site, biopsy_report_pccm,
                         biopsy_ihc_report_pccm, self.biopsy_block_id, self.biopsy_number_of_blocks, biopsy_block_series,
                         biopsy_date, biopsy_block_source, biopsy_lab_id]
            print(data_list)
            check = sql.review_input(self.file_number, col_list, data_list)
        data = data_list
        return data

    def ihc_biopsy_data(self):
        col_list = names.names_biopsy('ihc_biopsy_data')
        try:
            columns = names.names_biopsy('biopsy_report_info')
            biopsy_ihc_report_pccm = sql.extract_select_column_key(conn=self.conn, columns=columns,
                                                                   table=self.table_name, key_name='pk',
                                                                   key_value=self.pk,
                                                                   col_select='biopsy_ihc_report_pccm')
        except ValueError:
            biopsy_ihc_report_pccm = ask.ask_list("Is the biopsy IHC report available?", ["biopsy_ihc_report_pccm_yes",
                                                                                          "biopsy_ihc_report_pccm_no",
                                                                                          'doctors_notes_available',
                                                                                          'path_history_notes_'
                                                                                          'available',
                                                                                          'requires_specialist_input'])
        data_list = ['NAv'] * 11
        try:
            columns = names.names_biopsy('biopsy_details')
            benign = sql.extract_select_column_key(conn=self.conn, columns=columns, table=self.table_name,
                                                   key_name='pk', key_value=self.pk, col_select='benign')
            # print('Diagnosis is :', benign)
            if benign.lower() == 'false':
                benign = False
            elif benign.lower() == 'true':
                benign = True
            else:
                benign = ask.ask_y_n("Is the diagnosis for this block benign?")
        except ValueError:
            benign = ask.ask_y_n("Is the diagnosis for this block benign?")
        check = False
        while not check:
            if benign:
                # print(str(benign))
                print('Diagnosis is benign so IHC has not been considered')
                biopsy_er, biopsy_er_percent, biopsy_pr, biopsy_pr_percent, biopsy_her2, biopsy_her2_grade, biopsy_fish,\
                biopsy_ki67, biopsy_subtype = ['NA'] * 9
            else:
                print('biopsy_ihc_report_pccm: ' + biopsy_ihc_report_pccm)
                if biopsy_ihc_report_pccm[0] != 'biopsy_ihc_report_pccm_no':
                    print('Please input all data for ' + self.biopsy_block_id + ' block only')
                    biopsy_er, biopsy_er_percent, biopsy_pr, biopsy_pr_percent, biopsy_her2, biopsy_her2_grade, \
                    biopsy_fish, biopsy_ki67 = BlockDescription.ihc_report('biopsy')
                else:
                    biopsy_er, biopsy_er_percent, biopsy_pr, biopsy_pr_percent, biopsy_her2, biopsy_her2_grade, \
                    biopsy_fish, biopsy_ki67 = ['NAv'] * 8
                biopsy_subtype = breast_cancer_subtype('biopsy', biopsy_er, biopsy_pr, biopsy_her2,
                                                       biopsy_her2_grade, biopsy_fish)
            fnac_lymph_node = ask.ask_list("Lymph Node FNAC", ask.create_yes_no_options('Lymph Node FNAC'))
            fnac_lymph_node_location, fnac_lymph_node_diagnosis = (fnac_lymph_node,) * 2
            if fnac_lymph_node == "lymph_node_fnac_yes":
                fnac_lymph_node_location = input("Please enter lymph node biopsy location: ")
                fnac_lymph_node_diagnosis = ask.ask_list("Lymph Node FNAC diagnosis",
                                                         ask.create_yes_no_options('Lymph Node FNAC '
                                                                                   'diagnosis',
                                                                                   yes='malignant',
                                                                                   no='non_malignant'))
            data_list = [biopsy_er, biopsy_er_percent, biopsy_pr, biopsy_pr_percent, biopsy_her2,
                         biopsy_her2_grade, biopsy_fish, biopsy_ki67, biopsy_subtype, fnac_lymph_node,
                         fnac_lymph_node_location, fnac_lymph_node_diagnosis]
            check = sql.review_input(self.file_number, col_list[:-2], data_list)
        data = data_list + [self.user_name, sql.last_update()]
        return data

    def biopsy_details(self):
        col_list = names.names_biopsy('biopsy_details')
        try:
            columns = names.names_biopsy('biopsy_report_info')
            biopsy_report_pccm = sql.extract_select_column_key(conn=self.conn, columns=columns, table=self.table_name,
                                                               key_name='pk', key_value=self.pk,
                                                               col_select='biopsy_report_pccm')
        except ValueError:
            biopsy_report_pccm = ask.ask_list("Is the biopsy report available?", ["biopsy_report_pccm_yes",
                                                                                  "biopsy_report_pccm_no",
                                                                                  'doctors_notes_available',
                                                                                  'path_history_notes',
                                                                                  'requires_specialist_input'])
        data_list = ['NAv'] * 3 + ['False'] + ['NAv'] * 3
        if biopsy_report_pccm != 'biopsy_report_pccm_no':
            check = False
            while not check:
                print('Please input all data for ' + self.biopsy_block_id + ' report only')
                biopsy_type = ask.ask_list("Biopsy Type", PathReports.biopsy_type)
                biopsy_diagnosis = ask.ask_list("Biopsy Diagnosis: ", PathReports.diagnosis)
                biopsy_comments = input('Enter any additional comments on the diagnosis: ')
                benign = ask.ask_y_n('Is the diagnosis of ' + str(biopsy_diagnosis) + ' describing a benign condition ('
                                                                                      'If diagnosis is not available '
                                                                                      'enter NO here)')
                if benign:
                    biopsy_tumour_grade,  biopsy_lymph_emboli, dcis_biopsy = ['benign condition'] * 3
                else:
                    biopsy_tumour_grade = ask.ask_option("Tumour Biopsy Grade", PathReports.grade)
                    biopsy_lymph_emboli = ask.ask_list("Are Lymphovascular emboli seen?", ask.create_yes_no_options(
                        'Lymphovascular emboli Biopsy', not_cancer='requires_follow_up'))
                    dcis_biopsy = ask.ask_list("Does the biopsy show DCIS",
                                               ask.create_yes_no_options('dcis biopsy', not_cancer='requires_follow_up'
                                                                         ))

                data_list = [biopsy_type, biopsy_diagnosis, biopsy_comments, str(benign), biopsy_tumour_grade,
                             biopsy_lymph_emboli, dcis_biopsy]
                check = sql.review_input(self.file_number, col_list, data_list)
        else:
            print('\nBiopsy report is not available. Data for biopsy_type, biopsy_diagnosis, biopsy_comments, '
                  'tumour_grade, lymph_emboli, dcis_biopsy has been entered as NAv\n')
        return data_list

    def review_biopsy(self):
        review_biopsy_date, review_biopsy_source, review_biopsy_diagnosis, review_biopsy_diagnosis_comment, \
        review_biopsy_block_id, review_biopsy_er, review_biopsy_er_percent, review_biopsy_pr, review_biopsy_pr_percent, \
        review_biopsy_her2, review_biopsy_her2_grade, review_biopsy_fish, review_biopsy_ki67 = ['NA', ] * 13
        data_list = ['NA', ] * 13
        check = False
        while not check:
            review = ask.ask_y_n('Has a review (of diagnosis or IHC details) been done of this biopsy block?')
            if review:
                review_biopsy_date = ask.check_date('Date of review biopsy (if multiple dates?): ')
                review_biopsy_source = input('Name of Review Biopsy Laboratory (Enter multiple if required Lab_test): ')
                review_biopsy_diagnosis = input('Enter diagnosis of review biopsy: ')
                review_biopsy_diagnosis_comment = input('Additional comments for biopsy review diagnosis: ')
                review_biopsy_block_id = self.biopsy_block_id
                block_id = ask.ask_y_n('Has the block been relabelled in the review biopsy?')
                if block_id:
                    old_block_id = input('Please enter old block id: ')
                    new_block_id = input('Please enter new block id: ')
                    review_biopsy_block_id = old_block_id + ' relabelled to ' + new_block_id
                review_ihc = ask.ask_y_n('Has the IHC result for any marker been reviewed by another lab?')
                if review_ihc:
                    review_biopsy_er, review_biopsy_er_percent, review_biopsy_pr, review_biopsy_pr_percent, \
                    review_biopsy_her2, review_biopsy_her2_grade, review_biopsy_fish, review_biopsy_ki67  = \
                        BlockDescription.ihc_report('review_biopsy')
            data_list = [review_biopsy_date, review_biopsy_source, review_biopsy_diagnosis,
                         review_biopsy_diagnosis_comment, review_biopsy_block_id, review_biopsy_er,
                         review_biopsy_er_percent, review_biopsy_pr, review_biopsy_pr_percent, review_biopsy_her2,
                         review_biopsy_her2_grade, review_biopsy_fish, review_biopsy_ki67]
            col_list = names.names_biopsy('review_biopsy')
            check = sql.review_input(self.file_number, col_list[:-2], data_list)
        data = data_list + [self.user_name, sql.last_update()]
        return data

    def add_data(self):
        block_list_table = BlockInformation(self.conn, self.cursor, self.file_number)
        enter = ask.ask_y_n("Enter Biopsy Report information?")
        if enter:
            data = self.biopsy_report_info()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, names.names_biopsy("biopsy_report_info"),
                                    key_name='pk', key_value=self.pk, data=data)
        enter = ask.ask_y_n("Enter Biopsy data?")
        if enter:
            data = self.biopsy_details()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, names.names_biopsy("biopsy_details"),
                                    key_name='pk', key_value=self.pk, data=data)
            data = self.ihc_biopsy_data()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, names.names_biopsy("ihc_biopsy_data"),
                                    key_name='pk', key_value=self.pk, data=data)
            data = self.review_biopsy()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, names.names_biopsy("review_biopsy"),
                                    key_name='pk', key_value=self.pk, data=data)
            is_surgery = ask.ask_y_n('Is a surgery associated with this biopsy?')
            if is_surgery:
                surgery_block_id, surgery_number_of_blocks = block_list_table.get_block_id('surgery')
            else:
                surgery_block_id = 'NA'
            sql.update_single_key(self.conn, self.cursor, self.table_name, 'surgery_block_id', key_name='pk',
                                  key_value=self.pk, var=surgery_block_id)

    def edit_data(self):
        print("Block Report information")
        col_list = names.names_biopsy("biopsy_report_info")
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=self.pk,
                                    columns=col_list, col_name='biopsy_block_id', col_value=self.biopsy_block_id)
        if enter:
            # sql.add_pk_fk_to_table(self.conn, self.cursor, self.table_name, col_filter='pk', pk=self.pk)
            data = self.biopsy_report_info()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=self.pk,
                                    data=data)
        print("Biopsy Tumour data")
        col_list = names.names_biopsy("biopsy_details")
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=self.pk,
                                    columns=col_list, col_name='biopsy_block_id', col_value=self.biopsy_block_id)
        if enter:
            data = self.biopsy_details()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=self.pk,
                                    data=data)
        print("Biopsy IHC data")
        col_list = names.names_biopsy("ihc_biopsy_data")
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=self.pk,
                                    columns=col_list, col_name='biopsy_block_id', col_value=self.biopsy_block_id)
        if enter:
            data = self.ihc_biopsy_data()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=self.pk,
                                    data=data)
        print('Review Biopsy data')
        col_list = names.names_biopsy("review_biopsy")
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='pk', key_value=self.pk,
                                    columns=col_list, col_name='biopsy_block_id', col_value=self.biopsy_block_id)
        if enter:
            data = self.review_biopsy()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='pk', key_value=self.pk,
                                    data=data)
        surgery_block_id = sql.get_value(col_name='surgery_block_id', table=self.table_name, pk=self.pk, pk_name='pk',
                                         cursor=self.cursor, error_statement='Please enter surgery block id associated '
                                                                             'with this biopsy entry: ')
        print('Surgery block id associated with this biopsy is ' + str(surgery_block_id))
        block = ask.ask_y_n('Is this block id correct?')
        if not block:
            surgery_block_id = input('Please enter surgery block id associated with this biopsy entry: ')
            sql.update_single_key(self.conn, self.cursor, self.table_name, 'surgery_block_id', key_name='pk',
                                  key_value=self.pk, var=surgery_block_id)

import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
from helper_function.pccm_names import names_surgery as names
from additional_tables.block_description import BlockDescription, breast_cancer_subtype
from reports.block_information import BlockInformation
import pandas as pd
from helper_function.option_lists import PathReports

class SurgeryBlockData:

    def __init__(self, conn, cursor, file_number, fk, block_id, number_of_blocks, user_name):
        self.table_name = 'surgery_path_report_data'
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.fk = fk
        self.module_list = ['surgery_block_information_0', 'surgery_block_information_1', 'surgery_block_information_2',
                            'surgery_block_information_3']
        self.block_type = 'surgery'
        self.surgery_block_id, self.surgery_number_of_blocks = block_id, number_of_blocks
        self.print_statements = ['\nSurgery Block Report information\n',
                                 '\nSurgery Block information (Tumour Details)\n',
                                 '\nSurgery Block information (IHC and Node Details)\n',
                                 '\nSurgery Block Review Information\n']

    def surgery_block_information_0(self):
        module_name = self.module_list[0]
        check = False
        data_list = ['NA']*17
        surgery_block_data_type = 'primary'
        while not check:
            data_type = ask.ask_y_n("Is surgery type: '" + surgery_block_data_type + "'")
            if not data_type:
                surgery_block_data_type = ask.ask_option("Type of surgery", ['revision', 'recurrence'])
            block_list_table = BlockInformation(self.conn, self.cursor, self.file_number)
            block_data = ['block_sr_number', 'block_location', 'current_block_location', 'block_series']
            block_sr_number, block_location, current_block_location, surgery_block_series = \
                block_list_table.get_block_information(self.surgery_block_id, block_data)
            surgery_block_source = ask.ask_option("Pathology Lab (source of block)", PathReports.path_labs)
            breast_cancer_yes_no = ask.ask_y_n('Is this a case of breast cancer (Unilateral OR Bilateral)',
                                               yes_ans="breast_cancer_yes", no_ans="breast_cancer_no")
            pathology_report_available_yes_no = ask.ask_y_n('Is the pathology report available', yes_ans="yes",
                                                            no_ans="no")
            nat = ask.ask_y_n('Has Neo-Adjuvant therapy been administered to the patient (NACT or NAHT)?')
            if nat:
                nact = ask.ask_list('What type of therapy has been givent to the patient?',
                                    ['NACT', 'NAHT', 'NACT_and_NAHT'])
                neoadjuvant_therapy = nact.lower() + '_yes'
                surgery_block_primary_tissue = 'treated_tissue'
            else:
                neoadjuvant_therapy = 'nact_no'
                surgery_block_primary_tissue = 'primary_tissue'
            date_of_surgery = ask.check_date("Date of Surgery: ")
            surgeon_s = ask.ask_option("Name of the Surgeon/s", PathReports.surgeon)
            surgery_hospital_id = input("Hospital ID: ")
            surgery_lesion_site = ask.ask_list("Lesion on", ["right_breast", "left_breast", "bilateral"])
            surgery_type = self.bilateral_treatment(surgery_lesion_site, 'Type of surgery', PathReports.surgery_type)
            data_list = [self.file_number, surgery_block_data_type, block_sr_number, block_location,
                         current_block_location, self.surgery_block_id, self.surgery_number_of_blocks,
                         surgery_block_series, breast_cancer_yes_no, pathology_report_available_yes_no,
                         neoadjuvant_therapy, str(surgery_block_primary_tissue).lower(), surgery_block_source,
                         date_of_surgery, surgeon_s, surgery_hospital_id, surgery_lesion_site, surgery_type]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return data_list

    @property
    def surgery_block_information_1(self):
        module_name = self.module_list[1]
        data_list = ['NA', ] * 21
        block_desc_df = pd.DataFrame()
        check = False
        while not check:
            blocks = BlockDescription(fk=self.fk, file_number=self.file_number, block_id=self.surgery_block_id,
                                      block_no=self.surgery_number_of_blocks, user_name=self.user_name)
            block_desc_df, block_descriptions_all = blocks.block_description()
            breast_cancer_yes_no = sql.get_value_no_error(col_name='breast_cancer_yes_no', table=self.table_name,
                                                 pk=self.fk, cursor=self.cursor, pk_name='fk')
            if not breast_cancer_yes_no:
                breast_cancer_yes_no = ask.ask_y_n('Is this a case of breast cancer (Unilateral OR Bilateral)',
                                               yes_ans="breast_cancer_yes", no_ans="breast_cancer_no")
            surgery_lesion_site = sql.get_value_no_error(col_name='surgery_lesion_site', table=self.table_name,
                                                pk=self.file_number, cursor=self.cursor, pk_name='file_number')
            if not surgery_lesion_site:
                surgery_lesion_site = ask.ask_list("Lesion on", ["right_breast", "left_breast", "bilateral"])
            block_info = BlockInformation(self.conn, self.cursor, self.file_number)
            specimen_resection_size, margin_size, cut_margin_size, margin_report = block_info.margin_info()
            tumour_size, tumour_size_unit, tumour_grade, surgery_diagnosis, surgery_diagnosis_comments, dcis_yes_no, \
            dcis_percent, surgery_perineural_invasion, surgery_necrosis, surgery_lymphovascular_invasion, \
            percent_lymph_invasion, stromal_tils_percent, tumour_desmoplastic_response = [breast_cancer_yes_no, ] * 13
            print('breast_cancer_yes_no: ' + breast_cancer_yes_no)
            check_answer = ask.ask_y_n('Is this correct?')
            while not check_answer:
                breast_cancer_yes_no = ask.ask_y_n('Is this a case of breast cancer (Unilateral OR Bilateral)',
                                                   yes_ans="breast_cancer_yes", no_ans="breast_cancer_no")
                check_answer = ask.ask_y_n('Is this correct?')
            if breast_cancer_yes_no == 'breast_cancer_yes':
                tumour_size = input("Tumour size (please input dimension only, e.g, 1 x 3 x 4): ")
                tumour_size_unit = ask.ask_list("Tumour size unit", ['mm', 'cm'])
                tumour_grade = ask.ask_option("Tumour Grade", ["I", "II", "III"])
                surgery_diagnosis = self.bilateral_treatment(surgery_lesion_site, "Surgery Diagnosis: ",
                                                             PathReports.diagnosis)
                surgery_diagnosis_comments = self.bilateral_treatment(surgery_lesion_site, 'Descriptive or indicative '
                                                                                           'notes for surgery '
                                                                                           'diagnosis: ', 'input')
                dcis_yes_no = self.bilateral_treatment(surgery_lesion_site, 'DCIS', ask.create_yes_no_options('DCIS'))
                dcis_percent = dcis_yes_no
                if 'dcis_yes' in dcis_yes_no:
                    dcis_percent = self.bilateral_treatment(surgery_lesion_site, "Percent DCIS (number only if given "
                                                                                 "else NA): ", 'input')
                surgery_perineural_invasion = self.bilateral_treatment(surgery_lesion_site, "Perineural Invasion: ",
                                                                       ask.create_yes_no_options('Perineural Invasion',
                                                                                                  yes='yes', no='no'))
                surgery_necrosis = self.bilateral_treatment(surgery_lesion_site, "Necrosis", ask.create_yes_no_options(
                    'Necrosis'))
                surgery_lymphovascular_invasion = self.bilateral_treatment(surgery_lesion_site,
                                                                           "Lymphovascular Invasion: ",
                                                                           ask.create_yes_no_options
                                                                           ('Lymphovascular Invasion'))
                percent_lymph_invasion = self.bilateral_treatment(surgery_lesion_site, "Percent Lymphocyte Invasion "
                                                                                       "Enter number only; Enter "
                                                                                       "'data_not_in_report' "
                                                                                       "if not available: ", 'input')
                stromal_tils_percent = self.bilateral_treatment(surgery_lesion_site, 'Stromal Tumor infiltrating '
                                                                                     'lymphocytes: ', 'input')
                tumour_desmoplastic_response = self.bilateral_treatment(surgery_lesion_site,
                                                                        "Tumor desmoplastic response: ",
                                                                        ask.create_yes_no_options
                                                                        ('Tumor desmoplastic response'))

            tumour_block_ref, node_block_ref, ad_normal_block_ref, red_tissue_block_ref \
                = ask.join_lists(block_descriptions_all, sep="; ")
            data_list = [specimen_resection_size, tumour_block_ref, margin_size, cut_margin_size, margin_report,
                        node_block_ref, ad_normal_block_ref, red_tissue_block_ref, tumour_size, tumour_size_unit,
                        tumour_grade, surgery_diagnosis, surgery_diagnosis_comments, dcis_yes_no, dcis_percent,
                        surgery_perineural_invasion, surgery_necrosis, surgery_lymphovascular_invasion,
                         percent_lymph_invasion, stromal_tils_percent, tumour_desmoplastic_response]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return tuple(data_list), block_desc_df

    def surgery_block_information_2(self):
        module_name = self.module_list[2]
        data_list = ['NA', ] * 18
        check = False
        while not check:
            ihc_report = BlockDescription.ihc_report(ihc_type='Tumour_surgery_block')
            surgery_er, surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2, surgery_her2_grade, \
            surgery_fish, surgery_ki67 = ihc_report
            surgery_subtype = breast_cancer_subtype('surgery', surgery_er, surgery_pr, surgery_her2,
                                                   surgery_her2_grade, surgery_fish)
            node_details = self.node_details()
            sentinel_node_number_removed, sentinel_node_number_positive, axillary_node_number_removed, \
            axillary_node_number_positive, apical_node_number_removed, apical_node_number_positive = node_details
            surgery_perinodal_spread = ask.ask_list('Perinodal Spread',
                                                    ask.create_yes_no_options
                                                    ('Perinodal Spread', not_cancer='requires_follow_up'))
            pathological_pt = input('Pathological T Status (Enter T0/T1/T2 etc as given in report): ')
            pathological_pn = input('Pathological N Status (Enter N0/N1/N2 etc as given in report): ')
            metastasis = ask.ask_y_n('Did the patient have metastasis at diagnosis?')
            nat = sql.get_value(col_name='neoadjuvant_therapy', table=self.table_name, pk=self.fk, cursor=self.cursor,
                                pk_name='fk', error_statement='what is the nact status?')
            if nat != 'nact_no':
                prefix = 'yp'
            else:
                prefix = 'p'
            pathological_stage, clinical_stage = BlockDescription.stage(pathological_pt, pathological_pn, metastasis,
                                                                        prefix)
            data_list = [surgery_er, surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2,
                         surgery_her2_grade, surgery_fish, surgery_ki67, surgery_subtype, sentinel_node_number_removed,
                         sentinel_node_number_positive, axillary_node_number_removed, axillary_node_number_positive,
                         apical_node_number_removed, apical_node_number_positive, surgery_perinodal_spread,
                         pathological_pt, pathological_pn, str(metastasis).lower(), pathological_stage, clinical_stage,
                         self.user_name, sql.last_update()]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list[:-2], data_list[:-2])
        return data_list

    def surgery_block_information_3(self):
        module_name = self.module_list[3]
        review_surgery_date, review_surgery_source, review_surgery_diagnosis, review_surgery_diagnosis_comment, \
        review_surgery_block_id, review_surgery_er, review_surgery_er_percent, review_surgery_pr, review_surgery_pr_percent, \
        review_surgery_her2, review_surgery_her2_grade, review_surgery_fish, review_surgery_ki67 = ['NA', ] * 13
        data_list = ['NA', ] * 13
        check = False
        while not check:
            review = ask.ask_y_n('Has a review (of diagnosis or IHC details) been done of this surgery block?')
            if review:
                review_surgery_date = ask.check_date('Date of review (if multiple dates?): ')
                review_surgery_source = input(
                    'Name of Review Laboratory (Enter multiple if required Lab_test): ')
                review_surgery_diagnosis = input('Enter diagnosis of review: ')
                review_surgery_diagnosis_comment = input('Additional comments for review diagnosis: ')
                review_surgery_block_id = self.surgery_block_id
                block_id = ask.ask_y_n('Has the block been relabelled in the review?')
                if block_id:
                    old_block_id = input('Please enter old block id: ')
                    new_block_id = input('Please enter new block id: ')
                    review_surgery_block_id = old_block_id + ' relabelled to ' + new_block_id
                review_ihc = ask.ask_y_n('Has the IHC result for any marker been reviewed by another lab?')
                if review_ihc:
                    review_surgery_er, review_surgery_er_percent, review_surgery_pr, review_surgery_pr_percent, \
                    review_surgery_her2, review_surgery_her2_grade, review_surgery_fish, review_surgery_ki67 = \
                        BlockDescription.ihc_report('review_surgery')
            data_list = [review_surgery_date, review_surgery_source, review_surgery_diagnosis,
                         review_surgery_diagnosis_comment, review_surgery_block_id, review_surgery_er,
                         review_surgery_er_percent, review_surgery_pr, review_surgery_pr_percent, review_surgery_her2,
                         review_surgery_her2_grade, review_surgery_fish, review_surgery_ki67]
            col_list = names(module_name)
            check = sql.review_input(self.file_number, col_list[:-2], data_list)
        data = data_list + [self.user_name, sql.last_update()]
        return data

    def add_data(self):
        col_list = names(self.module_list[0])
        enter = ask.ask_y_n("Enter " + self.print_statements[0])
        if enter:
            data = self.surgery_block_information_0()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)
        col_list = names(self.module_list[1])
        enter = ask.ask_y_n("Enter " + self.print_statements[1])
        if enter:
            data, block_desc_df = self.surgery_block_information_1
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)
            block_desc_df.to_sql("block_data", self.conn, index=False, if_exists="append")
        col_list = names(self.module_list[2])
        enter = ask.ask_y_n("Enter " + self.print_statements[2])
        if enter:
            data = self.surgery_block_information_2()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)
        col_list = names(self.module_list[3])
        enter = ask.ask_y_n("Enter " + self.print_statements[3])
        if enter:
            data = self.surgery_block_information_3()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)

    def edit_data(self):
        print(self.print_statements[0])
        col_list = names(self.module_list[0])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='fk', key_value=self.fk,
                                    columns=col_list, col_name='surgery_block_id', col_value=self.surgery_block_id)
        if enter:
            data = self.surgery_block_information_0()
            sql.update_multiple(self.conn, self.cursor, self.table_name, col_list, self.file_number, data)
        print(self.print_statements[1])
        col_list = names(self.module_list[1])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='fk', key_value=self.fk,
                                    columns=col_list, col_name='surgery_block_id', col_value=self.surgery_block_id)
        if enter:
            data, block_desc_df = self.surgery_block_information_1
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)
            block_desc_df.to_sql("block_data", self.conn, index=False, if_exists="append")
        print(self.print_statements[2])
        col_list = names(self.module_list[2])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='fk', key_value=self.fk,
                                    columns=col_list, col_name='surgery_block_id', col_value=self.surgery_block_id)
        if enter:
            data = self.surgery_block_information_2()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)
        print(self.print_statements[3])
        col_list = names(self.module_list[3])
        enter = sql.review_data_key(self.conn, self.cursor, self.table_name, key_name='fk', key_value=self.fk,
                                    columns=col_list, col_name='surgery_block_id', col_value=self.surgery_block_id)
        if enter:
            data = self.surgery_block_information_3()
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, col_list, key_name='fk', key_value=self.fk,
                                    data=data)

    @staticmethod
    def node_details():
        nodes = ["sentinel", "axillary", "apical"]
        data_node = []
        for node in nodes:
            node_name = node.capitalize()
            print(node_name + " Node")
            number_removed = input("Number of " + node_name + " Nodes removed: ")
            if int(number_removed) == 0:
                number_removed, number_positive = (node + '_node_not_removed',) * 2
            else:
                number_positive = input("Number of " + node_name + " Nodes positive: ")
            data = [number_removed, number_positive]
            data_node.append(data)
        data_node = ask.flatten_nested_list(data_node)
        return data_node

    @staticmethod
    def bilateral_treatment(surgery_lesion_site, data_type_statement, data_type_options):
        if data_type_options != 'input':
            if surgery_lesion_site.lower == "bilateral":
                print("Right Breast")
                data_type = ask.ask_option(data_type_statement, data_type_options)
                data_type_rb = "rb_" + data_type
                print("Left Breast")
                data_type = ask.ask_option(data_type_statement, data_type_options)
                data_type_lb = "lb_" + data_type
                data = data_type_rb + "; " + data_type_lb
            else:
                data = ask.ask_option(data_type_statement, data_type_options)
        else:
            if surgery_lesion_site.lower == "bilateral":
                print("Right Breast")
                data_type = input(data_type_statement)
                data_type_rb = "rb_" + data_type
                print("Left Breast")
                data_type = input(data_type_statement)
                data_type_lb = "lb_" + data_type
                data = data_type_rb + "; " + data_type_lb
            else:
                data = input(data_type_statement)
        return data

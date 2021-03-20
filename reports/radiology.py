import helper_function.ask_y_n_statement as ask
from helper_function.pccm_names import names_radio as names
import sql.add_update_sql as sql
import additional_tables.radio_tables as radio_tables
from helper_function.option_lists import MultiTest, Radio
import uuid
import pandas as pd


# def file_row(cursor, file_number):
#     cursor.execute("INSERT INTO Radiology(file_number) VALUES ('" + 
# file_number + "')")


class Mammography:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "mammography"
        self.col_list_all = names(self.table)

    def report(self):
        data_list = ask.default_data_list(self.col_list_all)
        check_mammo = ask.ask_option("What is the purpose of this report?",
                                     MultiTest.test_reason_imaging)
        reason_report = check_mammo
        check = False
        while not check:
            mammo = ask.ask_y_n("Are mammography results available for this "
                                "patient?")
            if mammo:
                tomo = ask.ask_y_n("Have 3D Tomography images also been "
                                   "acquired?")
                if tomo:
                    tomography_y_n = "Yes"
                    print("Please include 3d-Tomo observations in Mammography "
                          "results")
                else:
                    tomography_y_n = "No"
                report_date = ask.check_date("Date of mammography: ")
                mammo_place = ask.ask_y_n("Was exam peformed at PCCM?",
                                          yes_ans="PCCM", no_ans="Outside")
                if mammo_place == "Outside":
                    mammography_place = input("Please input Radiologist name "
                                              "and place (Name; Place): ")
                else:
                    mammography_place = mammo_place
                mammography_indication = input("Indication for mammography: ")
                mammography_breast = ask.ask_option("Details described for",
                                                    MultiTest.breast_cancer)
                # masscalc = radio_tables.MassCalcification(self.table,
                                                        #   mass_breast,
                                                        #   self.file_number,
                                                        #   self.user_name)
                mammo_mass = ask.ask_y_n("Is there any mass/lesion detected? ")
                mass_all = []
                mass_data = ['no_mass_detected']
                mass_all.append(mass_data)
                [mammography_massnumber, mammography_masslocation,
                 mammography_massshape, mammography_massmargin,
                 mammography_massnipple_cm, mammography_masssize,
                 mammography_masssize_unit] = ("No mass detected",) * 7
                if mammo_mass:
                    mass_breast = ask.ask_option('What is the location of the'
                                                 ' lesions?',
                                                 MultiTest.breast_cancer)
                
                    masscalc = radio_tables.MassCalcification(self.table,
                                                              mass_breast,
                                                              self.file_number,
                                                              self.user_name)
                # mass_data = mass.multiple_mass()
                    mass_data = masscalc.multiple_mass()
                    mammography_massnumber, mammography_masslocation,
                    mammography_massshape, mammography_massmargin,
                    mammography_massnipple_cm, mammography_masssize,
                    mammography_masssize_unit = mass_data[:-2]
                mammography_calcificationnumber,
                mammography_calcificationlocation,
                mammography_calcificationtype,
                mammography_calcification_comments = ("No Calcification"
                                                      " detected",) * 4
                calc = ask.ask_y_n("Is Calcification present?")
                if calc:
                    mammography_calcificationnumber,
                    mammography_calcificationlocation,
                    mammography_calcificationtype,
                    mammography_calcification_comments = radio_tables.cal_table(self.file_number, mammography_breast)
                mammography_skin_involvement = input("Please input description"
                                                     " of skin involvement if "
                                                     "present: ")
                mammography_node_description, mammography_node_size,
                mammography_node_size_unit = ('nodes_not_described',) * 3
                node_description = ask.ask_y_n('Does the report include '
                                               'description of nodes?')
                if node_description:
                    mammography_node_description = input('Please enter '
                                                         'description of nodes'
                                                         ': )')
                    mammography_node_size,
                    longest_dimension = ask.check_size_input()
                    mammography_node_size_unit = 'NA'
                    if mammography_node_size != 'NA':
                        mammography_node_size_unit = ask.ask_list('Unit of node size: ', MultiTest.size_unit)
                mammo_birad = ask.ask_y_n('Does the report include a BI-RAD'
                                          'assessment/diagnosis?')
                if mammo_birad:
                    mammography_birad = radio_tables.birads()
                else:
                    mammography_birad = "BI-RAD not assigned in report"
                mammography_impression = input('Input Impression(if available'
                                               '): "')
                data_list = [reason_report, report_date, mammography_place,
                             mammography_indication, mammography_breast,
                             mammography_massnumber, mammography_masslocation,
                             mammography_massshape, mammography_massmargin,
                             mammography_massnipple_cm, mammography_masssize,
                             mammography_masssize_unit,
                             mammography_calcificationnumber,
                             mammography_calcificationlocation,
                             mammography_calcificationtype,
                             mammography_calcification_comments,
                             mammography_skin_involvement,
                             mammography_node_description,
                             mammography_node_size, mammography_node_size_unit,
                             mammography_birad, mammography_impression, 
                             tomography_y_n, self.user_name, sql.last_update]
                data_list = [self.file_number] + data_list
            else:
                data_list = [self.file_number] + data_list
            check = sql.review_input(self.file_number, self.col_list_all[:-2],
                                     data_list)
        data_list = data_list + [self.user_name, sql.last_update()]
        return data_list


class Abvs:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "abvs"
        self.col_list_all = names(self.table)

    def report(self):
        data_list = ask.default_data_list(self.col_list_all)
        check = False
        while not check:
            reason_report = ask.ask_option("What is the purpose of this report"
                                           "?", MultiTest.test_reason_imaging)
            report_date = ask.check_date("Date of examination of ABVS: ")
            abvs_acc = input("Accession number of ABVS: ")
            abvs_lesion = ask.ask_option("Location of lesion",
                                         MultiTest.breast_cancer)
            if abvs_lesion in {MultiTest.breast_cancer}:
                abvs_lesion_data = radio_tables.lesion_location(abvs_lesion)
            else:
                abvs_lesion_data = "NA"
            abvs_size = ask.ask_option("Size of lesion", ["<2 cm", "2-5 cm",
                                       ">5 cm", "Other"])
            abvs_dist = ask.ask_option("Distance from Skin (cm)", ["<0.5 cm",
                                       ">0.5 cm", "Other"])
            abvs_pect = input("Distance from Pectoralis Major (cm): ")
            abvs_diagnosis = ask.ask_option("ABVS Diagnosis", Radio.diagnosis)
            data_list = [self.file_number, reason_report, report_date,
                         abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size,
                         abvs_dist, abvs_pect, abvs_diagnosis]
            check = sql.review_input(self.file_number, self.col_list_all[:-2],
                                     data_list)
        data_list = data_list + [self.user_name, sql.last_update()]
        return data_list


class Ultrasound:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "abvs"
        self.col_list_all = names(self.table)

    def report(self):
        data_list = ask.default_data_list(self.col_list_all)
        check = False
        while not check:
            reason_report = ask.ask_option("What is the purpose of this repor"
                                           "t?", MultiTest.test_reason_imaging)
            report_date = ask.check_date("Date of examination of ultrsound: ")
            mammo_place = ask.ask_y_n("Was exam peformed at PCCM?",
                                      yes_ans="PCCM", no_ans="Outside")
            if mammo_place == "Outside":
                sonomammo_place = input("Please input Radiologist name and"
                                        " place (Name; Place): ")
            else:
                sonomammo_place = mammo_place
            sonomammo_breast = ask.ask_option("Details described for",
                                              MultiTest.breast_cancer)
            mass_sonomammo = ask.ask_y_n("Is there any mass detected")
            breast = sonomammo_breast
            masscalc = radio_tables.MassCalcification(self.table, breast, self.file_number, self.user_name)
            if mass_sonomammo:
                mass_sonomammo = 'Mass/Lesion Detected'
                table = "sonnomammography_mass"
                
                mass_number, sonomammo_mass_location,
                sonomammo_mass_location_clock, sonomammo_masss_shape,
                sonomammo_mass_margin, sonomammo_mass_echo,
                sonomammo_mass_size,
                sonomammo_mass_size_unit = masscalc.multiple_mass()
            else:
                mass_sonomammo, mass_number, sonomammo_mass_location,
                sonomammo_mass_location_clock, sonomammo_masss_shape,
                sonomammo_mass_margin, sonomammo_mass_echo,
                sonomammo_mass_size, sonomammo_mass_size_unit = ("No Mass"
                                                                 " Detected",) * 9
            sonomammo_calc = ask.ask_option("Calcification", MultiTest.breast_cancer)
            if sonomammo_calc in MultiTest.breast_cancer:
                sonomammo_calc_type = ask.ask_option("Calcification location", Radio.calcification)
            else:
                sonomammo_calc_type = "NA"
            sonomammo_vasc = ask.ask_option("Vascularity", Radio.vascularity)
            sono_birad = ask.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if sono_birad:
                sonomammo_birad = radio_tables.birads()
            else:
                sonomammo_birad = "NA"
            sonomammo_impression = input("Input Impression(if available): ")
            node_description = ask.ask_y_n('Does the report include description of nodes?')
            if node_description:
                sonomammo_node_description = input('Please enter description of nodes: ')
                sonomammo_node_size = input('Size of node if reported without unit (else enter NA): ')
                sonomammo_node_size_unit = input('Unit of node size')
            else:
                sonomammo_node_description, sonomammo_node_size, sonomammo_node_size_unit = ('nodes_not_described',) * 3
            data_list = [self.file_number, reason_report, report_date, sonomammo_place, sonomammo_breast,
                         mass_sonomammo, mass_number, sonomammo_mass_location, sonomammo_mass_location_clock,
                         sonomammo_masss_shape, sonomammo_mass_margin, sonomammo_mass_echo, sonomammo_mass_size,
                         sonomammo_mass_size_unit, sonomammo_calc, sonomammo_calc_type, sonomammo_vasc, sonomammo_birad,
                         sonomammo_node_description, sonomammo_node_size, sonomammo_node_size_unit,
                         sonomammo_impression]
            check = sql.review_input(self.file_number, self.col_list_all[:-2], data_list)
        data_list = data_list + [self.user_name, sql.last_update()]
        return data_list


class Mri:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "mri_breast"
        self.col_list_all = names(self.table)

    def report(self):
        data_list = ask.default_data_list(self.col_list_all)
        check = False
        while not check:
            reason_report = ask.ask_option("What is the purpose of this report?", MultiTest.test_reason_imaging)
            report_date = ask.check_date("Date of examination: ")
            mri_place = ask.ask_y_n("Was exam peformed at PCCM?", yes_ans="PCCM", no_ans="Outside")
            mri_breast_acc = input("Accession number of MRI: ")
            mri_breast_described = ask.ask_option("Details described for", MultiTest.breast_cancer)
            fgt_mri = ask.ask_option("Ammount of Fibroglandular Tissue",
                                     ["a. Almost entirely fat", "b. Scattered fibroglandular tissue",
                                      "d. Extreme fibroglandular tissue", "Other"])
            bpe_level_mri = ask.ask_option("Background parenchymal enhancement Level",
                                           ["Minimal", "Mild", "Moderate", "Marked", "Other"])
            bpe_symm_mri = ask.ask_option("Background parenchymal enhancement Symmetry",
                                          ["Symmetric", "Asymmetric", "Other"])
            focus_mri = input("Details of Focus: ")
            mass_mri = ask.ask_y_n("Are masses detected?")
            if mass_mri:
                mass_mri = "Mass Detected"
                table = "mri_mass"
                mri_mass_number, mass_location, mass_shape, mass_margin, mass_internal = \
                    radio_tables.multiple_mass(table, mri_breast_described)
            else:
                mass_mri = "No Mass Detected"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal = ("NA",) * 6
            asso_feat = ["Nipple Retraction", "Nipple Invasion", "Skin Retraction", "Skin Thickening",
                         "Axillary adenopathy", "Pectoralis muscle invasion", "Chest wall invasion",
                         "Architectural Distortion"]
            asso_feat_data = []
            for index in (asso_feat):
                print("Associated feature: " + index)
                print("Detailed description can be added by choosing 'Other'")
                var = ask.ask_option(index, MultiTest.breast_cancer)
                asso_feat_data.append(var)
            asso_feat_9 = ask.ask_option("Associated Feature: Skin Invasion",
                                         ["Direct invasion", "Inﬂammatory cancer", "Other"])
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, \
            asso_feat_8 = asso_feat_data
            fat_lesions = ask.ask_option("Fat Containing Lesions",
                                         ["Lymph nodes: Normal", "Lymph nodes: Abnormal", "Fat necrosis",
                                          "Hamartoma", "Postoperative seroma", "hematoma with fat"])
            mri_breast_kinetics_initial = ask.ask_option("Kinetic curve assessment Signal intensity "
                                                         "(SI)/time curve description (Initial Phase)",
                                                         ["Slow", "Medium", "Fast", "Other"])
            mri_breast_kinetics_delayed = ask.ask_option("Kinetic curve assessment Signal intensity "
                                                         "(SI)/time curve description (Delayed Phase)",
                                                         ["Persistent", "Plateau", "Washout", "Other"])
            mri_breast_non_enhance = ask.ask_option("Non-enhancing findings",
                                                    ["Ductal precontrast high signal on T1W", "Cyst",
                                                     "Postoperative collections (hematoma/seroma)",
                                                     "Post-therapy skin thickening and trabecular "
                                                     "thickening", "Signal void from foreign bodies, "
                                                                   "clips, etc.", "Other"])
            mri_breast_implant = input("Implant related findings: ")
            mri_breast_lesion = ask.ask_option("Location of lesion", MultiTest.breast_cancer)
            if mri_breast_lesion in {MultiTest.breast_cancer}:
                mri_breast_lesion_location = radio_tables.lesion_location(mri_breast_lesion)
                mri_breast_lesion_depth = input("Lesion depth: ")
            else:
                mri_breast_lesion_location, mri_breast_lesion_depth = ("NA",) * 2
            mri_breast_size = ask.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            mri_breast_dist = ask.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            mri_breast_pect = input("Distance from Pectoralis Major (cm): ")
            mri_breast_birad = ask.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if mri_breast_birad:
                mri_breast_birad = radio_tables.birads()
            else:
                mri_breast_birad = "No BI-RAD Category given in report"
            data_list = [self.file_number, reason_report, report_date, mri_place, mri_breast_acc, mri_breast_described, fgt_mri,
                         bpe_level_mri, bpe_symm_mri, focus_mri, mass_mri, mri_mass_number, mass_location, mass_shape,
                         mass_margin, mass_internal, asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5,
                         asso_feat_6, asso_feat_7, asso_feat_8, asso_feat_9, fat_lesions, mri_breast_kinetics_initial,
                         mri_breast_kinetics_delayed, mri_breast_non_enhance, mri_breast_implant, mri_breast_lesion,
                         mri_breast_lesion_location, mri_breast_lesion_depth, mri_breast_size, mri_breast_dist,
                         mri_breast_pect, mri_breast_birad]
            check = sql.review_input(self.file_number, self.col_list_all[:-2], data_list)
        data_list = data_list + [self.user_name, sql.last_update()]
        return data_list


class Radiology:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.tables = ['Mammography', 'ABVS', 'Ultrasound', 'MRI']


    def get_table(self, type_action):
        table = ask.ask_list('What type of Radiology data do you want to enter'
                             '/edit? ', list(self.tables))
        type_action = ask.ask_y_n('Do you want to add data or edit data',
                                  yes_ans='add', no_ans='edit')
        table = table.lower()
        if type_action == 'add':
            self.add_radio(table)
        if type_action == 'edit':
            self.edit_radio(table)

    def add_radio(self, table):
        pk = uuid.uuid4().hex
        sql.add_pk_fk_to_table(self.conn, self.cursor, table, col_name='pk',
                              pk=pk)
        print(table)
        enter = ask.ask_y_n("Enter " + table)
        col_list = names(table)
        if enter:
            data = self.table_fx().get(table)
            try:
                sql.update_multiple_key(self.conn, self.cursor, table,
                                        col_list, key_name='pk', key_value=pk,
                                        data=data)
            except TypeError:
                print(data)

    def edit_radio(self, table):
        col_list = names(table)
        enter = sql.view_multiple(self.conn, table, col_list, self.file_number)
        if enter == "Add data":
            self.add_radio(table)
        elif enter == "Edit data":
            sql_statement = ('SELECT ' + ", ".join(col_list) + " FROM '" +
                             table +
                             "' WHERE file_number = '" + self.file_number + "'"
                             )
            df = pd.read_sql(sql_statement, self.conn)
            sql.print_df(df)
            pk, value_row_to_edit = sql.retrieve_with_pk_to_edit(df, value_col='reason_report', table=table,
                                                                 cursor=self.cursor, pk=False)
            print('value_row_to_edit: ', value_row_to_edit)
            if not value_row_to_edit:
                sql.delete_rows(self.cursor, table, col_name="file_number", col_data=self.file_number)
                self.add_radio(table)
            else:
                self.edit_data_pk(pk, value_row_to_edit, table)
        else:
            print('\n No edits will be made to this table\n')

    def edit_data_pk(self, pk, value_row_to_edit, table):
        col_list = names(table)
        enter = sql.review_data_key(self.conn, self.cursor, table, key_name='pk', key_value=pk,
                                    columns=col_list, col_name='report_date', col_value=value_row_to_edit)
        if enter:
            data = self.table_fx().get(table)
            sql.update_multiple_key(self.conn, self.cursor, table, col_list, key_name='pk', key_value=pk,
                                    data=data)

    def table_fx(self):
        mammo = Mammography(self.conn, self.cursor, self.file_number, self.user_name)
        abvs = Abvs(self.conn, self.cursor, self.file_number, self.user_name)
        usg = Ultrasound(self.conn, self.cursor, self.file_number, self.user_name)
        mri = Mri(self.conn, self.cursor, self.file_number, self.user_name)
        tables = {'Mammography': mammo.report(), 'ABVS': abvs.report(), 'Ultrasound': usg.report(), 'MRI': mri.report()}
        return tables

    def add_data(self):
        self.get_table(type_action='add')

    def edit_data(self):
        self.get_table(type_action='edit')


if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('/mnt/v/pccm_db/main/DB/PCCM_DB_test_final_final_final_2020_09_15.db')
    cursor = conn.cursor()
    file_number = 'test'
    user_name = 'dk'
    radio = Radiology(conn, cursor, file_number, user_name)
    radio.add_data()

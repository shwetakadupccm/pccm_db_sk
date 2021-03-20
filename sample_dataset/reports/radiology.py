import helper_function.ask_y_n_statement as ask
from helper_function.pccm_names import names_radio
import sql.add_update_sql as sql
import sample_dataset.additional_rnd_tables.radio_tables as radio_tables
from helper_function.option_lists import MultiTest, Radio
import uuid
import pandas as pd
import names
from sample_dataset.sample_data_strings import Radiology
import sample_dataset.general_functions as gf


class Mammography:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "mammography"
        self.col_list_all = names_radio(self.table)

    def report(self):
        data_list = ask.default_data_list(self.col_list_all[1:])
        check_mammo = gf.get_choice(MultiTest.test_reason)
        reason_report = check_mammo
        mammo = gf.get_bool()
        if mammo:
            tomo = gf.get_bool()
            if tomo:
                tomography_y_n = "Yes"
            else:
                tomography_y_n = "No"
            report_date = gf.gen_date('2019-03-13')
            mammo_place = gf.get_choice(["PCCM", "Outside"])
            if mammo_place == "Outside":
                mammography_place = names.get_full_name()
            else:
                mammography_place = mammo_place
            mammography_indication = gf.get_choice(Radiology.mammo_indication)
            mammography_breast = gf.get_choice(MultiTest.breast_cancer)
            mammo_mass = gf.get_bool()
            mass_all = []
            mass_data = ['no_mass_detected']
            mass_all.append(mass_data)
            mammography_massnumber = "No mass detected"
            mammography_masslocation = "No mass detected"
            mammography_massshape = "No mass detected"
            mammography_massmargin = "No mass detected"
            mammography_massnipple_cm = "No mass detected"
            mammography_masssize = "No mass detected"
            mammography_masssize_unit = "No mass detected"
            mass_longest_dimension = 'na'
            if mammo_mass:
                mass_breast = gf.get_choice(MultiTest.breast_cancer)
                mass = radio_tables.MassCalcification(self.table, mass_breast,
                                                      self.file_number,
                                                      self.user_name)
                mammography_massnumber, mass_dat = mass.multiple_mass()
                [mammography_masslocation, mass_name, mass_quadrant,
                 mammography_massshape, mammography_massmargin,
                 mammography_massnipple_cm, mammography_masssize,
                 mass_longest_dimension,
                 mammography_masssize_unit, modality] = mass_dat[1:]
            mammography_calcificationnumber = "No Calcification detected"
            mammography_calcificationlocation = "No Calcification detected"
            mammography_calcificationtype = "No Calcification detected"
            mammography_calcification_comments = "No Calcification detected"
            calc = gf.get_bool()
            if calc:
                mammography_calcification = radio_tables.cal_table(self.file_number, mammography_breast)
                (mammography_calcificationnumber,
                 mammography_calcificationlocation,
                 mammography_calcificationtype,
                 mammography_calcification_comments) = mammography_calcification
            mammography_skin_involvement = gf.get_choice(Radiology.skin_involvement)
            mammography_node_description = 'nodes_not_described'
            mammography_node_size = 'nodes_not_described'
            mammography_node_size_unit = 'nodes_not_described'
            node_description = gf.get_bool()
            if node_description:
                mammography_node_description = gf.get_choice(Radiology.node_description)
                mammography_node_size = gf.get_number_lt(3,10)
                mammography_node_size_unit = 'cm'
            mammo_birad = gf.get_bool()
            if mammo_birad:
                mammography_birad = radio_tables.birads()
            else:
                mammography_birad = "BI-RAD not assigned in report"
            mammography_impression = gf.get_choice(Radiology.impression)
            data_list = [reason_report, report_date, mammography_place,
                         mammography_indication, mammography_breast,
                         mammography_massnumber, mammography_masslocation,
                         mammography_massshape, mammography_massmargin,
                         mammography_massnipple_cm, mammography_masssize[0],
                         mammography_masssize_unit,
                         mammography_calcificationnumber,
                         mammography_calcificationlocation,
                         mammography_calcificationtype,
                         mammography_calcification_comments,
                         mammography_skin_involvement,
                         mammography_node_description,
                         mammography_node_size, mammography_node_size_unit,
                         mammography_birad, mammography_impression, 
                         tomography_y_n]
            data_list = [str(dat) for dat in data_list]
        data_list = [self.file_number] + data_list + [self.user_name,
                                                      sql.last_update()]
        return data_list

    def add_radio(self):
        rep = gf.get_number(4)
        for i in range(rep):
            pk = uuid.uuid4().hex
            sql.add_pk_fk_to_table(self.conn, self.cursor, self.table, col_name='pk',
                                   pk=pk)
            col_list = names_radio(self.table)
            # report = Mammography(self.conn, self.cursor, self.file_number, self.user_name)
            data = self.report()
            for col, dat in zip(col_list, data):
                print(col, dat)
            sql.update_multiple_key(self.conn, self.cursor, self.table,
                                    col_list, key_name='pk', key_value=pk,
                                    data=data)


if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('d:/repos/pccm_db/main/DB/PCCM_DB_2021_02_25.db')
    cursor = conn.cursor()
    file_number = gf.get_file_id()
    user_name = 'dk'
    radio = Mammography(conn, cursor, file_number, user_name)
    radio.add_radio()
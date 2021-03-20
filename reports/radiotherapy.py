
# TODO run check of this module since have added no_rt option, requires_follow_up option.

import helper_function.ask_y_n_statement as ask
from sql.add_update_sql import review_input, update_multiple, review_data, last_update
import helper_function.pccm_names as names
from helper_function.option_lists import RadiotherapyOptions
from itertools import chain


class RadioTherapy:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "radiotherapy"
        self.col_list = names.names_radiation()[:-2]

    def radiation(self):
        check = False
        data_list = ask.default_data_list(self.col_list)
        while not check:
            radio = ask.ask_y_n("Radiotherapy Recieved?")
            if not radio:
                radio_opt = ask.ask_listd("Reason for not recieving radiotherapy: ", RadiotherapyOptions.no_rt_reason)
                radio = 'not_recieved|' + radio_opt
                data_list = [[radio] + ask.na_data_list(self.col_list)[1:]]
            else:
                radio = "rt_received"
                data_list = [[radio] + ask.fup_data_list(self.col_list)[1:]]
                radio_details = ask.ask_y_n('Is radiotherapy discharge summary present?')
                if radio_details:
                    radio_date = ask.check_date("Date of starting radiotherapy: ")
                    radio_type = ask.ask_list("Type of radiotherapy", ["Cobalt", "Linear Accelerator based treatment", "Not"
                    "known", "Other"])
                    imrt = ask.ask_y_n_na("Did the patient opt for Intensity"
                    "Modulated/3Dimensional conformal radiotherapy" 
                    " (IMRT/3DCRT)")
                    if imrt == "Yes":
                        imrt = "IMRT/3DCRT_yes"
                    if imrt == "No":
                        imrt = ask.ask_list("Reasons for not opting for " 
                        "IMRT/3DCRT", RadiotherapyOptions.reason_imrt)
                    rt_admin = [self.radiation_admin(location) for location in RadiotherapyOptions.
                    rt_location]
                    rt_admin = list(chain.from_iterable(rt_admin))
                    print(rt_admin)
                    rt_boost = ['boost_not_given', ] * len(RadiotherapyOptions.
                    rt_location) * 2
                    boost = ask.ask_y_n('Was boost administered')
                    if boost:
                        rt_boost = [self.radiation_admin(location, boost=True) 
                        for location in RadiotherapyOptions.rt_location]
                        rt_boost = list(chain.from_iterable(rt_boost))
                        print(rt_boost)
                    radio_tox = ask.ask_y_n("Did radiotherapy related acute toxicity occur?")
                    if radio_tox:
                        radio_tox = input("Type of toxicity: ")
                    radio_delayed_tox = ask.ask_y_n_na("Did radiotherapy" 
                    "related delayed toxicity occur?", na_ans="data_not_available")
                    radio_finish = ask.check_date_chron(date_string="Date of" 
                    " finishing radiotherapy: ", date_ref=radio_date,
                    past_date_check=True)
                    radio_location = ask.ask_list("Location of radiotherapy: ", 
                    RadiotherapyOptions.rt_hosp)
                    radio_onco = ask.ask_list("Name of Radiation Oncologist", RadiotherapyOptions.rt_doc)
                    data_list = [radio, radio_date,  radio_type, imrt], rt_admin, rt_boost, [str(radio_tox), radio_delayed_tox, radio_finish, radio_location, radio_onco]
                else:
                    details = 'NA'
                    details_check = ask.ask_y_n('Are any details of radiotherapy available?')
                    if details_check:
                        details = input('Details of radiotherapy and source: ')
                    radio = radio + '|' + details
                    data_list = [[radio] + ask.fup_data_list(self.col_list)[1:]]
            data_list = list(chain.from_iterable(data_list))
            col_list = self.col_list
            check = review_input(self.file_number, col_list, data_list)
        return data_list

    def add_data(self):
        col_list = names.names_radiation()
        data = self.radiation()
        update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)

    def edit_data(self):
        col_list = names.names_radiation()
        enter = review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = self.radiation()
            update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)

    def radiation_admin(self, location, boost=False):
        quest = 'Was rt given to '
        if boost:
            quest = 'Was rt boost given to '
        rt_admin_check = ask.ask_y_n(quest + location + '? ')
        dat_list, rt_admin = ['not_given', ]*2, 'not_given'
        if rt_admin_check:
            check = False
            while not check:
                all_dosage = ['not_given', ] * 4
                dosecheck = False
                while not dosecheck:
                    if location.startswith('other', 0, len('other')):
                        rt_admin = input('Describe location: ')
                    else:
                        rt_admin = 'rt_given'
                        if boost:
                            rt_admin = 'rt_boost_given'
                    dose = ask.check_number_input('Gy administered: ', error='input only number or NA') + 'Gy'
                    cycles = ask.check_number_input('Cycles given: ', error='input only number or NA') + '#'
                    duration = ask.check_number_input('Weeks given: ', error='input only number or NA') + 'weeks'
                    mev = ask.check_number_input('meV administered: ', error='input only number or NA') + 'meV'
                    comments_add = ask.ask_y_n('Additional Comments?')
                    comments = 'NA'
                    if comments_add:
                        comments = input('Comments: ')
                    all_dosage = [dose, cycles, duration, mev, comments]
                    col_list = ['dose', 'cycles', 'duration', 'meV', 'comments']
                    dosecheck = review_input(self.file_number, col_list, all_dosage)
                rt_dosage = '| '.join(tuple(all_dosage))
                col_list = [location, 'dosage']
                dat_list = [rt_admin, rt_dosage]
                check = review_input(self.file_number, col_list, dat_list)
        return dat_list

import helper_function.ask_y_n_statement as ask
import pandas as pd
import sql.add_update_sql as sql
from helper_function.pccm_names import names_nact as names
from additional_tables.chemo_tables import drug_table_enter, tox_table


class NeoAdjuvant:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "radiotherapy"

    def nact_test(self):
        col_drug = names("nact_drug_table")
        drug_table = pd.DataFrame(columns=col_drug)
        col_tox = names('nact_tox_table')
        toxicity = pd.DataFrame(columns=col_tox)
        nact_status, place_nact, details_nact, plan_nact, date_start_nact, 
        patient_weight_nact, nact_drugs_administered, number_cycles_nact, 
        cycle_weekly_frequency, drugs_totaldose, drugs_unit, toxicity_type, 
        toxicity_grade, toxicity_treatment, toxicity_response, 
        nact_change_due_to_toxicity, tumour_response_check_method, 
        tumour_response_nact, tumour_size, tumour_size_unit, 
        date_tumour_size_checked, nact_response_impression,
        nact_response_node, nact_completion_status, nact_end_date, 
        trastuzumab_use_nact, trastuzumab_regime_nact, 
        trastuzumab_courses_taken_nact, hormone_therapy_nact, 
        hormone_therapy_type_nact, hormone_therapy_duration, 
        horomone_therapy_side_effects = ['NA', ]*33
        data_list = ['NA', ]*30 + [self.user_name, sql.last_update()]
        check = False
        while not check:
            nact_status = ask.ask_y_n_na("Has neo adjuvant therapy been done for the patient (Please check for chemotherapy and/hormone therapy)?")
            if nact_status == 'Yes':
                place_nact = ask.ask_y_n_na("Has neo adjuvant therapy been done at PCCM?", "At PCCM",
                                            "Outside", "Not Certain, requires follow-up")
                details_nact = ask.ask_y_n("Are neo adjuvant therapy details available?", "Details Available",
                                           "Follow-up required")
                if details_nact == "Follow-up required":
                    plan_nact, date_start_nact, patient_weight_nact, nact_drugs_administered, number_cycles_nact, cycle_weekly_frequency, drugs_totaldose, drugs_unit, toxicity_type, toxicity_grade, toxicity_treatment, toxicity_response, toxicity_at_cycle, nact_change_due_to_toxicity, tumour_response_check_method, tumour_response_nact, tumour_size, tumour_size_unit, date_tumour_size_checked, nact_response_impression, nact_response_node, nact_completion_status, nact_end_date, trastuzumab_use_nact, trastuzumab_regime_nact, trastuzumab_courses_taken_nact, hormone_therapy_nact, hormone_therapy_type_nact, hormone_therapy_duration,  dhoromone_therapy_side_effects = (details_nact,)*30
                elif details_nact == "Details Available":
                    plan_nact = input("What is the plan of NACT (for eg., 4 cycles AC followed by 12 cycles Paclitaxel; "
                                      "Include hormone therapy plan here):")
                    date_start_nact = ask.check_date(
                        "Date of starting neo-adjuvant therapy: ")
                    patient_weight_nact = input(
                        "Weight of patient at start of therapy (in kgs): ")
                    check_wt = ask.ask_y_n("Is weight at any other time point mentioned in report "
                                           "(with date, if given)?")
                    while check_wt:
                        other_wt = input(
                            "Time point at which weight mentioned: ")
                        other_wt = other_wt + " " + \
                            input("Weight of patient at " + other_wt + ": ")
                        patient_weight_nact = patient_weight_nact + "; " + other_wt
                        check_wt = ask.ask_y_n("Is weight at any other time point mentioned in report "
                                               "(with date, if given)?")
                    drug_admin = drug_table_enter(file_number, drug_table)
                    data_drug = col_drug[1:]
                    data_drug_list = []
                    for index in data_drug:
                        data_drug = "; ".join(list(drug_admin.loc[:, index]))
                        data_drug_list.append(data_drug)
                    nact_drugs_administered, number_cycles_nact, cycle_weekly_frequency, drugs_totaldose, drugs_unit\
                        = data_drug_list
                    toxicity = tox_table(
                        file_number, nact_drugs_administered, toxicity)
                    columns = col_tox
                    tox_details = []
                    for column in columns:
                        tox_detail = toxicity.loc[:, column].drop_duplicates()
                        tox_details.append(list(tox_detail))
                    tox_details = ask.join_lists(tox_details, "; ")
                    print(tox_details)
                    file_number, nact_drugs_administered, toxicity_type, toxicity_grade, toxicity_treatment, toxicity_response, \
                        toxicity_at_cycle, nact_change_due_to_toxicity = tox_details
                    tumour_response_check_method = ask.ask_option("Response to NACT measured by", ['Mammography',
                                                                                                   'SonoMammography'])
                    if tumour_response_check_method not in {'Mammography', 'SonoMammography'}:
                        tumour_response_nact, tumour_size, tumour_size_unit, date_tumour_size_checked, nact_response_impression, \
                            nact_response_node, nact_response_impression, nact_response_node = (
                                tumour_response_check_method,)*8
                    else:
                        tumour_response_nact = ask.ask_list("Response of tumour",
                                                            ["Partial", "Complete", "No Effect", "Other"])
                        tumour_size = input(
                            "Tumour size (without unit, e.g., 2 x 4 x 5) after treatment: ")
                        tumour_size_unit = ask.ask_option(
                            "Tumour size unit", ['mm', 'cm'])
                        date_tumour_size_checked = ask.check_date(
                            "Date tumour size checked: ")
                        nact_response_impression = input(
                            'Please input impression given in report for NACT response: ')
                        nact_node = ask.ask_y_n(
                            'Does the report mention node response? ')
                        nact_response_node = 'nact_node_response_not_mentioned'
                        if nact_node:
                            nact_response_node = input(
                                'Please input statement on node response to NACT: ')
                    trast_nact = ask.ask_y_n("Trastuzumab used?")
                    if trast_nact:
                        trastuzumab_regime_nact = ask.ask_option(
                            "Trastuzumab use was", ["Sequential", "Concurrent"])
                        trastuzumab_use_nact = "Trastuzumab used"
                        trastuzumab_courses_taken_nact = input(
                            "Number of courses of trastuzumab/herceptin taken: ")
                    else:
                        trastuzumab_use_nact, trastuzumab_regime_nact, trastuzumab_courses_taken_nact, \
                            = ("no_neo_adjuvant_trastuzumab", )*3
                    nact_end_date = ask.check_date(
                        "Date of completion of NACT: ")
                    complete_nact = ask.ask_y_n(
                        "Was NACT completed as per schedule? ")
                    if complete_nact:
                        nact_completion_status = "nact_complete"
                    else:
                        nact_completion_status = ask.ask_option("Reason for discontinuation",
                                                                ["Toxicity", "Reluctance of patient",
                                                                 "Progression on chemotherapy",
                                                                 "Advised by treating doctor",
                                                                 "Death due to toxicity",
                                                                 "Death due to progressive disease",
                                                                 "Preferred treatment at another centre",
                                                                 "Death due to unrelated cause",
                                                                 "Patient was unable to afford treatment"])
                        nact_completion_status = "NACT incomplete: " + nact_completion_status
                    hormone_therapy = ask.ask_y_n_na(
                        "Was hormone therapy given?")
                    if hormone_therapy == 'Yes':
                        hormone_therapy_nact = "naht_given"
                        hormone_therapy_type_nact = ask.ask_option(
                            "Hormone therapy type", ["Sequential", "Concurrent"])
                        hormone_therapy_duration = input(
                            "What was the duration of therapy? ")
                        therapy_side = ask.ask_y_n_na(
                            "Were any side effects observed ?")
                        horomone_therapy_side_effects = 'no_side_effects'
                        if therapy_side == 'Yes':
                            horomone_therapy_side_effects = input(
                                "Please give details of side effects observed: ")
                        nact_naht = ask.ask_y_n(
                            'Was chemotherapy given in addition to hormone therapy?')
                        if nact_naht:
                            nact_status = 'nact_and_naht_given'
                        else:
                            nact_status = 'naht_given'
                    elif hormone_therapy == 'No':
                        hormone_therapy = "no_naht"
                        nact_status = "nact_given"
                        hormone_therapy_nact, hormone_therapy_type_nact, hormone_therapy_duration, \
                            horomone_therapy_side_effects = (
                                hormone_therapy,) * 4
                    else:
                        hormone_therapy_nact, hormone_therapy_type_nact, hormone_therapy_duration, \
                            horomone_therapy_side_effects = (
                                hormone_therapy,) * 4
                        nact_status = "nact_given"
            data_list = [nact_status, place_nact, details_nact, plan_nact, date_start_nact, patient_weight_nact,
                         nact_drugs_administered, number_cycles_nact, cycle_weekly_frequency, drugs_totaldose, drugs_unit,
                         toxicity_type, toxicity_grade, toxicity_treatment, toxicity_response, toxicity_at_cycle,
                         nact_change_due_to_toxicity, tumour_response_check_method, tumour_response_nact, tumour_size,
                         tumour_size_unit, nact_response_impression, nact_response_node, date_tumour_size_checked,
                         nact_completion_status, nact_end_date, trastuzumab_use_nact,
                         trastuzumab_regime_nact, trastuzumab_courses_taken_nact, hormone_therapy_nact,
                         hormone_therapy_type_nact, hormone_therapy_duration, horomone_therapy_side_effects, self.user_name,
                         sql.last_update()]
            col_list = names("neo_adjuvant_therapy")
            check = sql.review_input(file_number, col_list, data_list)
        return data_list, drug_table, toxicity

    def clip_information(self):
        clip_number, clip_date, clip_cycle = ['NA, ']*3
        data_list = clip_number, clip_date, clip_cycle
        check = False
        while not check:
            clip = ask.ask_y_n("Was Clip inserted for surgery?")
            if clip:
                clip_number = input("Number of clips inserted: ")
                clip_date = ask.check_date("Date of clip insertion: ")
                clip_cycle = input("Clip inserted after cycle? ")
            else:
                clip_date, clip_number, clip_cycle = ("NA", )*3
            data_list = clip_number, clip_date, clip_cycle
            col_list = names("clip_information")
            check = sql.review_input(self.file_number, col_list, data_list)
        return data_list

    def add_data(self):
        table = "neo_adjuvant_therapy"
        data = self.nact_test()
        data_sql, drug_table, tox_response = data
        sql.update_multiple(self.conn, self.cursor, table,
                            names(table), self.file_number, data_sql)
        drug_table.to_sql("nact_drug_table", self.conn,
                          index=False, if_exists="append")
        tox_response.to_sql("nact_tox_table", self.conn,
                            index=False, if_exists="append")
        enter = ask.ask_y_n("Input Clip Information")
        if enter:
            data = self.clip_information()
            col_list = names("clip_information")
            sql.update_multiple(self.conn, self.cursor, table,
                                col_list, self.file_number, data)

    def edit_data(self):
        table = "neo_adjuvant_therapy"
        enter = sql.review_data(self.conn, self.cursor,
                                table, self.file_number, names(table))
        if enter:
            sql.delete_rows(self.cursor, 'nact_drug_table',
                            "file_number", self.file_number)
            sql.delete_rows(self.cursor, 'nact_tox_table',
                            "file_number", self.file_number)
            data = self.nact_test()
            data_sql, drug_table, tox_response = data
            sql.update_multiple(self.conn, self.cursor, table, names(
                table), self.file_number, data_sql)
            drug_table.to_sql("nact_drug_table", self.conn,
                              index=False, if_exists="append")
            tox_response.to_sql("nact_tox_table", self.conn,
                                index=False, if_exists="append")

        print("clip information")
        module = "clip_information"
        col_list = names(module)
        enter = sql.review_data(self.conn, self.cursor,
                                table, self.file_number, col_list)
        if enter:
            data = self.clip_information()
            sql.update_multiple(self.conn, self.cursor, table,
                                col_list, self.file_number, data)

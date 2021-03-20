import helper_function.ask_y_n_statement as ask
import pandas as pd
import sql.add_update_sql as sql
from helper_function.pccm_names import names_chemotherapy as names
from additional_tables.chemo_tables import drug_table_enter, tox_table



def chemotherapy(file_number, user_name):
    col_drug = names("chemo_drug_table")
    drug_table = pd.DataFrame(columns=col_drug)
    col_tox = names('chemo_tox_table')
    toxicity = pd.DataFrame(columns=col_tox)
    data_list = ['data_to_be_entered', ]*27 + [user_name, sql.last_update()]
    check = False
    while not check:
        chemo = ask.ask_y_n_na("Has adjuvant chemotherapy been done for the patient?")
        if chemo == 'Yes':
            place_chemo = ask.ask_y_n_na("Has Adjuvant Chemotherapy been done at PCCM?", "At PCCM",
                                                       "Outside", "Not Certain, requires follow-up")
            details_chemo = ask.ask_y_n("Are Adjuvant Chemotherapy details available?",
                                                      "Details Available", "Follow-up required")
            chemo = "act_given"
            if details_chemo == "Follow-up required":
                plan_chemo, date_start_chemo, cyc_number, drug_cyc, drug_doses, drug_units, tox_type, tox_grade, \
                tox_treat, tox_response, tox_cycle, change_tox,chemo_response_by, chemo_response, chemo_size, \
                chemo_size_date, trast_chemo, trast_regime, trast_courses,date_complete, reason_incomplete, \
                hormone_therapy, therapy_type, therapy_duration, therapy_side, ovary_status, patient_wt, drug_freq\
                    = (details_chemo,)*28
            elif details_chemo == "Details Available":
                plan_chemo = input("What is the plan of Adjuvant Chemotherapy (for eg., "
                                   "4 cycles AC followed by 12 cycles Paclitaxel):")
                date_start_chemo = ask.check_date("Date of starting Adjuvant Chemotherapy: ")
                patient_wt = ask.check_number_input("Weight of patient at start of therapy (in kgs): ", 'Weight must '
                                                                                                        'be a number')
                check_wt = ask.ask_y_n("Is weight at any other time point mentioned in report?")
                while check_wt:
                    other_wt = input("Time point at which weight mentioned: ")
                    other_wt = other_wt + " " + input("Weight of patient at " + other_wt + ": ")
                    patient_wt = patient_wt + "; " + other_wt
                    check_wt = ask.ask_y_n("Is weight at any other time point mentioned in report "
                                                         "(with date, if given)?")
                drug_table = drug_table_enter(file_number, drug_table)
                data_drug = col_drug[1:]
                data_drug_list = []
                for index in data_drug:
                    data_drug = "; ".join(list(drug_table.loc[:, index]))
                    data_drug_list.append(data_drug)
                drug_cyc, cyc_number, drug_freq, drug_doses, drug_units = data_drug_list
                toxicity = tox_table(file_number, drug_cyc, toxicity)
                columns = col_tox
                tox_details = []
                for column in columns:
                    tox_detail = toxicity.loc[:, column].drop_duplicates()
                    tox_details.append(list(tox_detail))
                tox_details = ask.join_lists(tox_details, "; ")
                file_number_tox, drug_tox, tox_type, tox_grade, tox_treat, tox_response, tox_cycle, change_tox \
                    = tox_details
                trast_chemo = ask.ask_y_n("Trastuzumab used?")
                if trast_chemo:
                    trast_regime = ask.ask_option("Trastuzumab use was", ["Sequential", "Concurrent"])
                    trast_chemo = "Trastuzumab used"
                    trast_courses = ask.check_number_input("Number of courses of trastuzumab/herceptin taken: ",
                                                           'Enter number only')
                else:
                    trast_chemo, trast_regime, trast_courses, therapy_side = ("Trastuzumab not used", )*4
                date_complete = ask.check_date("Date of completion of Adjuvant Chemotherapy: ")
                complete_chemo = ask.ask_y_n("Was Adjuvant Chemotherapy completed as per schedule?")
                if complete_chemo:
                    reason_incomplete = "Adjuvant Chemotherapy completed as per schedule"
                else:
                    reason_incomplete = ask.ask_option("Reason for discontinuation",
                                                                     ["Toxicity", "Reluctance of patient",
                                                                      "Progression on chemotherapy",
                                                                      "Advised by treating doctor",
                                                                      "Death due to toxicity",
                                                                      "Death due to progressive disease",
                                                                      "Preferred treatment at another centre",
                                                                      "Death due to unrelated cause",
                                                                      "Patient was unable to afford treatment"])
                    reason_incomplete = "Adjuvant Chemotherapy incomplete: "+reason_incomplete
                menopause = ask.ask_option("Menopausal Status", ["Pre-menopausal", "Peri-menopausal",
                                                                               "Post-Menopausal", "Other"])
                if menopause in {"Pre-menopausal", "Peri-menopausal"}:
                    ovary_status = ask.ask_option("Status of ovarian function after Chemotherapy",
                                   ["Menses ongoing", "Amenorrhoea on Chemo", "Amenorrhoea post Chemotherapy"])
                else:
                    ovary_status = menopause
                #hormone_therapy, therapy_type, therapy_duration, therapy_side = hormone_therapy_chemo()
                hormone_therapy, therapy_type, therapy_duration, therapy_side = ('NA', )*4
            else:
                plan_chemo, date_start_chemo, cyc_number, drug_cyc, drug_doses, drug_units, drug_freq,tox_type, \
                tox_grade, tox_treat, tox_response, tox_cycle, change_tox,chemo_response_by, chemo_response, \
                chemo_size, chemo_size_date, trast_chemo, trast_regime, trast_courses, hormone_therapy,  therapy_type, \
                therapy_duration, therapy_side, date_complete, reason_incomplete,ovary_status, patient_wt \
                    = (details_chemo,)*28
        elif chemo == 'No':
            place_chemo, plan_chemo, date_start_chemo, cyc_number, drug_cyc, drug_doses, drug_units, \
            drug_freq,tox_type, tox_grade, tox_treat, tox_response, tox_cycle, change_tox, chemo_response_by, \
            chemo_response, chemo_size, chemo_size_date, trast_chemo, trast_regime, trast_courses, hormone_therapy, \
            therapy_type, therapy_duration, therapy_side, date_complete, reason_incomplete, details_chemo, chemo, \
            ovary_status, patient_wt = ("Adjuvant Chemotherapy not given",)*31
        else:
            place_chemo, plan_chemo, date_start_chemo, cyc_number, drug_cyc, drug_doses, drug_units, drug_freq, \
            tox_type, tox_grade, tox_treat, tox_response, tox_cycle, change_tox, chemo_response_by, chemo_response, \
            chemo_size, chemo_size_date, trast_chemo, trast_regime, trast_courses, hormone_therapy, therapy_type, \
            therapy_duration,ovary_status, therapy_side, date_complete, reason_incomplete, details_chemo, patient_wt \
                = (chemo,)*30
        data_list = [chemo, place_chemo, details_chemo, plan_chemo, date_start_chemo, patient_wt, drug_cyc, cyc_number,
                     drug_freq, drug_doses, drug_units, tox_type, tox_grade, tox_treat, tox_response, tox_cycle,
                     change_tox, reason_incomplete, date_complete, trast_chemo, trast_regime, trast_courses,
                     ovary_status, hormone_therapy, therapy_type, therapy_duration, therapy_side, user_name,
                     sql.last_update()]
        col_list = names("adjuvant_chemotherapy")
        check = sql.review_input(file_number, col_list, data_list)
    return data_list, drug_table, toxicity


def add_data(conn, cursor, file_number, user_name):
    table = "adjuvant_chemotherapy"
    data = chemotherapy(file_number, user_name)
    data_sql, drug_table, tox_response = data
    sql.update_multiple(conn, cursor, table, names(table), file_number, data_sql)
    drug_table.to_sql("chemo_drug_table", conn, index=False, if_exists="append")
    tox_response.to_sql("chemo_tox_table", conn, index=False, if_exists="append")


def edit_data(conn, cursor, file_number, user_name):
    table = "adjuvant_chemotherapy"
    enter = sql.review_data(conn, cursor, table, file_number, names(table))
    if enter:
        sql.delete_rows(cursor, 'chemo_drug_table', "file_number", file_number)
        sql.delete_rows(cursor, 'chemo_tox_table', "file_number", file_number)
        data = chemotherapy(file_number, user_name)
        data_sql, drug_table, tox_response = data
        sql.update_multiple(conn, cursor, table, names(table), file_number, data_sql)
        drug_table.to_sql("chemo_drug_table", conn, index=False, if_exists="append")
        tox_response.to_sql("chemo_tox_table", conn, index=False, if_exists="append")\

import helper_function.ask_y_n_statement as ask
from sql.add_update_sql import review_input, update_multiple, review_data, last_update
import helper_function.pccm_names as names
from datetime import datetime
from helper_function.option_lists import FollowUpStatus

def hormone (file_number):
    check = False
    while not check:
        hormone = ask.ask_y_n("Hormone therapy indicated?")
        if not hormone:
            hormone = "Hormone therapy not indicated"
            hormone_recieved, hormone_date, hormone_type, hormone_duration, hormone_disc, hormone_ovary,hormone_outcome, \
            hormone_follow_up, hormone_recur = ("NA", )*9
        else:
            hormone = "Hormone therapy indicated"
            hormone_recieved = ask.ask_y_n("Was Hormone therapy recieved?")
            if hormone_recieved:
                hormone_recieved = "Hormone therapy recieved"
                hormone_date = ask.check_date("Date of starting hormone therapy: ")
                hormone_type = ask.ask_option("Type of hormone therapy", ["Tamoxifen", "Anastrazole",
                                                             "Injectables", "Letrozole", "Others"])
                if hormone_type == "Injectables":
                    details = input ("Please provide details of injectables recieved: ")
                    hormone_type = hormone_type +": "+ details
                hormone_duration = input("Duration of hormone therapy (years): ")
                hormone_disc = ask.ask_option("What is the current status of hormone therapy. "
                                                            "Give specific reasons if discontinued prematurely "
                                                            "(or not taken at all)",
                                                            ['Therapy is ongoing', "Completion of planned course",
                                                             "Adverse Effects","Stopped by patient",
                                                             "Progression of disease","Other"])
                ovary = ask.ask_y_n_na("Has ovarian surpression been used?")
                if ovary == 'Yes':
                    hormone_ovary = ask.ask_option("Type of ovarian surpression used", ["Surgery", "Drug"])
                    if hormone_ovary == "Drug":
                        details = input("Please provide details of drug used: ")
                        hormone_ovary = hormone_ovary + ": "+details
                else:
                    hormone_ovary = ovary
                hormone_outcome = input ("Outcome of hormone therapy: ")
                hormone_follow_up = input("Follow up after hormone therapy: ")
                hormone_recur = ask.ask_y_n("Was there recurrence after hormone therapy?", "Recurrence",
                                                          "No recurrence")
            else:
                hormone_recieved = "No hormone therapy recieved"
                hormone_date, hormone_type, hormone_duration, hormone_disc, hormone_ovary, hormone_outcome, \
                hormone_follow_up, hormone_recur = ("NA", )*8
        data_list = [hormone, hormone_recieved, hormone_date, hormone_type, hormone_duration, hormone_disc,
                     hormone_ovary,hormone_outcome, hormone_follow_up, hormone_recur]
        col_list = names.names_longterm("hormone")
        check = review_input(file_number, col_list, data_list)
    return data_list


def metastasis(file_number, user_name):
    check = False
    while not check:
        met_has = ask.ask_y_n("Has the patient been examined for metastatic disease?")
        if not met_has:
            met_has = "Not examined for metastatic disease"
        else:
            met_has = "Examined for metastatic disease"
        date_last = ask.check_date("Date of last follow-up: ")
        recur = ask.ask_y_n("Has the patient experienced a recurrence?")
        if recur:
            time_recur = input("Time to disease recurrence: ")
            nature_recur = ask.ask_option("Nature of recurrence", ["Distant", "Local", "Other"])
            if nature_recur == "Distant":
                distant_site = input("Site of distant recurrence: ")
            else:
                distant_site = "NA"
        else:
            time_recur, nature_recur, distant_site = ("NA", )*3
        status = patient_status()
        data_list = [met_has, date_last, time_recur, nature_recur,
        distant_site, status, user_name, last_update()]
        col_list = names.names_longterm("metastasis")
        check = review_input(file_number, col_list, data_list)
    return data_list


def patient_status():
    status = ask.ask_option("Status at last follow up",
                                          ["Survivor", "Deceased", "Lost to follow-up", 'Case of Non Malignant Breast Disease',"Other"])
    if status == "Survivor":
        type_survivor = ask.ask_list("the Survivor is ", FollowUpStatus.survivor_status)
        status = status + ": " + type_survivor
    if status == "Deceased":
        type_death = ask.ask_option("Cause of death", FollowUpStatus.deceased_status)
        status = status + ": " + type_death
    return status


def file_row(cursor, file_number):
    cursor.execute("INSERT INTO HormoneTherapy_Recurrence_Survival(File_number) VALUES ('" + file_number + "')")


def add_data(conn, cursor, file_number, user_name):
    #file_row(cursor, file_number)
    table = "hormonetherapy_survival"
    enter = ask.ask_y_n("Enter Hormone Therapy Details?")
    if enter:
        col_list = names.names_longterm(module_name= "hormone")
        data = hormone(file_number)
        update_multiple(conn, cursor, table, col_list, file_number, data)
    enter = ask.ask_y_n("Enter Recurrence and follow-up status?")
    if enter:
        col_list = names.names_longterm(module_name="metastasis")
        data = metastasis(file_number, user_name)
        update_multiple(conn, cursor, table, col_list, file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "hormonetherapy_survival"
    print("Hormone Therapy Details")
    col_list = names.names_longterm(module_name="hormone")
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = hormone(file_number)
        update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Recurrence and follow-up status")
    col_list = names.names_longterm(module_name="metastasis")
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = metastasis(file_number, user_name)
        update_multiple(conn, cursor, table, col_list, file_number, data)

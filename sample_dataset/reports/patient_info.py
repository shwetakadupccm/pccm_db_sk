import sample_dataset.additional_rnd_tables.breast_cancer_tables as bct
import sql.add_update_sql as sql
# from add_edit.print_gen_info import print_info
import helper_function.pccm_names as pccm_names
from sample_dataset.additional_rnd_tables.radio_tables import clinical_tests
from helper_function.option_lists import PatientInfo
import sample_dataset.general_functions as gf
import numpy as np
import random
from datetime import datetime
import names
import sqlite3
import os
from helper_function.ask_y_n_statement import default_data_list


def nut_supplements(file_number):
    module_name = "nut_supplements"        
    nut_supplements = gf.get_yes_no_na()
    if nut_supplements == 'yes':
        nuts = bct.nut_supp_table(file_number)
        nut_supplements = "Nutritional supplements taken"
    elif nut_supplements == 'no':
        nut_supplements = "No nutritional supplements taken"
        nuts = ("No nutritional supplements taken",) * 3
    else:
        nuts = (nut_supplements,) * 3
    nuts_type, nuts_quant, nuts_dur = nuts
    data_list = [nut_supplements, nuts_type, nuts_quant, nuts_dur]
    columns_list = pccm_names.names_info(module_name)
    return (tuple(data_list))


def phys_act(file_number):
    module_name = "phys_act"
    phys_act = gf.get_yes_no_na()
    if phys_act == 'yes':
        phys = bct.physical_activity_table(file_number)
        phys_act = "Physical Activities Performed"
        phys_act_done, phys_act_freq = phys
    elif phys_act == 'no':
        phys_act = "No Physical Activities"
        phys_act_done, phys_act_freq = ("No Physical Activities",) * 2
    else:
        phys_act_done, phys_act_freq = (phys_act, ) * 2
    data_list = [phys_act, phys_act_done, phys_act_freq]
    columns_list = pccm_names.names_info(module_name)
    return (tuple(data_list))


def med_history(file_number):
    module_name = "med_history"
    medical_history_y_n = gf.get_yes_no_na()
    if medical_history_y_n == 'yes':
        med_hist = bct.med_history_table(file_number)
        medical_history_y_n = "Previous medical history present"
    elif medical_history_y_n == 'no':
        medical_history_y_n = "No previous medical history present"
        med_hist = ("No previous medical history present",) * 3
    else:
        med_hist = (medical_history_y_n,) * 3
    condition_hist, diagnosis_date_hist, treatment_hist = med_hist
    data_list = [medical_history_y_n, condition_hist, diagnosis_date_hist,
                 treatment_hist]
    columns_list = pccm_names.names_info(module_name)
    return (tuple(data_list))


def cancer_history(file_number):
    module_name = "cancer_history"
    previous_cancer_history_y_n = gf.get_yes_no_na()
    if previous_cancer_history_y_n == 'yes':
        previous_cancer = bct.cancer_table(file_number)
        previous_cancer_history_y_n = "Previous history of cancer"
    elif previous_cancer_history_y_n == 'no':
        previous_cancer_history_y_n = "No previous history of cancer"
        previous_cancer = ("No previous history of cancer",) * 5
    else:
        previous_cancer = (previous_cancer_history_y_n,) * 5
    type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all = previous_cancer
    data_list = [previous_cancer_history_y_n, type_of_cancer_list, year_diagnosis_list, treat_all,
                 type_all, duration_all]
    return (tuple(data_list))


def family_details(file_number, age_mother):
    module_name = "family_details"
    col_list = pccm_names.names_info(module_name)
    marital_status = 'data_not_available'
    siblings = gf.get_yes_no_na()
    if siblings == 'yes':
        siblings_number = gf.get_number(5)
        sisters = gf.get_number(siblings_number)
        brothers = siblings_number - sisters
    elif siblings == 'no':
        siblings_number, sisters, brothers = "No Siblings", "0", "0"
    else:
        siblings_number, sisters, brothers = (siblings,)*3
    children_y_n = gf.get_yes_no_na()
    if children_y_n == 'yes':
        children_number = gf.get_number(5)
        daughters = gf.get_number(children_number)
        sons = children_number - daughters
    elif children_y_n == 'no':
        children_number, daughters, sons = 0,0,0
    else:
        children_number, daughters, sons = (children_y_n,)*3
    menarche = gf.get_number_lt(11, 20)
    menopause = gf.get_choice(PatientInfo.menopause_status)
    menopause_age = menopause
    if menopause == "Post-Menopausal":
        menopause_age = gf.get_number_lt(menarche, 60)
        lmp = "Last menstrual period " + str(menopause_age) + " yrs"
    else:
        lmp = gf.gen_date(base_date='2020-01-01')
    # category = "Type of Period"
    options = ["Regular", "Irregular", "Other"]
    period_type = gf.get_choice(options)
    number_pregnancy = gf.get_number(8)
    if number_pregnancy == "0":
        age_first_preg = 'No children'
        age_last_preg = 'No children'
        number_term = 'No children'
        number_abortion = 'No children'
        age_first = 'No children'
        age_last = 'No children'
        twice_birth = 'No children'
        breast_feeding_data = 'No children'
        kid_feeding = 'No children'
        duration_feeding = 'No children'
        breast_usage = 'No children'
    elif number_pregnancy == "Requires Follow-up":
        age_first_preg = number_pregnancy
        age_last_preg = number_pregnancy
        number_term = number_pregnancy
        number_abortion = number_pregnancy
        age_first = number_pregnancy
        age_last = number_pregnancy
        twice_birth = number_pregnancy
        breast_feeding_data = number_pregnancy
        kid_feeding = number_pregnancy
        duration_feeding = number_pregnancy
        breast_usage = number_pregnancy
    else:
        number_term = gf.get_number(5)
        number_abortion = gf.get_number(5)
        age_first_preg = gf.get_number_lt(menarche, 55)
        age_last_preg = "NA"
        age_first = gf.get_number_lt(0, age_mother)
        age_last = age_first
        if children_number == 0:
            age_first = children_number
            age_last = children_number
            twice_birth = children_number
            breast_feeding_data = children_number
            kid_feeding = children_number
            duration_feeding = children_number
            breast_usage = children_number
        elif children_y_n == 'yes':
            age_first = gf.get_number_lt(0, age_mother)
            if age_first_preg == "NA":
                age_first_preg = int(age_mother) - int(age_first)
            if int(children_number) > 1:
                age_last = gf.get_number_lt(0, age_first_preg)
                age_last_preg = age_mother - age_last
                if age_last_preg == "NA":
                    age_last_preg = str(int(age_mother) - int(age_last))
                twice_birth = gf.get_choice(["Two births in a year",
                                             "No two births in a year"])
            else:
                age_last = age_first
                age_last_preg = 'NA'
                twice_birth = "NA"
            breast_feeding = gf.get_bool()
            if breast_feeding:
                breast_feeding_data = "Breast feeding"
                feed_details = bct.feed_duration(file_number, children_number)
            else:
                breast_feeding_data = "No Breast feeding"
                feed_details = ("NA",) * 3
            kid_feeding, duration_feeding, breast_usage = feed_details
        else:
            age_first = str(children_y_n)
            age_last = str(children_y_n)
            twice_birth = str(children_y_n)
            breast_feeding_data = str(children_y_n)
            kid_feeding = str(children_y_n)
            duration_feeding = str(children_y_n)
            breast_usage = str(children_y_n)
    fert_treat_y_n = gf.get_yes_no()
    if fert_treat_y_n == 'yes':
        fert_treat = "Fertility Treatment used"
        type_fert = gf.get_choice(PatientInfo.fert_treat)
        detail_fert = 'data_not_available'
        cycles_fert = gf.get_number_lt(1, 4)
        success_fert = gf.get_choice(["Pregnancy from Treatment",
                                      "No pregnancy from treatment"])
    elif fert_treat_y_n == "no":
        fert_treat = "No Fertility Treatment used"
        type_fert = fert_treat
        detail_fert = fert_treat
        cycles_fert = fert_treat
        success_fert = fert_treat
    else:
        fert_treat = str(fert_treat_y_n)
        type_fert = str(fert_treat_y_n)
        detail_fert = str(fert_treat_y_n)
        cycles_fert = str(fert_treat_y_n)
        success_fert = str(fert_treat_y_n)
    birth_control = gf.get_yes_no_na()
    if birth_control == 'yes':
        type_birth_control = gf.get_choice(["Birth control pills",
                                            "Copper-T", "Condom"])
        detail_birth_control = 'data_not_available'
        duration_birth_control = gf.get_number(max_no=age_mother)
    elif birth_control == 'no':
        type_birth_control = "No birth control used"
        detail_birth_control = "No birth control used"
        duration_birth_control ="No birth control used" * 3
    else:
        type_birth_control = birth_control
        detail_birth_control = birth_control
        duration_birth_control = birth_control
    data_list = [marital_status, siblings_number, sisters, brothers,
                 children_number, daughters, sons, menarche, menopause,
                 menopause_age, lmp, period_type, number_pregnancy,
                 number_term, number_abortion, age_first, age_first_preg,
                 age_last, age_last_preg, twice_birth, breast_feeding_data,
                 kid_feeding, duration_feeding, breast_usage, fert_treat,
                 type_fert, detail_fert, cycles_fert, success_fert,
                 type_birth_control, detail_birth_control,
                 duration_birth_control]
    return tuple(data_list)


def breast_symptoms(file_number, user_name):
    module_name = "breast_symptoms" 
    symp_present = gf.get_bool()
    if symp_present:
        rb_symp_list = []
        rb_dur_list = []
        lb_symp_list = []
        lb_dur_list = []
        for index in PatientInfo.symp_state:
            symp = gf.get_bool()
            if symp:
                RB = gf.get_bool()
                if RB:
                    rb_symp = index
                    rb_dur = str(gf.get_number(5)) + gf.get_choice(['weeks', 'year', 'months', 'days'])
                    rb_symp_list.append(rb_symp)
                    rb_dur_list.append(rb_dur)
                LB = gf.get_bool()
                if LB:
                    lb_symp = index
                    lb_dur = str(gf.get_number(5)) + gf.get_choice(['weeks', 'year', 'months', 'days'])
                    lb_symp_list.append(lb_symp)
                    lb_dur_list.append(lb_dur)
        rb_symps = "; ".join(rb_symp_list)
        rb_duration = "; ".join(rb_dur_list)
        lb_symps = "; ".join(lb_symp_list)
        lb_duration = "; ".join(lb_dur_list)
        data_list_symp = [rb_symps, rb_duration, lb_symps, lb_duration]
        for index in range(0, len(data_list_symp)):
            if data_list_symp[index] == '':
                data_list_symp[index] = "NA"
        rb_symp_list = []
        rb_dur_list = []
        lb_symp_list = []
        lb_dur_list = []
        rb_symps_other = "; ".join(rb_symp_list)
        rb_duration_other = "; ".join(rb_dur_list)
        lb_symps_other = "; ".join(lb_symp_list)
        lb_duration_other = "; ".join(lb_dur_list)
        data_list_other = [rb_symps_other, rb_duration_other,
                           lb_symps_other, lb_duration_other]
        for index in range(0, len(data_list_other)):
            if data_list_other[index] == '':
                data_list_other[index] = "NA"
        met = []
        for symptom in PatientInfo.met_symptoms:
            met_symp = gf.get_bool()
            if met_symp:
                met.append([symptom])
        met_flat = [item for sublist in met for item in sublist]
        data_met = "; ".join(met_flat)
        if met_flat == []:
            data_met = "No Metastatis Symptoms"
    else:
        data_list_other = ["Symptoms at presentation not in report", ] * 4
        data_list_symp = ["Symptoms at presentation not in report", ] * 4
        data_met = "Symptoms at presentation not in report"
    columns_list = pccm_names.names_info(module_name)
    data_list = data_list_symp + data_list_other + [data_met]
    return tuple(data_list)


def habits(file_number, age):
    module_name = "habits"
    diet = gf.get_choice(PatientInfo.diet)
    alcohol = gf.get_yes_no_na()
    if alcohol == 'yes':
        alcohol_consump = "Alcohol Consumption"
        alcohol_age = gf.get_number_lt(21, age)
        alcohol_quant = gf.get_number_lt(1, 10)
        alcohol_duration = gf.get_choice(PatientInfo.frequency)
        alcohol_comments = 'na'
    elif alcohol == 'no':
        alcohol_consump = "No Alcohol Consumption"
        alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments = ("No Alcohol Consumption",) * 4
    else:
        alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments = (alcohol,) * 5
    data_list_alc = [diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments]
    tobacco = gf.get_yes_no_na()
    if tobacco == 'yes':
        tobacco = "Tobacco consumption"
        exposure_type = gf.get_choice(PatientInfo.tobacco_exposure)
        if exposure_type == "Passive":
            tobacco_type_partic = gf.get_choice(PatientInfo.passive_tobacco)
            if tobacco_type_partic == "Home":
                tobacco_type_who = 'family member'
                tobacco_passive = tobacco_type_partic + (" : ") + tobacco_type_who

            else:
                tobacco_passive = tobacco_type_partic
        else:
            tobacco_passive = "NA"
        tobacco_type = gf.get_choice(PatientInfo.type_tobacco)
        tobacco_age = gf.get_number_lt(15, age)
        tobacco_freq = gf.get_choice(PatientInfo.frequency)
        tobacco_quant = gf.get_number(5)
        tobacco_duration = age - tobacco_age
        tobacco_comments = 'na'
    elif tobacco == 'no':
        tobacco = "No Tobacco Consumption"
        exposure_type, tobacco_type, tobacco_passive, tobacco_age, tobacco_freq, tobacco_quant, tobacco_duration, \
        tobacco_comments = ("No Tobacco Consumption",) * 8
    else:
        exposure_type, tobacco_type, tobacco_passive, tobacco_age, tobacco_freq, tobacco_quant, tobacco_duration, \
        tobacco_comments = (tobacco,) * 8
    other_del_habits = 'na'
    data_list_tob = [tobacco, exposure_type, tobacco_passive, tobacco_type, tobacco_age, tobacco_freq,
                     tobacco_quant, tobacco_duration, tobacco_comments, other_del_habits]
    data_list = data_list_alc + data_list_tob
    return tuple(data_list)


def det_by(file_number):
    module_name = "det_by"
    options = ["Self", "Physician", "Screening Camp", "Other"]
    determined_by = gf.get_choice(options)
    if determined_by == "Screening Camp":
        sc_id = gf.get_number(5)
        determined_by = "Screening Camp ID " + str(sc_id)
    det_date = gf.gen_date(datetime.now().strftime("%Y-%m-%d"))
    data_list = [determined_by, det_date]
    return (tuple(data_list))


def family_cancer(file_number):
    module_name = "family_cancer"
    family_cancer_history_y_n = gf.get_yes_no_na()
    if family_cancer_history_y_n == 'yes':
        family_cancer = bct.family_cancer_table(file_number)
        family_cancer_history_y_n = "Family History of Cancer"
    elif family_cancer_history_y_n == 'no':
        family_cancer_history_y_n = "No Family History of Cancer"
        family_cancer = "No Family History of Cancer"
    else:
        family_cancer = family_cancer_history_y_n
    data_list = [family_cancer_history_y_n, family_cancer]
    columns_list = pccm_names.names_info(module_name)
    return (tuple(data_list))


def other_test(file_number, user_name):
    data_list = ['data_to_be_entered', ]*14 + [user_name, sql.last_update()]
    module_name = "other_test"
    data = clinical_tests()
    data_list = data + [user_name, sql.last_update()]
    return data_list


def bio_info(file_number):
    module_name = "bio_info"  
    mr_number = gf.get_number_lt(500, 2000)
    name = names.get_full_name(gender='female')
    aadhaar_card = 'data_not_available'
    date_first = gf.gen_date(base_date='2010-12-12')
    permanent_address = 'data_not_available'
    current_address = permanent_address
    phone = gf.get_number_lt(900000000, 999999999)
    email_id = 'data_not_available'
    gender = gf.get_choice(["Female", "Male"])
    date_of_birth = gf.get_dob()
    age_yrs = gf.get_age(date_of_birth)
    age_diag = gf.get_years(date_of_birth, date_first)
    place_birth = 'data_not_available'
    height_cm = gf.get_number_lt(140, 180)
    weight_kg = gf.get_number_lt(50, 90)
    weight = float(weight_kg)
    height = float(height_cm) / 100
    bmi = str(round(weight / (height * height)))
    columns_list = pccm_names.names_info(module_name)
    new_data = [mr_number, name, aadhaar_card, date_first, permanent_address,
                current_address, phone, email_id, gender, age_yrs,
                age_diag, date_of_birth, place_birth, height_cm, weight_kg,
                bmi]
    return (age_diag, tuple(new_data))


def add_gen_info(conn, cursor, file_number, user_name):
    table = "patient_information_history"
    sql.add_pk_fk_to_table(conn, cursor, table=table, col_name='file_number', pk=file_number)
    age, data = bio_info(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("bio_info"),
                    file_number, data)
    data = phys_act(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("phys_act"),
                    file_number, data)
    data = habits(file_number, age)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("habits"),
                    file_number, data)
    data = nut_supplements(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                        pccm_names.names_info("nut_supplements"),
                        file_number, data)
    data = family_details(file_number, age)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("family_details"),
                    file_number, data)
    data = med_history(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("med_history"),
                    file_number, data)
    data = cancer_history(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("cancer_history"),
                    file_number, data)
    data = family_cancer(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("family_cancer"),
                    file_number, data)
    data = det_by(file_number)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table, pccm_names.names_info("det_by"),
                    file_number, data)
    data = breast_symptoms(file_number, user_name)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("breast_symptoms"),
                    file_number, data)
    data = other_test(file_number, user_name)
    data = [str(dat) for dat in data]
    sql.update_multiple(conn, cursor, table,
                    pccm_names.names_info("other_test"),
                    file_number, data)


def gen_sample():
    file = 'PCCM_DB_2021_02_25.db'
    folder = 'd:/repos/pccm_db/main/DB'
    conn = sqlite3.connect(os.path.join(folder, file))
    cursor = conn.cursor()
    file_number = gf.get_file_id()
    user_name = 'dk'
    add_gen_info(conn, cursor, file_number, user_name)

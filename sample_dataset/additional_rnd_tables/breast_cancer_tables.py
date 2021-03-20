import helper_function.pccm_names as pccm_names
from helper_function.option_lists import PatientInfo
# from faker import Faker
import sample_dataset.general_functions as gf
from datetime import datetime
from helper_function.ask_y_n_statement import join_lists


def physical_activity_table(file_number):
# def physical_activity_table(file_number):
    table_act = "physical_activity"
    columns = ", ".join(pccm_names.names_info("phys_act_table"))
    type_phys_list, freq_phys_list = [], []
    type_phys_act = gf.get_choice(options=PatientInfo.phys_act)
    type_phys_list.append(type_phys_act)
    freq_phys_act = gf.get_choice(options=PatientInfo.frequency)
    freq_phys_list.append(freq_phys_act)
    type_phys_act = gf.get_choice(options=PatientInfo.phys_act)
    type_phys_list.append(type_phys_act)
    freq_phys_act = gf.get_choice(options=PatientInfo.frequency)
    freq_phys_list.append(freq_phys_act)
    type_phys = '; '.join(type_phys_list)
    freq_phys = '; '.join(freq_phys_list)
    return (type_phys, freq_phys)


def cancer_table(file_number):
    table_cancer = "previous_cancer_history"
    type_of_cancer_list = []
    year_diagnosis_list = []
    treat_all = []
    type_all = []
    duration_all = []
    data_return = []
    type_of_cancer = 'data_not_available'
    type_of_cancer_list.append(type_of_cancer)
    year_diagnosis = 'data_not_available'
    year_diagnosis_list.append(year_diagnosis)
    col = ("File_number, Type_Cancer, Year_diagnosis")
    treat_list = []
    type_list = []
    duration_list = []
    treated, type, duration = ("NA", )*3
    for treatment in PatientInfo.previous_cancer_treatment:
        treat = gf.get_bool()
        if treat:
            treat_list.append(treatment)
            type_treat = 'data_not_available'
            type_list.append(type_treat)
            duration_treat = 'data_not_available'
            duration_list.append(duration_treat)
            data = treatment, type_treat, duration_treat
            columns = [treatment, ("type_" + treatment),
                       ("duration_" + treatment)]
            treated = "; ".join(treat_list)
            type = "; ".join(type_list)
            duration = "; ".join(duration_list)
        elif not treat:
            index_no = "No " + treatment
            type_treat, duration_treat = ("NA",) * 2
            data = index_no, type_treat, duration_treat
            columns = [treatment, ("type_" + treatment),
                       ("duration_" + treatment)]
        treat_all.append(treated)
        type_all.append(type)
        duration_all.append(duration)
    all_data = [type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all]
    for index in all_data:
        data_joint = "|".join(index)
        data_return.append(data_joint)
    return tuple(data_return)


def nut_supp_table(file_number):
    type_nut_list, quant_nut_list, duration_nut_list = [], [], []
    add_supp = True
    table_nut = "nutritional_supplements"
    columns = ", ".join(pccm_names.names_info("nut_sup"))
    nut_supplements_type = 'data_not_available'
    type_nut_list.append(nut_supplements_type)
    nut_supplements_quant = str(gf.get_number(1000))
    quant_nut_list.append(nut_supplements_quant)
    nut_supplements_duration = str(gf.get_number(4))
    duration_nut_list.append(nut_supplements_duration)
    type_nut = '; '.join(type_nut_list)
    quant_nut = '; '.join(quant_nut_list)
    duration_nut = "; ".join(duration_nut_list)
    return (type_nut, quant_nut, duration_nut)


def med_history_table(file_number):
    add_history = True
    diagnosis_date_list, treatment_list, condition_list = [], [], []
    condition = 'data_not_available'
    condition_list.append(condition)
    diagnosis_date = gf.gen_date(datetime.today().strftime('%Y-%m-%d'))
    diagnosis_date_list.append(diagnosis_date)
    treatment = 'data_not_available'
    treatment_list.append(treatment)
    condition_hist = '; '.join(condition_list)
    treatment_hist = '; '.join(treatment_list)
    diagnosis_date_hist = "; ".join(diagnosis_date_list)
    return (condition_hist, diagnosis_date_hist, treatment_hist)


def family_cancer_table(file_number):
    type_cancer_list, relation_degree_list, type_relation_list, age_detect_list = [], [], [], []
    all_data = []
    type_of_cancer = 'data_not_available'
    type_cancer_list.append(type_of_cancer)
    relation_to_patient = gf.get_choice(PatientInfo.family)
    relation_degree_list.append(relation_to_patient)
    type_relation = 'data_not_available'
    type_relation_list.append(type_relation)
    age_at_detection_yrs = str(gf.get_number_lt(15, 80))
    age_detect_list.append(age_at_detection_yrs)
    family_history = file_number, type_of_cancer, relation_to_patient, type_relation, age_at_detection_yrs
    family_history_list = "; ".join([type_of_cancer, relation_to_patient, type_relation, age_at_detection_yrs])
    all_data.append(family_history_list)
    all_data_flat = "|".join(all_data)
    return(all_data_flat)


def feed_duration(file_number, children_number):
    table = "breast_feeding"
    child_list, feeding_duration_list, feeding_details_list = [], [], []
    child_number = int(children_number)
    for index in range(0, child_number):
        kid = str(index+1)
        kid_add = "Child "+ kid
        child_list.append(kid_add)
        feeding_duration = str(gf.get_number_lt(1, 36))
        feeding_duration_list.append(feeding_duration)
        feeding_details = gf.get_choice(PatientInfo.breast_feeding)
        feeding_details_list.append(feeding_details)
    data_list = [child_list, feeding_duration_list, feeding_details_list]
    data_return = join_lists(data_list, "; ")
    return (data_return)

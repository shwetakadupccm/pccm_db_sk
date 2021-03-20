from additional_tables.breast_cancer_tables import nut_supp_table, physical_activity_table, med_history_table, \
    cancer_table, feed_duration, family_cancer_table
from sql.add_update_sql import review_input, update_multiple, review_data, last_update
from helper_function.ask_y_n_statement import ask_option, ask_y_n, ask_y_n_na, check_date
import helper_function.pccm_names as pccm_names
from additional_tables.radio_tables import clinical_tests
from helper_function.option_lists import PatientInfo


# noinspection SqlNoDataSourceInspection
class GenInfo:

    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name

    def nut_supplements(self):
        module_name = "nut_supplements"
        data_list = ['NA'] *4
        check = False
        while not check:
            nutrition = ask_y_n_na("Nutritional supplements taken")
            if nutrition == 'Yes':
                nuts = nut_supp_table(self.conn, self.cursor, self.file_number)
                nutrition = "Nutritional supplements taken"
            elif nutrition == 'No':
                nutrition = "No nutritional supplements taken"
                nuts = ("No nutritional supplements taken",) * 3
            else:
                nuts = (nutrition,) * 3
            nuts_type, nuts_quant, nuts_dur = nuts
            data_list = [nutrition, nuts_type, nuts_quant, nuts_dur]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def phys_act(self):
        module_name = "phys_act"
        check = False
        data_list = ['NA'] * 3
        while not check:
            activity = ask_y_n_na("Any Physical Activities ?")
            if activity == 'Yes':
                phys = physical_activity_table(self.conn, self.cursor, self.file_number)
                activity = "Physical Activities Performed"
                phys_act_done, phys_act_freq = phys
            elif activity == 'No':
                activity = "No Physical Activities"
                phys_act_done, phys_act_freq = ("No Physical Activities",) * 2
            else:
                phys_act_done, phys_act_freq = (activity,) * 2
            data_list = [activity, phys_act_done, phys_act_freq]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def med_history(self):
        module_name = "med_history"
        check = False
        while not check:
            medical_history_y_n = ask_y_n_na("Any Other Medical History ?")
            if medical_history_y_n == 'Yes':
                med_hist = med_history_table(self.conn, self.cursor, self.file_number)
                medical_history_y_n = "Previous medical history present"
            elif medical_history_y_n == 'No':
                medical_history_y_n = "No previous medical history present"
                med_hist = ("No previous medical history present",) * 3
            else:
                med_hist = (medical_history_y_n,) * 3
            condition_hist, diagnosis_date_hist, treatment_hist = med_hist
            data_list = [medical_history_y_n, condition_hist, diagnosis_date_hist, treatment_hist]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def cancer_history(self):
        module_name = "cancer_history"
        data_list = ['NA']*6
        check = False
        while not check:
            previous_cancer_history_y_n = ask_y_n_na("Previous history of cancer ?")
            if previous_cancer_history_y_n == 'Yes':
                previous_cancer = cancer_table(self.conn, self.cursor, self.file_number)
                previous_cancer_history_y_n = "Previous history of cancer"
            elif previous_cancer_history_y_n == 'No':
                previous_cancer_history_y_n = "No previous history of cancer"
                previous_cancer = ("No previous history of cancer",) * 5
            else:
                previous_cancer = (previous_cancer_history_y_n,) * 5
            type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all = previous_cancer
            data_list = [previous_cancer_history_y_n, type_of_cancer_list, year_diagnosis_list, treat_all,
                         type_all, duration_all]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def family_details(self):
        module_name = "family_details"
        check = False
        while not check:
            marital_status = input('Marital Status :')
            siblings = ask_y_n_na('Siblings', na_ans='data_not_available')
            if siblings == 'Yes':
                siblings_number = input("Number of siblings: ")
                sisters = input('Sisters :')
                brothers = input('Brothers :')
            elif siblings == 'No':
                siblings_number, sisters, brothers = "No Siblings", "0", "0"
            else:
                siblings_number, sisters, brothers = (siblings,)*3
            children_y_n = ask_y_n_na('Children', na_ans='data_not_available')
            if children_y_n == 'Yes':
                children_number = input("Number of children: ")
                daughters = input('Daughters :')
                sons = input('Sons :')
            elif children_y_n == 'No':
                children_number, daughters, sons = "No Children", "0", "0"
            else:
                children_number, daughters, sons = (children_y_n,)*3
            menarche = input('Age at menarche (yrs): ')
            menopause = ask_option("Menopausal Status", PatientInfo.menopause_status)
            menopause_age = menopause
            if menopause == "Post-Menopausal":
                menopause_age = input('Age at menopause (yrs): ')
                lmp = "Last menstrual period " + menopause_age + " yrs"
            else:
                lmp = check_date("Date of last menstrual period: ")
            period_type = ask_option("Type of Period", PatientInfo.menstrual_type)
            number_pregnancy = input("Number of pregnancies (enter Requires Follow-up if no data given): ")
            if number_pregnancy == "0":
                age_first_preg, age_last_preg, number_term, number_abortion, age_first, age_last, twice_birth, \
                breast_feeding_data, kid_feeding, duration_feeding, breast_usage = ('No children',) * 11
            elif number_pregnancy == "Requires Follow-up":
                age_first_preg, age_last_preg, number_term, number_abortion, age_first, age_last, twice_birth, \
                breast_feeding_data, kid_feeding, duration_feeding, breast_usage = ('Requires Follow-up',) * 11
            else:
                number_term = input("Pregnancy carried to term (include abortion after 6 months): ")
                number_abortion = input("Number of abortions: ")
                age_first_preg = input("Age at first pregnancy: ")
                age_last_preg = "NA"
                try:
                    sql = ("SELECT age_at_first_visit_yrs FROM patient_information_history WHERE File_number = \'" +
                           self.file_number + "'")
                    self.cursor.execute(sql)
                    age = self.cursor.fetchall()
                    age_mother = age[0][0]
                except:
                    age_mother = input("Age at first visit to clinic")
                if children_number == 'No Children':
                    age_first, age_last, twice_birth, breast_feeding_data, kid_feeding,  duration_feeding, \
                    breast_usage = (children_number,) * 7
                elif children_y_n == 'Yes':
                    age_first = input("Age of first child: ")
                    if age_first_preg == "NA":
                        age_first_preg = str(int(age_mother) - int(age_first))
                    if int(children_number) > 1:
                        age_last = input("Age of last child: ")
                        age_last_preg = input("Age at last pregnancy: ")
                        if age_last_preg == "NA":
                            age_last_preg = str(int(age_mother) - int(age_last))
                        twice_birth = ask_y_n("Two births in a year (not twins)", "Two births in a year",
                                              "No two births in a year")
                    else:
                        age_last = age_first
                        age_last_preg, twice_birth = ("NA", )*2
                    breast_feeding = ask_y_n("Breast feeding?")
                    if breast_feeding:
                        breast_feeding_data = "Breast feeding"
                        feed_details = feed_duration(self.conn, self.cursor, self.file_number, children_number)
                    else:
                        breast_feeding_data = "No Breast feeding"
                        feed_details = ("NA",) * 3
                    kid_feeding, duration_feeding, breast_usage = feed_details
                else:
                    age_first, age_last, twice_birth, breast_feeding_data, kid_feeding, duration_feeding, \
                    breast_usage = (children_y_n,) * 7
            fert_treat_y_n = ask_y_n_na("Have any fertility treatments ever been used")
            if fert_treat_y_n == 'Yes':
                fert_treat = "Fertility Treatment used"
                type_fert = input("Type of fertility treatment used: ")
                detail_fert = input ("Details of fertility treatment used:")
                cycles_fert = input("Number of cycles of fertility treatment taken: ")
                success_fert = ask_y_n("Did fertility treatment result in successful pregnancy? ",
                                       "Pregnancy from Treatment", "No pregnancy from treatment")
            elif fert_treat_y_n== "No":
                fert_treat = "No Fertility Treatment used"
                type_fert, detail_fert, cycles_fert, success_fert = ("No Fertility Treatment used", ) * 4
            else:
                fert_treat, type_fert, detail_fert, cycles_fert, success_fert = (fert_treat_y_n, ) * 5
            birth_control = ask_y_n_na("Birth control used?")
            if birth_control == 'Yes':
                type_birth_control = ask_option("Type of birth control used", ["Birth control pills", "Other"])
                detail_birth_control = input("Details of birth control used: ")
                duration_birth_control = input("Duration of birth control use: ")
            elif birth_control == 'No':
                type_birth_control, detail_birth_control, duration_birth_control = ("No birth control used",) * 3
            else:
                type_birth_control, detail_birth_control, duration_birth_control = (birth_control,) * 3
            data_list = [marital_status, siblings_number, sisters, brothers, children_number, daughters, sons, menarche,
                         menopause, menopause_age, lmp, period_type, number_pregnancy, number_term,
                         number_abortion, age_first, age_first_preg, age_last, age_last_preg, twice_birth,
                         breast_feeding_data, kid_feeding, duration_feeding, breast_usage, fert_treat, type_fert,
                         detail_fert, cycles_fert, success_fert, type_birth_control, detail_birth_control,
                         duration_birth_control]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def breast_symptoms(self):
        module_name = "breast_symptoms"
        check = False
        while not check:
            symp_present = ask_y_n("Does the file include information on patient symptoms at presentations?")
            if symp_present:
                rb_symp_list = []
                rb_dur_list = []
                lb_symp_list = []
                lb_dur_list = []
                for index in PatientInfo.symp_state:
                    symp = ask_y_n("Is " + index + " present")
                    if symp:
                        rb = ask_y_n(index + " in Right Breast?")
                        if rb:
                            rb_symp = index
                            rb_dur = input("Duration of " + index + ": ")
                            rb_symp_list.append(rb_symp)
                            rb_dur_list.append(rb_dur)
                        lb = ask_y_n(index + " in Left Breast?")
                        if lb:
                            lb_symp = index
                            lb_dur = input("Duration of " + index + ": ")
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
                other_symptom = ask_y_n("Other Symptoms?")
                if other_symptom:
                    check = True
                    while check:
                        type = input("Other Symptoms type? ")
                        rb = ask_y_n(type + " in Right Breast?")
                        if rb:
                            rb_symp = type
                            rb_dur = input("Duration of " + type)
                            rb_symp_list.append(rb_symp)
                            rb_dur_list.append(rb_dur)
                        lb = ask_y_n(type + " in Left Breast?")
                        if lb:
                            lb_symp = type
                            lb_dur = input("Duration of " + type)
                            lb_symp_list.append(lb_symp)
                            lb_dur_list.append(lb_dur)
                        check = ask_y_n("Additional Symptoms?")
                rb_symps_other = "; ".join(rb_symp_list)
                rb_duration_other = "; ".join(rb_dur_list)
                lb_symps_other = "; ".join(lb_symp_list)
                lb_duration_other = "; ".join(lb_dur_list)
                data_list_other = [rb_symps_other, rb_duration_other, lb_symps_other, lb_duration_other]
                for index in range(0, len(data_list_other)):
                    if data_list_other[index] == '':
                        data_list_other[index] = "NA"
                met = []
                for symptom in PatientInfo.met_symptoms:
                    met_symp = ask_y_n("Is " + symptom + " present?")
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
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def habits(self):
        module_name = "habits"
        check = False
        while not check:
            diet = ask_option("Diet", PatientInfo.diet)
            alcohol = ask_y_n_na("Alcohol consumption", na_ans='data_not_available')
            if alcohol == 'Yes':
                alcohol_consump = "Alcohol Consumption"
                alcohol_age = input("Consumption of alcohol from which age (yrs): ")
                alcohol_quant = input("Quantity of alcohol consumed per week: ")
                alcohol_duration = input("Duration of alcohol consumption: ")
                alcohol_comments = input("Additional comments for alcohol consumption: ")
            elif alcohol == 'No':
                alcohol_consump = "No Alcohol Consumption"
                alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments = ("No Alcohol Consumption",) * 4
            else:
                 alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments = (alcohol,) * 5
            data_list_alc = [diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments]
            tobacco = ask_y_n_na("Tobacco exposure (Passive and/or Active)", na_ans='data_not_available')
            if tobacco == 'Yes':
                tobacco = "Tobacco consumption"
                exposure_type = ask_option("Mode of exposure to Tobacco", PatientInfo.tobacco_exposure)
                if exposure_type =="Passive":
                    tobacco_type_partic = ask_option("Mode of passive consumption", PatientInfo.passive_tobacco)
                    if tobacco_type_partic == "Home":
                        tobacco_type_who = input ("What is the specific source?")
                        tobacco_passive = tobacco_type_partic + (" : ") + tobacco_type_who

                    else:
                        tobacco_passive = tobacco_type_partic
                else:
                    tobacco_passive = "NA"
                tobacco_type = ask_option("Type of tobacco use", PatientInfo.type_tobacco)
                tobacco_age = input("Consumption of tobacco from which age (yrs): ")
                tobacco_freq = input ("Frequency of tobacco consumption: ")
                tobacco_quant = input("Quantity of tobacco consumed per week: ")
                tobacco_duration = input("Duration of tobacco consumption: ")
                tobacco_comments = input("Additional comments for tobacco consumption: ")
            elif tobacco == 'No':
                tobacco = "No Tobacco Consumption"
                exposure_type, tobacco_type, tobacco_passive, tobacco_age, tobacco_freq, tobacco_quant, \
                tobacco_duration, tobacco_comments = ("No Tobacco Consumption",) * 8
            else:
                exposure_type, tobacco_type, tobacco_passive, tobacco_age, tobacco_freq, tobacco_quant, \
                tobacco_duration, tobacco_comments = (tobacco,) * 8
            other_del_habits = input("Other Deleterious Habits (if present give details): ")
            data_list_tob = [tobacco, exposure_type, tobacco_passive,tobacco_type, tobacco_age, tobacco_freq,
                             tobacco_quant, tobacco_duration, tobacco_comments, other_del_habits]
            columns_list = pccm_names.names_info(module_name)
            data_list = data_list_alc + data_list_tob
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def det_by(self):
        module_name = "det_by"
        check = False
        while not check:
            category = "Current Breast Cancer Detected by"
            options = ["Self", "Physician", "Screening Camp", "Other"]
            determined_by = ask_option(category, options)
            if determined_by == "Screening Camp":
                sc_id = input("Screening Camp ID: ")
                determined_by = "Screening Camp ID " + sc_id
            det_date = check_date("Date of current breast cancer detection: ")
            columns_list =pccm_names.names_info(module_name)
            data_list = [determined_by, det_date]
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def family_cancer(self):
        module_name = "family_cancer"
        check = False
        while not check:
            family_cancer_history_y_n = ask_y_n_na('Cancer history in Family')
            if family_cancer_history_y_n == 'Yes':
                family_cancer = family_cancer_table(self.conn, self.cursor, self.file_number)
                family_cancer_history_y_n = "Family History of Cancer"
            elif family_cancer_history_y_n == 'No':
                family_cancer_history_y_n = "No Family History of Cancer"
                family_cancer = "No Family History of Cancer"
            else:
                family_cancer = family_cancer_history_y_n
            data_list = [family_cancer_history_y_n, family_cancer]
            columns_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, columns_list, data_list)
        return data_list

    def other_test(self):
        data_list = ['data_to_be_entered', ]*14 + [self.user_name, last_update()]
        module_name = "other_test"
        check = False
        while not check:
            print('In this module please enter data for tests done at the time of diagnosis before the start of '
                  'treatment')
            data = clinical_tests()
            data_list = data + [self.user_name, last_update()]
            col_list = pccm_names.names_info(module_name)
            check = review_input(self.file_number, col_list, data_list)
        return data_list

    def bio_info(self):
        module_name = "bio_info"
        new_data = ['NA'] * 16
        check = False
        while not check:
            mr_number = input('MR number :')
            name = input('Name :')
            aadhaar_card = input("Aadhaar card number (if available): ")
            date_first = check_date("Date of first visit: ")
            permanent_address = input('Permanent Address :')
            current_address_check = ask_option('Current Address', ["Same as Permanent", "Different"])
            if current_address_check == "Different":
                current_address = input("Current Address: ")
            else:
                current_address = permanent_address
            phone = input('Phone :')
            email_id = input('Email_ID :')
            gender = ask_option('Gender', ["Female", "Male", "Other"])
            age_yrs = input('Age at first visit (yrs) :')
            age_diag = input('Age at diagnosis (yrs): ')
            date_of_birth = check_date('Date of Birth (dd/mm/yyyy):')
            place_birth = input('Place of Birth :')
            height = ask_option("Height unit", ["cm", "feet/inches", "Height not available"])
            height_cm, height_feet, height_inch, weight, bmi = ['NA'] * 5
            if height == "Height not available":
                height_cm = "NA"
                weight_kg = input('Weight (kg) (if available else enter NA) :')
                bmi = "NA"
            else:
                if height == "cm":
                    height_cm = input('Height (cm) :')
                else:
                    height_feet = float(input("Height (feet)"))
                    height_inch = float(input("Height (inches)"))
                    height_inch = height_inch + 12 * height_feet
                    height_cm = height_inch * 2.54
                weight_kg = input('Weight (kg) (if available else enter NA) :')
                try:
                    weight = float(weight_kg)
                    height = float(height_cm) / 100
                    bmi = str(round(weight / (height * height)))
                except ValueError:
                    bmi = 'NA'
            columns_list = pccm_names.names_info(module_name)
            new_data = [mr_number, name, aadhaar_card, date_first, permanent_address, current_address, phone,
                        email_id, gender, age_yrs, age_diag, date_of_birth, place_birth, height_cm, weight_kg, bmi]
            check = review_input(self.file_number, columns_list, new_data)
        return new_data

    def add_gen_info(self):
        table = "patient_information_history"
        enter = ask_y_n("Enter Patient Biographical Information")
        if enter:
            data = self.bio_info()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("bio_info"), self.file_number, data)
        enter = ask_y_n("Enter Patient habits")
        if enter:
            data = self.phys_act()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("phys_act"), self.file_number, data)
            data = self.habits()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("habits"), self.file_number, data)
            data = self.nut_supplements()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("nut_supplements"), self.file_number,
                            data)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            data = self.family_details()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("family_details"), self.file_number,
                            data)
        enter = ask_y_n("Enter Patient medical history?")
        if enter:
            data = self.med_history()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("med_history"), self.file_number, data)
            data = self.cancer_history()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("cancer_history"), self.file_number,
                            data)
        enter = ask_y_n("Enter patient family cancer history")
        if enter:
            data = self.family_cancer()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("family_cancer"), self.file_number,
                            data)
        enter = ask_y_n("Enter Patient Symptoms?")
        if enter:
            data = self.det_by()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("det_by"), self.file_number, data)
            data = self.breast_symptoms()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("breast_symptoms"), self.file_number,
                            data)
        enter = ask_y_n('Enter other tests done for diagnosis/metastatic checkup? ')
        if enter:
            data = self.other_test()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("other_test"), self.file_number, data)

    def edit_data(self):
        table = "patient_information_history"
        print("Patient Biographical Information")
        col_list = pccm_names.names_info("bio_info")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data = self.bio_info()
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data)
        col_list = pccm_names.names_info("phys_act") + pccm_names.names_info("habits") + pccm_names.names_info(
            "nut_supplements")
        print("Patient habits")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data_phys = self.phys_act()
            data_hab = self.habits()
            data_nut = self.nut_supplements()
            data = data_phys + data_hab + data_nut
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data)
        print("Patient family and reproductive details")
        col_list = pccm_names.names_info("family_details")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data = self.family_details()
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data)
        print("Patient medical history")
        col_list = pccm_names.names_info("med_history") + pccm_names.names_info("cancer_history")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data_med = self.med_history()
            data_can = self.cancer_history()
            data = data_med + data_can
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data)
        print("Patient Family Cancer History")
        col_list = pccm_names.names_info("family_cancer")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data_fam = self.family_cancer()
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data_fam)
        print("Patient Symptoms")
        col_list = pccm_names.names_info("det_by") + pccm_names.names_info("breast_symptoms")
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data_det = self.det_by()
            data_symp = self.breast_symptoms()
            data = data_det + data_symp
            update_multiple(self.conn, self.cursor, table, col_list, self.file_number, data)
        print('Other tests for diagnosis/metastatic checkup')
        col_list = pccm_names.names_info('other_test')
        enter = review_data(self.conn, self.cursor, table, self.file_number, col_list)
        if enter:
            data = self.other_test()
            update_multiple(self.conn, self.cursor, table, pccm_names.names_info("other_test"), self.file_number, data)

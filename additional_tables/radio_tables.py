import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
import helper_function.pccm_names as pccm_names
import pandas as pd
from helper_function.option_lists import Radio, RadioTables, MultiTest


class MassCalcification:

    def __init__(self, table, mammo_breast, file_number, user_name):
        self.table = table
        self.mammo_breast = mammo_breast
        self.col_list = pccm_names.names_radio_mass(self.table)
        self.file_number = file_number
        self.user_name = user_name

    def mammo_mass(self, mass_id):
        print(self.table, mass_id)
        check = False
        data_list = ask.default_data_list(self.col_list)
        while not check:
            mass_location = self.mammo_breast
            if self.mammo_breast == "bilateral":
                mass_location = ask.ask_option("Location of mass "
                                               + str(mass_id),
                                               RadioTables.breast)
            mass_quadrant = ask.ask_list('Quadrant location of lesion',
                                         Radio.lesion_quadrant)
            mammo_mass_shape = ask.ask_option("Shape of mass",
                                              RadioTables.mass_shape)
            mammo_mass_margin = ask.ask_option("Margins of mass",
                                               RadioTables.mass_margin)
            mass_nipple = input("Distance from nipple (cm): ")
            mass_dimension,
            mass_size_unit,
            mass_longest_dimension = self.lesion_size()
            modality = self.table
            data_list = [self.file_number, mass_location, mass_name,
                         mass_quadrant, mammo_mass_shape, mammo_mass_margin,
                         mass_nipple, mass_dimension, mass_longest_dimension,
                         mass_size_unit, modality]
            check = sql.review_input(self.file_number, columns=self.col_list,
                                     data=data_list)
            data_list = data_list + [self.user_name, sql.last_update()]
        return data_list

    def usg_mass(self, mass_id):
        print(self.table, mass_id)
        check = False
        data_list = ask.default_data_list(self.col_list)
        while not check:
            mass_location = self.mammo_breast
            if self.mammo_breast == "bilateral":
                mass_location = ask.ask_option("Location of mass "
                                               + str(mass_id),
                                               RadioTables.breast)
            location_clock = ask.check_number_input("What is the clock"
                                                    "position of mass "
                                                    + str(mass_id) + "?",
                                                    'Please enter only numbers'
                                                    ' additional paramters '
                                                    'can be entered '
                                                    'next')
            location_add = input('Additional parameters for clock position')
            location_clock = location_clock + location_add + " o'clock"
            mass_quadrant = 'data_not_available'
            quad = ask.ask_y_n('Is the quadrant location given?')
            if quad:
                mass_quadrant = ask.ask_list('what is the quadrant location',
                                             Radio.lesion_quadrant)
            mass_shape = ask.ask_list("Shape of mass " + str(mass_id),
                                      RadioTables.mass_shape)
            mass_name = "lesion_" + str(mass_id)
            mass_dimension,
            mass_size_unit,
            mass_longest_dimension = self.lesion_size()
            mass_margin = ask.ask_option("Margin of mass " + str(mass_id),
                                         RadioTables.mass_margin_usg)
            mass_echo = ask.ask_option("Echo pattern of mass " + str(mass_id),
                                       RadioTables.mass_echo)
            mass_id = "Mass " + str(mass_id)
            modality = self.table
            data_list = [self.file_number, mass_name, mass_location,
                         location_clock, mass_quadrant, mass_shape,
                         mass_margin, mass_echo, mass_dimension,
                         mass_longest_dimension, mass_size_unit, modality]
            check = sql.review_input(self.file_number, columns=self.col_list,
                                     data=data_list)
            data_list = data_list + [self.user_name, sql.last_update()]
        return data_list

    def mri_mass(self, mass_id):
        check = False
        data_list = ask.default_data_list(self.col_list)
        while not check:
            if self.mammo_breast == "bilateral":
                mass_location = ask.ask_option("Location of mass " + str(
                                               mass_id), RadioTables.breast)
            else:
                mass_location = self.mammo_breast
            check_t1_t2 = ask.ask_y_n('Are both T1 and T2 image analysis'
                                      'available for this mass?')
            type_of_imaging = ['T1', 'T2']
            if not check_t1_t2:
                type_of_imaging = ask.ask_list('Observation of this mass is a'
                                               'result of which type of'
                                               'imaging? ',
                                               RadioTables.mri_image_type)
            data_list = self.mri_mass_detail(type_of_imaging, mass_id)
            if type_of_imaging in {'T1', 'T2'}:
                data_list = [('{0}_{1}'.format(type_of_imaging, data)) for
                             data in data_list]
            mass_name = "Lesion " + str(mass_id)
            data_list = [self.file_number, mass_location, mass_name]+data_list
            check = sql.review_input(self.file_number, columns=self.col_list,
                                     data=data_list)
            data_list = [data_list] + [self.user_name, sql.last_update()]
            data_list = data_list + [self.user_name, sql.last_update()]
        return data_list

    def mri_mass_detail(self, image_type, mass_id):
        print(self.table, mass_id)
        data_list = ask.default_data_list(self.col_list)
        check = False
        while not check:
            non_mass = ask.ask_y_n('Is the enhancement non-mass?')
            enhancement_type = 'mass'
            if non_mass:
                enhancement_type = 'non_mass'
            location_clock = input("What is the clock position of mass "
                                   + str(mass_id) + "? (Enter NA if clock"
                                   "position not available)")
            if location_clock != 'NA':
                location_clock = location_clock + " o'clock"
            mass_quadrant = ask.ask_option('Quadrant location of mass',
                                           Radio.lesion_quadrant)
            mass_shape = ask.ask_option("Shape of mass " + str(mass_id),
                                        RadioTables.mass_shape)
            mass_margin = ask.ask_option("Margin of mass " + str(mass_id),
                                         RadioTables.mass_margin_mri)
            mass_dimension,
            mass_size_unit,
            mass_longest_dimension = self.lesion_size()
            mass_echo = ask.ask_option("Internal enhancement characteristics"
                                       " " + str(mass_id),
                                       RadioTables.mass_iec)
            mass_id = "Mass " + str(mass_id)
            modality = self.table
            data_list = [mass_id, image_type, enhancement_type, location_clock,
                         mass_quadrant, mass_shape,  mass_margin,
                         mass_echo, mass_dimension,
                         str(mass_longest_dimension), mass_size_unit, modality]
            col_list = self.col_list[3:]
            check = sql.review_input(self.file_number, columns=col_list,
                                     data=data_list)
            data_list = data_list + [self.user_name, sql.last_update()]
        return data_list

    def mass_fx(self, mass_id):
        mass_dict = {'mammography': self.mammo_mass,
                     'ultrasound': self.usg_mass,
                     'mri_breast': self.mri_mass}
        dat = mass_dict[self.table](mass_id)
        return dat

    def multiple_mass(self):
        mass_df = pd.DataFrame(columns=self.col_list)
        number_mass = input("Number of masses detected: ")
        try:
            mass_number = int(number_mass)
        except ValueError:
            mass_number = 1
        mass_all = list(range(0, (mass_number)))
        for i in mass_all:
            mass_id = 'mass_' + str(1+i)
            dat = self.mass_fx(mass_id)
            mass_df.loc[i] = dat
        mass_data = []
        for col in mass_df.columns[-1]:
            dat = list(mass_df[col])
            dat = '|'.join(dat)
            mass_dat.append(data)     
        return mass_data[:-2]
        # data_mass = ('| '.join(dat) for dat in mass_list)
        # data_df = ask.join_lists([data_mass], "; ")
        # mass_id_, location_quad, mammo_mass_shape, mammo_mass_margin,
        # mass_nipple, \
        # mass_size, mass_size_unit  = data_df
        # data_return = number_mass, location_quad, mammo_mass_shape,
        # mammo_mass_margin, mass_nipple, mass_size,
        # mass_size_unit


def clinical_tests():
    other_tests = {'USG Abdomen': ['Abnormal'],
                   'CECT Abdomen and Thorax': ['Visceral Metastasis'],
                   'PET Scan': ['Visceral Metastasis', 'Skeletal Metastasis'],
                   'Bone Scan': ['Skeletal Metastasis']}
    test_key = list(other_tests.keys())
    data_list = []
    for test in test_key:
        test_name = test
        test_done = ask.ask_y_n("Has "+test_name+" been done?")
        if test_done:
            test_done = test_name+" done"
            data_list.append(test_done)
            abnormal = other_tests[test]
            for diagnosis in abnormal:
                test_diag = ask.ask_y_n('Is the result ' + diagnosis + '?')
                if test_diag:
                    test_details = input("Please provide details of "
                                         + diagnosis + " diagnosis: ")
                else:
                    diagnosis = 'Normal'
                    test_details = "NA"
                data_list.append(diagnosis)
                data_list.append(test_details)
        else:
            test_done = test_name+"_not_done"
            data_list.append(test_done)
            abnormal = other_tests[test]
            for i in range(2*len(abnormal)):
                i = 'NA'
                data_list.append(i)
    return data_list


def birads():
    check = False
    while not check:
        birad_list = [i for i in Radio.birads]
        mammo_birads = ask.ask_option("BI-RADS Category", birad_list)
        mammo_birads_det = Radio.birads.get(mammo_birads)
        birad = mammo_birads + ": " + mammo_birads_det
        print(birad)
        check = ask.ask_y_n("Is this correct?")
        data_list = birad
    return data_list


def cal_table(file_number, mammo_breast):
    import helper_function.pccm_names as pccm_names
    table = "calcification_mammography"
    mass_number = ask.check_number_input("Number of groups of calcifications"
                                         " detected? ", error='Please enter'
                                         'number of calcification groups'
                                         'detected only')
    try:
        number_calc = int(mass_number)
    except ValueError:
        number_calc = 1
    location, calc_type, calicification_comments = [list([]) for _ in range(3)]
    for index in range(0, number_calc):
        check = False
        while not check:
            mass_id = index + 1
            if mammo_breast == "Bilateral":
                mass_location = ask.ask_option("Location of calcification"
                                               "group " + str(mass_id),
                                               ["Right Breast", "Left Breast"])
            else:
                mass_location = mammo_breast
            location.append(mass_location)
            mammo_calcification = ask.ask_option("Calcification Type ",
                                                 ["Skin", "Vascular",
                                                  "Coarse or 'Popcorn-like'",
                                                  "Large Rod-like",
                                                  "Round and punctate",
                                                  "Eggshell or Rim",
                                                  "Dystrophic", "Suture",
                                                  "Amorphous",
                                                  "Coarse Heterogeneous",
                                                  "Fine Pleomorphic",
                                                  "Fine Linear or"
                                                  "Fine Linear Branching",
                                                  "Other"])
            calc_type.append(mammo_calcification)
            mass_id = "Group " + str(index + 1)
            comment = input('Additional comments for calcification: ')
            calicification_comments.append(comment)
            data_list = [file_number, mass_id, str(mass_location),
                         mammo_calcification, comment]
            col_list = pccm_names.names_radio_mass(table)
            check = sql.review_input(file_number, col_list, data_list)
    all_data = [[str(mass_number)], location, calc_type,
                calicification_comments]
    data_return = ask.join_lists(all_data, "; ")
    return tuple(data_return)

    @staticmethod
    def lesion_size():
        mass_size = ask.check_size_input("Mass dimensions (without unit): ")
        mass_size_unit = 'NA'
        if mass_size != 'NA':
            mass_size_unit = ask.ask_list("Mass dimensions unit: ",
                                          RadioTables.mass_units)
        mass_name = "lesion_" + str(mass_id)
        mass_dimension, mass_longest_dimension = mass_size
        mass_longest_dimension = ask.convert_mm_to_cm(
                                 mass_longest_dimension, mass_size_unit)
        return mass_size, mass_size_unit, mass_longest_dimension

# todo : fix option - what is it supposed to be?


def lesion_location(lesion, option=MultiTest.breast_cancer):
    lesion_data = {}
    category = ["Location on right_breast", "Location on left_breast",
                'Other Location']
    if lesion in {"right_breast", "bilateral"}:
        lesion_rb = ask.ask_option(category[0], )
        lesion_rb_data = "RB-" + lesion_rb
        lesion_data.append(lesion_rb_data)
    if lesion in {"right_breast", "bilateral"}:
        lesion_lb = ask.ask_option(category[1], option)
        lesion_lb_data = "LB-" + lesion_lb
        lesion_data.append(lesion_lb_data)
    if lesion not in {MultiTest.breast_cancer}:
        lesion_other = str.lower(str.replace(lesion, ' ', '_'))
        lesion_data.append(lesion_other)
    lesion_data = "|".join(lesion_data)
    return lesion_data


def check_masscalc():
    table = 'mammography'
    mammo_breast = 'right_brast'
    file_number = 'test'
    user_name = 'dk'
    masscalc = MassCalcification(table, mammo_breast, file_number, user_name)
    mass_id = ['1', '2']
    dat_all = []
    for mass in mass_id:
        dat = masscalc.mass_fx(mass)
        dat_all.append(dat)
    return dat_all

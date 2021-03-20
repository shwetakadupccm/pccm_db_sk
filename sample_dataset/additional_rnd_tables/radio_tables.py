import helper_function.ask_y_n_statement as  ask
import sql.add_update_sql as sql
import helper_function.pccm_names as pccm_names
import pandas as pd
from helper_function.option_lists import Radio, RadioTables, MultiTest
import sample_dataset.general_functions as gf


class MassCalcification:

    def __init__(self, table, mammo_breast, file_number, user_name):
        self.table = table
        self.mammo_breast = mammo_breast
        self.col_list = pccm_names.names_radio_mass(self.table)
        self.file_number = file_number
        self.user_name = user_name

    def mammo_mass(self, mass_id):
        data_list = ask.default_data_list(self.col_list)
        mass_location = self.mammo_breast
        if self.mammo_breast == "bilateral":
            mass_location = gf.get_choice(RadioTables.breast)
        mass_quadrant = gf.get_choice(Radio.lesion_quadrant)
        mammo_mass_shape = gf.get_choice(RadioTables.mass_shape)
        mammo_mass_margin = gf.get_choice(RadioTables.mass_margin)
        mass_nipple = gf.get_number(10)
        size_input = gf.get_choice(['3d', '2d'])
        x = gf.get_number_lt(1, 10)
        y = gf.get_number_lt(1, 10)
        z = gf.get_number_lt(1, 10)
        if size_input == '3d':
            mass_dimension = [str(x) + ' x ' + str(y) + ' x ' + str(z)]
            mass_longest_dimension = max([x, y, z])
        elif size_input == '2d':
            mass_dimension = [str(x) + ' x ' + str(y)]
            mass_longest_dimension = max([x, y])
        mass_size_unit = gf.get_choice(RadioTables.mass_units)
        mass_name = "lesion_" + str(mass_id)
        modality = self.table
        data_list = [self.file_number, mass_location, mass_name,
                     mass_quadrant, mammo_mass_shape, mammo_mass_margin,
                     mass_nipple, mass_dimension,
                     mass_longest_dimension, mass_size_unit, modality]
        data_list = data_list + [self.user_name, sql.last_update()]
        return data_list

    def multiple_mass(self):
        number_mass = gf.get_number_lt(1, 4)
        mass_df = pd.DataFrame(columns=self.col_list, index=range(number_mass))
        for i in range(number_mass):
            mass_id = 'mass' + str(1+i)
            dat = self.mammo_mass(mass_id)
            dat = [str(data) for data in dat]
            mass_df.loc[i] = dat
        mass_dat = []
        for col in list(mass_df.columns):
            i = "; ".join(list(mass_df[col]))
            mass_dat.append(i)
        return number_mass, mass_dat[:-2]


def clinical_tests():
    other_tests = {'USG Abdomen': ['Abnormal'], 'CECT Abdomen and Thorax': ['Visceral Metastasis'],
                   'PET Scan': ['Visceral Metastasis', 'Skeletal Metastasis'], 'Bone Scan': ['Skeletal Metastasis']}
    test_key = list(other_tests.keys())
    data_list = []
    for test in test_key:
        test_name = test
        test_done = gf.get_bool()
        if test_done:
            test_done = test_name+" done"
            data_list.append(test_done)
            abnormal = other_tests[test]
            for diagnosis in abnormal:
                test_diag = gf.get_bool()
                if test_diag:
                    test_details = 'data_not_available'
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
    birad_list = [i for i in Radio.birads]
    mammo_birads = gf.get_choice(birad_list)
    mammo_birads_det = Radio.birads.get(mammo_birads)
    birad = mammo_birads + ": " + mammo_birads_det
    data_list = birad
    return data_list


def cal_table(file_number, mammo_breast):
    import helper_function.pccm_names as pccm_names
    table = "calcification_mammography"
    mass_number = gf.get_number_lt(1,3)
    try:
        number_calc = int(mass_number)
    except ValueError:
        number_calc = 1
    location, calc_type, calicification_comments = [list([]) for _ in range(3)]
    for index in range(0, number_calc):
        mass_id = index + 1
        if mammo_breast == "Bilateral":
            mass_location = gf.get_choice(["Right Breast", "Left Breast"])
        else:
            mass_location = mammo_breast
        location.append(mass_location)
        mammo_calcification = gf.get_choice(["Skin", "Vascular", "Coarse or 'Popcorn-like'",
                                             "Large Rod-like", "Round and punctate", "Eggshell or Rim",
                                             "Dystrophic", "Suture", "Amorphous", "Coarse Heterogeneous",
                                             "Fine Pleomorphic", "Fine Linear or Fine Linear Branching", "Other"])
        calc_type.append(mammo_calcification)
        mass_id = "Group " + str(index + 1)
        comment = 'na'
        calicification_comments.append(comment)
        data_list = [file_number, mass_id, str(mass_location), mammo_calcification, comment]
        col_list = pccm_names.names_radio_mass(table)
    all_data = [[str(mass_number)], location, calc_type, calicification_comments]
    data_return = ask.join_lists(all_data, "; ")
    return tuple(data_return)

#todo : fix option - what is it supposed to be?


def lesion_location(lesion, option=MultiTest.breast_cancer):
    lesion_data = {}
    category = ["Location on right_breast", "Location on left_breast",
                'Other Location']
    if lesion in {"right_breast", "bilateral"}:
        lesion_rb = gf.get_choice(option)
        lesion_rb_data = "RB-" + lesion_rb
        lesion_data.append(lesion_rb_data)
    if lesion in {"right_breast", "bilateral"}:
        lesion_lb = gf.get_choice(option)
        lesion_lb_data = "LB-" + lesion_lb
        lesion_data.append(lesion_lb_data)
    if lesion not in {MultiTest.breast_cancer}:
        lesion_other = str.lower(str.replace(lesion, ' ', '_'))
        lesion_data.append(lesion_other)
    lesion_data = "|".join(lesion_data)
    return lesion_data

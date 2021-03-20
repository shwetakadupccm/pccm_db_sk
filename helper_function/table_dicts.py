from helper_function import pccm_names as names


def create_col_list (colnames):
    try:
        col_list = ['file_number'] + colnames
    except(TypeError):
        col_list = ['file_number']
    return col_list


def table_module_dict(table):
    table_module = {
        "patient_information_history": ["bio_info", "phys_act", "habits", "nut_supplements", "family_details",
                                        "med_history", "cancer_history", "family_cancer", "det_by", "breast_symptoms",
                                        'other_test'],
        "mammography": [], "abvs": [], "sonomammo": [], "mri_breast": [],
        'pet_reports': ['pet_report_identifier', 'pet_report_findings', 'pet_breast_cancer'],
        "neo_adjuvant_therapy": ["neo_adjuvant_therapy", "clip_information"],
        'biopsy_report': [],
        "surgery_report": ["surgery_information", "node_excision", "post_surgery"],
        "adjuvant_chemotherapy": ['adjuvant_chemotherapy'],
        "radiotherapy": [],
        "hormonetherapy_survival": ["hormone", "metastasis"],
        "follow_up_data": [],
        'block_list': ['all'],
        'biopsy_path_report_data': ['biopsy_report_info', 'biopsy_details', 'ihc_biopsy_data', 'review_biopsy'],
        'surgery_path_report_data': ['surgery_block_information_0', 'surgery_block_information_1',
                                     'surgery_block_information_2', 'surgery_block_information_3']

    }
    module_list = table_module.get(table)
    return module_list


def table_module_research(table):
    table_module = {
        "patient_information_history": ["bio_info_without_personal_info", "phys_act", "habits", "nut_supplements", "family_details",
                                        "med_history","cancer_history", "family_cancer", "det_by", "breast_symptoms",
                                        'other_test'],
        "mammography": [], "abvs": [], "sonomammo": [], "mri_breast": [],
        'pet_reports' : ['pet_report_identifier', 'pet_report_findings', 'pet_breast_cancer'],
        "neo_adjuvant_therapy": ["neo_adjuvant_therapy", "clip_information"],
        "surgery_report": ["surgery_information", "node_excision", "post_surgery"],
        "adjuvant_chemotherapy": ['adjuvant_chemotherapy'],
        "radiotherapy": [],
        "hormonetherapy_survival": ["hormone", "metastasis"],
        "follow_up_data": [],
        'block_list': ['research'],
        'biopsy_path_report_data': ['biopsy_report_info', 'biopsy_details', 'ihc_biopsy_data', 'review_biopsy'],
        'surgery_path_report_data': ['surgery_block_information_0', 'surgery_block_information_1',
                                     'surgery_block_information_2', 'surgery_block_information_3']
    }
    module_list = table_module.get(table)
    return module_list

def db_dict (table, module):
    db_tables = {"patient_information_history": names.names_info(module),
                 "radiology": names.names_radio(module),
                 'pet_reports': names.names_pet(module),
                 'biopsy_path_report_data': names.names_biopsy(module),
                 "neo_adjuvant_therapy": names.names_nact(module),
                 "surgery_report": names.names_surgery_information(module),
                 'surgery_path_report_data': names.names_surgery(module),
                 "adjuvant_chemotherapy": names.names_chemotherapy(module),
                 "radiotherapy": names.names_radiation(),
                 "hormonetherapy_survival": names.names_longterm(module),
                 "follow_up_data": names.name_follow_up(),
                 'block_list': names.block_list(module)}

    cols = db_tables.get(table)
    return cols

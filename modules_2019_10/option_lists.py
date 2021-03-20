class SurgeryLists:
    anesthetists = ["Dr.Sachin Arbhi", "Dr. Sandhya Sathe", 'Dr. Sagar Sanjay', 'Dr. Amol Ramekar',"Dr. Nita D'Souza",
                    'other']
    hospitals = ['Ruby Hall Clinic', 'RHC Wanowarie','Jehangir Hospital', 'Oyster and Pearl', 'Inamdar Hospital',
                 'other']
    surgeon = ["Dr. C. B. Koppiker", 'other']
    lesion = ["Right Breast", "Left Breast", "Both Breasts", "other", "Not known"]
    incision =  ['Inframammary Fold Incision','Lateral Fold', 'Lateral Crease', 'Wise Pattern', 'Radial', 'Oblique',
                 'Transverse Oblique', 'Oblique with Supra-areolar','Circum-areolar', 'Axillary', 'Vertical Scar']
    conventional_surgery_subtype = ["Lumpectomy", "Quadrantectomy", "Wedge Resection", 'Extreme Resection']
    oncoplastic_levels = "Level 1", "Level 2: Therapeutic Mammoplasty",'Level 3: Volume Replacement'
    level_1_type = ["Type 1: Simple oncoplastic – mammoplasty", "Type 2: Volume Displacement"]
    level_2_flap = ["Grisotti Flap", "Round Block", "Batwing Procedure"]
    simple_plan = ['Wise pattern', 'Vertical Scar']
    simple_pedicle = ["Lower Pedicle", "Superior Pedicle", "Superio-medial Pedicle", "Lateral Pedicle",
                       "Dual Pedicle", "other"]
    primary_pedicle = ["Lower Pedicle", "Superior Pedicle", "Superio-medial Pedicle", "Lateral Pedicle",
                       "Inferior Pedicle", "Inferior Medial Pedicle", "Inferior Medial and Lateral Pedicle", "other"]
    guide = ['Wire guided', 'USG guided', 'other']


class PathReports:
    path_labs = ['A.G. Diagnostics', 'Ruby Hall Clinic', 'SRL Pathlab', 'Core Diagnostics', 'Other']
    diagnosis = ['IDC', 'IDC+DCIS', 'ILC', 'LCIS', 'ILC+LCIS', 'DCIS', 'Granulamatous Mastitis', 'Papillary Carcinoma',
                 'Malignant Phylloides', 'Phylloides', 'Other']
    biopsy_type = ["trucut", "vab", 'excision', 'fnac', 'lumpectomy']
    grade = ["I", "II", "III", 'na']
    surgery_type = ['Mastectomy', 'Modified Radical Mastectomy', 'Breast Conservation Surgery',
                    'Therapeutic Mammoplasty', 'Reduction Mammoplasty', 'Lumpectomy (Wide Local Excision)',
                    'Reconstruction', 'Mastopexy', 'Other']
    surgeon = ["Dr. C. B. Koppiker", 'other']


class BlockList:
    edit_values = {'current_block_location' : ['pccm', 'iiser_mk_lab', 'iiser_ml_lab', 'with_patient', 'not_available'],
                   'number_of_blocks' : ['Enter value'], 'block_series' : ['Enter value'],
                   'block_type': ['biopsy', 'surgery'], 'block_id' : ['Enter value']}
    unique_values = {'file_number', 'mr_number', 'block_sr_number', 'block_location','block_id'}


class FollowUpStatus:
    survivor_status = ["disease Free", "with recurrence", "disease free with no known recurrence",
                       'primary surgery not done', 'metastatic disease']
    deceased_status = ["due to disease", "due to unrelated causes", "not known"]


class PetReport:
    carcinoma_status = ["pre-operative", "post-operative", 'other']
    breast_cancer = ["right_breast", "left_breast", "other"]
    body_region = ['skull_to_mid_thigh', 'other']
    machine_name = ['LYSO Crystal based Gemini TF16 Pet-CT Scanner', 'other']
    pet_regions = ['head & neck', 'thorax', 'abdomen & pelvis', 'muscoskeletal']


class PatientInfo:
    menopause_status = ["Pre-menopausal", "Peri-menopausal", "Post-Menopausal", 'data_not_available', "Other"]
    symp_state = ["Pain or tenderness", "Lumps", "Nipple Discharge", "Nipple Retraction", "Dimpling",
                  "Discolouration", "Ulceration", "Eczema"]
    met_symptoms = ['Bone Pain', 'Cough', 'Jaundice', 'Headache', 'Weight loss']
    diet = ["Vegetarian", "Non-Vegetarian", "Ovo-Vegetarian", "Other"]
    tobacco_exposure = ["Passive", "Active", "Other"]
    passive_tobacco = ["Home", "Work", "Commute", "Social Interactions"]
    type_tobacco = ["Cigarette", "Beedi", "Gutkha", "Pan Masala", "Jarda/Maava", "Hookah", "Nicotine Patch", "Mishri",
                    "Other"]
    previous_cancer_treatment = ["surgery", "radiation", "chemotherapy", "hormone", "alternative", "homeremedy"]
    family = ["immediate", "maternal", "paternal"]
    breast_feeding = ["right_breast", "left_breast", "both_breasts", "other"]
class SurgeryLists:
    anesthetists = ['Dr.Sachin Arbhi', 'Dr. Sandhya Sathe', 'Dr. Sagar Sanjay', 'Dr. Amol Ramekar', "Dr. Nita D'Souza",
                    'requires_follow_up', 'data_not_in_report', 'other']
    hospitals = ['Ruby Hall Clinic', 'RHC Wanowarie', 'Jehangir Hospital', 'Oyster and Pearl', 'Inamdar Hospital',
                 'requires_follow_up', 'data_not_in_report', 'other']
    surgeon = ['Dr. C. B. Koppiker', 'other']
    lesion = ['right_breast', 'left_breast', 'both_breasts', 'requires_follow_up', 'data_not_in_report',
              'other', 'Not known']
    incision = ['inframammary_fold_incision', 'lateral_fold', 'lateral_crease', 'wise_pattern', 'radial', 'oblique',
                'transverse_oblique', 'oblique_with_supra_areolar', 'circum_areolar', 'axillary', 'vertical_scar',
                'requires_follow_up', 'data_not_in_report']
    conventional_surgery_subtype = ['lumpectomy', 'quadrantectomy', 'wedge_resection', 'extreme_resection',
                                    'requires_follow_up', 'data_not_in_report']
    oncoplastic_levels = 'Level 1', 'Level 2: Therapeutic Mammoplasty', 'Level 3: Volume Replacement'
    level_1_type = ['Type 1: Simple oncoplastic – mammoplasty', 'Type 2: Volume Displacement']
    level_2_flap = ['grisotti_flap', 'round_block', 'batwing_procedure', 'requires_follow_up', 'data_not_in_report']
    simple_plan = ['wise_pattern', 'vertical_scar', 'requires_follow_up', 'data_not_in_report']
    simple_pedicle = ['lower_pedicle', 'superior_pedicle', 'superio_medial_pedicle', 'lateral_pedicle', 'dual_pedicle',
                      'requires_follow_up', 'data_not_in_report', 'other']
    primary_pedicle = ['lower_pedicle', 'superior_pedicle', 'superio_medial_pedicle', 'lateral_pedicle',
                       'inferior_pedicle', 'inferior_medial_pedicle', 'inferior_medial_and_lateral_pedicle',
                       'requires_follow_up', 'data_not_in_report', 'other']
    guide = ['Wire guided', 'USG guided', 'requires_follow_up', 'data_not_in_report', 'other']


class PathReports:
    path_labs = ['A.G. Diagnostics', 'Ruby Hall Clinic', 'SRL Pathlab', 'Core Diagnostics', 'requires_follow_up',
                 'data_not_in_report', 'Other']
    diagnosis = ['IDC', 'IDC+DCIS', 'ILC', 'LCIS', 'ILC+LCIS', 'DCIS', 'granulamatous_mastitis', 'papillary_carcinoma',
                 'malignant_phylloides', 'phylloides', 'requires_follow_up', 'data_not_in_report', 'other']
    biopsy_type = ['trucut', 'vab', 'excision', 'fnac', 'lumpectomy', 'requires_follow_up', 'data_not_in_report']
    grade = ['I', 'II', 'III', 'na']
    surgery_type = ['mastectomy', 'modified_radical_mastectomy', 'breast_conservation_surgery',
                    'therapeutic_mammoplasty', 'reduction_mammoplasty', 'lumpectomy (wide_local_excision)',
                    'reconstruction', 'mastopexy', 'requires_follow_up', 'data_not_in_report', 'Other']
    surgeon = ['Dr. C. B. Koppiker', 'other']


class BlockList:
    edit_values = dict(current_block_location=['pccm', 'iiser_mk_lab',
                       'iiser_ml_lab', 'with_patient', 'not_available'],
                       number_of_blocks=['Enter value'], block_series=['Enter value'], block_type=['biopsy', 'surgery'],
                       block_id=['Enter value'])
    unique_values = {'file_number', 'mr_number', 'block_sr_number', 'block_location', 'block_id'}


class FollowUpStatus:
    survivor_status = ['disease_free', 'with_recurrence', 'with_disease', 'disease_free_with_no_known_recurrence',
                       'primary_surgery_not_done', 'metastatic_disease', 'lost_to_follow_up',
                       'requires_follow_up', 'data_not_in_report']
    deceased_status = ['due_to_disease', 'due_to_unrelated_causes', 'not_known',
                       'requires_follow_up', 'data_not_in_report']


class PetReport:
    pet_carcinoma_status = ['pre_operative', 'post_operative', 'requires_follow_up', 'data_not_in_report', 'other']
    pet_cancer_location = ['right_breast', 'left_breast', 'bilateral', 'thorax', 'requires_follow_up',
                           'data_not_in_report', 'other']
    body_region = ['skull_to_mid_thigh', 'chest', 'abdomen', 'pelvis', 'thorax', 'musculoskeletal', 'whole_body',
                   'requires_follow_up', 'data_not_in_report', 'other']
    machine_name = ['LYSO Crystal based Gemini TF16 Pet-CT Scanner', 'requires_follow_up',
                    'data_not_in_report', 'other']
    pet_regions = ['head & neck', 'thorax', 'abdomen & pelvis', 'muscoskeletal', 'requires_follow_up',
                   'data_not_in_report', 'other']


class IHC:
    ihc_status = ['positive', 'negative', 'borderline', 'equivocal']


class PatientInfo:
    gender = ['male', 'female', 'other']
    menopause_status = ['pre_menopausal', 'peri_menopausal', 'post_menopausal', 'hysterectomy', 'oopherectomy',
                        'bilateral_oopherectomy', 'post_hysterectomy', 'requires_follow_up',
                        'data_not_in_report', 'Other']
    menstrual_type = ['regular', 'irregular', 'requires_follow_up', 'data_not_in_report']
    symp_state = ['pain_or_tenderness', 'lumps', 'nipple_discharge', 'nipple_retraction', 'dimpling',
                  'discolouration', 'ulceration', 'eczema', 'swelling', 'redness', 'requires_follow_up',
                  'data_not_in_report']
    met_symptoms = ['bone_pain', 'cough', 'jaundice', 'headache', 'weight_loss', 'requires_follow_up',
                    'data_not_in_report']
    diet = ['vegetarian', 'non-vegetarian', 'ovo-vegetarian', 'requires_follow_up', 'data_not_in_report', 'other']
    tobacco_exposure = ['passive', 'active', 'requires_follow_up', 'data_not_in_report', 'Other']
    passive_tobacco = ['home', 'work', 'commute', 'social_interactions', 'requires_follow_up', 'data_not_in_report']
    type_tobacco = ['cigarette', 'beedi', 'gutkha', 'pan_masala', 'jarda/maava', 'hookah', 'nicotine_Patch', 'mishri',
                    'requires_follow_up', 'data_not_in_report', 'Other']
    previous_cancer_treatment = ['surgery', 'radiation', 'chemotherapy', 'hormone', 'alternative', 'homeremedy',
                                 'requires_follow_up', 'data_not_in_report']
    family = ['immediate', 'maternal', 'paternal', 'requires_follow_up', 'data_not_in_report']
    breast_feeding = ['right_breast', 'left_breast', 'both_breasts', 'requires_follow_up', 'data_not_in_report', 'other']
    phys_act = ['yoga', 'walking', 'weights', 'aerobics', 'zumba', 'cycling', 'running', 'swimming',
                'jogging', 'gym', 'dance', 'exercise', 'lower_intensity_exercise', 'other_vigorous_activity',
                'requires_follow_up', 'data_not_in_report', 'other']
    frequency = ['weekly', 'daily', 'twice weekly', 'alternate days',
                 'twice_a_month', 'monthly', 'rarely', 'requires_follow_up', 'data_not_in_report']
    fert_treat = ['IVF', 'ovarian_stimulation', 'hormone_injection',
                  'not_aware_of_details', 'requires_follow_up', 'data_not_in_report']
    cancer_detected_by = ['self', 'routine_checkup', 'physician', 'screening_camp', 'requires_follow_up',
                          'data_not_in_report']

physical_activity_dict = {'walking': ['walk', 'walking', 'walking_for_exercise', 'lawn_walking'],
                             'cycling': ['cycle', 'cycling', 'bicycling'],
                             'running': ['run', 'running'],
                             'swimming': ['swimm', 'swimming', 'lap swimming'],
                             'jogging': ['jogging', 'jogg'],
                             'gym': ['gym', 'gymming'],
                             'dancing': ['dance', 'dancing', 'kathak', 'zumba'],
                             'exercise': ['exercise', 'yoga', 'lower intensity exercise', 'aerobic exercise',
                                         'other aerobic exercise'],
                             'player': ['badminton', 'tennis', 'throw ball']}


class RadiotherapyOptions:
    rt_location = ['ipsilateral_breast', 'contralateral_breast', 'chest_wall', 'supraclavicular_fossa', 'axilla',
                   'other_location', 'requires_follow_up', 'data_not_in_report']
    rt_hosp = ['Ruby Hall', 'Inlaks/Budhrani', 'requires_follow_up', 'data_not_in_report']
    rt_doc = ['Dr. Mansi Munshi', 'Dr. Gautam Sharan', 'requires_follow_up', 'data_not_in_report', 'other']
    reason_imrt = ['financial', 'not_advised', 'data_not_available', 'requires_follow_up', 'data_not_in_report',
                   'other']
    no_rt_reason = ['not_indicated', 'unable_to_afford', 'patients_reluctance', 'logistic_concern',
                    'requires_follow_up', 'data_not_in_report', 'other']


class MultiTest:
    test_reason = ['diagnostic', 'screening', 'follow_up', 'mid_NACT', 'post_NACT_staging', 'staging',
                   'clip_insertion', 'biopsy', 'requires_follow_up', 'data_not_in_report', 'other']
    carcinoma_status = ['pre_operative', 'post_operative', 'requires_follow_up', 'data_not_in_report', 'other']
    breast_cancer = ['right_breast', 'left_breast', 'bilateral', 'requires_follow_up', 'data_not_in_report', 'other']


class Radio:
    birads = {'Category 0': 'Incomplete – Need Additional Imaging Evaluation', 'Category 1': 'Negative',
              'Category 2': 'Benign', 'Category 3': 'Probably Benign, ', 'Category  4': 'Suspicious',
              'Category 4A': 'Low suspicion for malignancy', 'Category 4B': 'Moderate suspicion for malignancy',
              'Category 4C': 'High suspicious for malignancy', 'Category 5': 'Highly Suspicious for Malignancy',
              'Category 6': 'Malignant'}
    diagnosis = ['normal', 'benign', 'suspicious', 'diagnostic_for_cancer', 'requires_follow_up', 'data_not_in_report']
    calcification = ['calcifications_in_a_mass', 'calcifications_outside_of_a_mass', 'intraductal_calcifications',
                     'requires_follow_up', 'data_not_in_report']
    vascularity = ['absent', 'internal_vascularity', 'vessels_in_rim', 'requires_follow_up', 'data_not_in_report', 'other']
    lesion_quadrant = ['uoq', 'uiq', 'ucq', 'loq', 'liq', 'lcq', 'coq', 'ciq', 'ccq', 'retroaerolar', 'NA',
                       'requires_follow_up', 'data_not_in_report', 'other']


class RadioTables:
    breast = ['right_breast', 'left_breast', 'requires_follow_up', 'data_not_in_report']
    mass_shape = ['oval', 'round', 'irregular', 'requires_follow_up', 'data_not_in_report', 'other']
    mass_margin = ['circumscribed', 'obscured', 'microlobulated', 'indistinct', 'spiculated', 'requires_follow_up',
                   'data_not_in_report', 'other']
    mass_units = ['cm', 'mm', 'ml', 'requires_follow_up', 'data_not_in_report', 'other']
    mass_margin_usg = ['circumscribed', 'indistinct', 'angular', 'microlobulated', 'requires_follow_up',
                       'data_not_in_report']
    mass_echo = ['anechoic', 'hyperechoic', 'complex_cystic_and_solid', 'hypoechoic', 'isoechoic', 'heterogeneous',
                 'requires_follow_up', 'data_not_in_report', 'other']
    mass_margin_mri = ['circumscribed', 'irregular', 'spiculated', 'requires_follow_up', 'data_not_in_report', 'other']
    mass_iec = ['homogeneous', 'heterogeneous', 'rim_enhancement', 'dark_internal_septations',
                'requires_follow_up', 'data_not_in_report']
    mri_image_type = ['T1', 'T2', 'type_not_mentioned', 'requires_follow_up', 'data_not_in_report']


class NeoAdjuvantTherapy:
    nact_status = ['yes', 'no', 'other', 'requires_follow_up', 'data_not_in_report']
    nact_place = ['pccm', 'outside', 'requires_follow_up', 'data_not_in_report']
    toxicity_grade = ['no_toxicity', 'mild', 'moderate', 'severe', 'requires_follow_up', 'data_not_in_report',
                      'other']
    toxicity_response = ['complete', 'partial', 'no', 'requires_follow_up', 'data_not_in_report', 'other']
    tumour_response_check_method = ['sonomammography', 'mammography', 'ultrasound', 'usg', 'mri', 'pet_ct',
                                    'requires_follow_up', 'data_not_in_report', 'other']
    hormone_therapy_nact = ['nact_given', 'naht_given', 'nact_not_given', 'naht_not_given',
                            'requires_follow_up', 'data_not_in_report']
    hormone_therapy_type_nact = ['sequential', 'anastrazole', 'letrozole', 'concurrent', 'requires_follow_up',
                                 'data_not_in_report', 'other']


class Hormonetherapy:
    hormonetherapy_outcome = ['completed', 'discontinued', 'therapy_is_ongoing', 'good', 'requires_follow_up',
                              'data_not_in_report']
    nature_of_recurrence = ['no recurrence', 'local', 'metastasis', 'distant', 'requires_follow_up', 'data_not_in_report']
    distant_site = ['right_breast', 'left_breast', 'right_axilla', 'left_axilla', 'right_chest_wall', 'left_chest_wall',
                    'chest_wall_nodule', 'liver', 'brain_metastasis', 'left_side_neck', 'right_side_neck',
                    'left_axillary_node', 'right_axillary_node', 'pancreas', 'requires_follow_up', 'data_not_in_report']

class AdjuvantChemoTherapy:
    act_place = ['pccm', 'outside', 'requires_follow_up', 'data_not_in_report']
    drugs_unit = ['mg', 'gm', 'ml', 'requires_follow_up', 'data_not_in_report']
    toxicity_grade = ['mild', 'moderate', 'severe', 'no_toxicity', 'requires_follow_up', 'data_not_in_report', 'other']
    toxicity_response = ['complete', 'no_effect', 'no_toxicity', 'requires_follow_up', 'data_not_in_report']
    act_completion_status = ['act_completed', 'act_incomplete', 'ongoing', 'requires_follow_up', 'data_not_in_report']
    trastuzumab_regime_chemotherapy = ['concurrent', 'sequential', 'other', 'requires_follow_up', 'data_not_in_report']
    overy_status = ['pre_menopausal', 'post_menopausal', 'hysterectomy', 'menses ongoing', 'oopherectomy',
                    'requires_follow_up', 'data_not_in_report']


def cd_db_dict(table_name):
    i2b2dict = dict(NA='NA')
    if table_name == 'ffpe':
        i2b2dict = dict(procedure='ffpe_procedure', block_serial_number='ffpe_block_serial_number',
                        location='ffpe_location', biopsy_type='cd_biopsy_type',
                        biopsy_grade='cd_biopsy_grade', biopsy_diagnosis='cd_biopsy_diagnosis',
                        biopsy_lymphovascular_emboli='cd_biopsy_lymphovascular_emboli',
                        biopsy_subtype='cd_biopsy_subtype', biopsy_er_status='cd_biopsy_er_status',
                        biopsy_er_percentage='cd_biopsy_er_percentage', biopsy_pr_status='cd_biopsy_pr_status',
                        biopsy_pr_percentage='cd_biopsy_pr_percentage', biopsy_her2_status='cd_biopsy_her2_status',
                        biopsy_her2_score='cd_biopsy_her2_score', biopsy_fish_status='cd_biopsy_fish_status',
                        biopsy_ki67='cd_biopsy_ki67', neoadjuvant_status='cd_neoadjuvant_status',
                        neoadjuvant_regimen='cd_neoadjuvant_regimen', surgeon='cd_surgeon',
                        surgery_type='cd_surgery_type',
                        surgery_grade='cd_surgery_grade', surgery_diagnosis='cd_surgery_diagnosis',
                        surgery_lymphovascular_emboli='cd_surgery_lymphovascular_emboli',
                        surgery_subtype='cd_surgery_subtype', surgery_er_status='cd_surgery_er_status',
                        surgery_er_percentage='cd_surgery_er_percentage', surgery_pr_status='cd_surgery_pr_status',
                        surgery_pr_percentage='cd_surgery_pr_percentage', surgery_her2_status='cd_surgery_her2_status',
                        surgery_her2_score='cd_surgery_her2_score', surgery_fish='cd_surgery_fish',
                        surgery_ki67='cd_surgery_ki67', surgery_tils='cd_surgery_tils',
                        surgery_tumour_desmoplastic_response='cd_tumour_desmoplastic_response')
    return i2b2dict


def cd_unit_dict(table_name):
    unitdict = {'NA': None}
    if table_name == 'ffpe':
        unitdict = dict(ffpe_procedure=None, ffpe_block_serial_number=None, ffpe_location_user=None, ffpe_location_storage=None,
                        cd_biopsy_type=None, cd_biopsy_grade=None, cd_biopsy_diagnosis=None,
                        cd_biopsy_lymphovascular_emboli=None, cd_biopsy_subtype=None, cd_biopsy_er_status=None,
                        cd_biopsy_er_percentage=None, cd_biopsy_pr_status=None, cd_biopsy_pr_percentage=None,
                        cd_biopsy_her2_status=None, cd_biopsy_her2_score=None, cd_biopsy_fish_status=None,
                        cd_biopsy_ki67=None, cd_neoadjuvant_status=None, cd_neoadjuvant_regimen=None, cd_surgeon=None,
                        cd_surgery_type=None, cd_surgery_grade=None, cd_surgery_diagnosis=None,
                        cd_surgery_lymphovascular_emboli=None, cd_surgery_subtype=None, cd_surgery_er_status=None,
                        cd_surgery_er_percentage=None, cd_surgery_pr_status=None, cd_surgery_pr_percentage=None,
                        cd_surgery_her2_status=None, cd_surgery_her2_score=None, cd_surgery_fish=None,
                        cd_surgery_ki67=None, cd_surgery_tils=None, cd_surgery_tumour_desmoplastic_response=None)
    return unitdict


class DateCols:
    col_date = dict(date_col='NA', ffpe_date=['cabinet_location', 'block_used_by'],
                    biopsy_date=['biopsy_type', 'biopsy_grade', 'biopsy_diagnosis',
                                 'biopsy_lymphovascular_emboli', 'biopsy_subtype', 'biopsy_er_status',
                                 'biopsy_er_percentage', 'biopsy_pr_status', 'biopsy_pr_percentage',
                                 'biopsy_her2_status', 'biopsy_her2_score', 'biopsy_fish_status', 'biopsy_ki67'],
                    nat_start_date=['neoadjuvant_status', 'neoadjuvant_regimen'],
                    surgery_date=['surgeon', 'surgery_type', 'surgery_grade', 'surgery_diagnosis',
                                  'surgery_lymphovascular_emboli', 'surgery_subtype', 'surgery_er_status'])


def cd_formal_cd_dict(table_name):
    unitdict = {'NA': None}
    if table_name == 'ffpe':
        unitdict = dict(ffpe_procedure='ffpe_procedure_formal_code',
                        ffpe_block_serial_number='ffpe_block_serial_number_formal_code',
                        ffpe_location='ffpe_location_user_formal_code',
                        ffpe_location_storage='ffpe_location_storage_formal_code',
                        cd_biopsy_type='cd_biopsy_type_formal_code',
                        cd_biopsy_grade='cd_biopsy_grade_formal_code',
                        cd_biopsy_diagnosis='cd_biopsy_diagnosis_formal_code',
                        cd_biopsy_lymphovascular_emboli='cd_biopsy_lymphovascular_emboli_formal_code',
                        cd_biopsy_subtype='cd_biopsy_subtype_formal_code',
                        cd_biopsy_er_status='cd_biopsy_er_status_formal_code',
                        cd_biopsy_er_percentage='cd_biopsy_er_percentage_formal_code',
                        cd_biopsy_pr_status='cd_biopsy_pr_status_formal_code',
                        cd_biopsy_pr_percentage='cd_biopsy_pr_percentage_formal_code',
                        cd_biopsy_her2_status='cd_biopsy_her2_status_formal_code',
                        cd_biopsy_her2_score='cd_biopsy_her2_score_formal_code',
                        cd_biopsy_fish_status='cd_biopsy_fish_status_formal_code',
                        cd_biopsy_ki67='cd_biopsy_ki67_formal_code',
                        cd_neoadjuvant_status='cd_neoadjuvant_status_formal_code',
                        cd_neoadjuvant_regimen='cd_neoadjuvant_regimen_formal_code',
                        cd_surgeon='cd_surgeon_formal_code',
                        cd_surgery_type='cd_surgery_type_formal_code', cd_surgery_grade='cd_surgery_grade_formal_code',
                        cd_surgery_diagnosis='cd_surgery_diagnosis_formal_code',
                        cd_surgery_lymphovascular_emboli='cd_surgery_lymphovascular_emboli_formal_code',
                        cd_surgery_subtype='cd_surgery_subtype_formal_code',
                        cd_surgery_er_status='cd_surgery_er_status_formal_code',
                        cd_surgery_er_percentage='cd_surgery_er_percentage_formal_code',
                        cd_surgery_pr_status='cd_surgery_pr_status_formal_code',
                        cd_surgery_pr_percentage='cd_surgery_pr_percentage_formal_code',
                        cd_surgery_her2_status='cd_surgery_her2_status_formal_code',
                        cd_surgery_her2_score='cd_surgery_her2_score_formal_code',
                        cd_surgery_fish='cd_surgery_fish_formal_code', cd_surgery_ki67='cd_surgery_ki67_formal_code',
                        cd_surgery_tils='cd_surgery_tils_formal_code',
                        cd_surgery_tumour_desmoplastic_response='cd_surgery_tumour_desmoplastic_response_formal_code')
    return unitdict
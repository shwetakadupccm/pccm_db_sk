def names_info(module_name):
    if module_name == 'nut_supplements':
        col_list = ['nutritional_supplements_y_n',
                    'type_nutritional_supplements',
                    'quantity_nutritional_supplements',
                    'duration_nutritional_supplements']
    elif module_name == 'phys_act':
        col_list = ['physical_activity_y_n', 'type_physical_activity',
                    'frequency_physical_activity']
    elif module_name == 'med_history':
        col_list = ['any_other_medical_history_y_n',
                    'type_any_other_medical_history',
                    'diagnosis_date_any_other_medical_history',
                    'treatment_any_other_medical_history']
    elif module_name == 'cancer_history':
        col_list = ['previous_cancer_history_y_n',
                    'type_previous_cancer',
                    'year_diagnosed_previous_cancer',
                    'treatment_previous_cancer',
                    'treatment_type_previous_cancer',
                    'treatment_duration_previous_cancer']
    elif module_name == 'family_details':
        col_list = ['marital_status', 'siblings', 'sisters', 'brothers',
                    'children', 'daughters', 'sons', 'menarche_yrs',
                    'menopause_status', 'age_at_menopause_yrs',
                    'date_last_menstrual_period', 'period_type',
                    'number_pregnancies', 'pregnancy_to_term',
                    'number_abortions', 'age_first_child',
                    'age_first_pregnancy', 'age_last_child',
                    'age_last_pregnancy', 'two_births_in_year',
                    'breast_feeding', 'child_breast_feeding',
                    'duration_breast_feeding', 'breast_usage_breast_feeding',
                    'fertility_treatment_y_n', 'type_fertility_treatment',
                    'details_fertility_treatment',
                    'cycles_fertility_treatment',
                    'success_fertility_treatment', 'type_birth_control_used',
                    'details_birth_control', 'duration_birth_control']
    elif module_name == 'breast_symptoms':
        col_list = ['rb_symptoms', 'rb_symptoms_duration', 'lb_symptoms',
                    'lb_symptoms_duration', 'rb_other_symptoms',
                    'rb_other_symptoms_duration', 'lb_other_symptoms',
                    'lb_other_symptoms_duration','patient_metastasis_symptoms']
    elif module_name == 'habits':
        col_list = ['diet', 'alcohol_y_n', 'alcohol_consumption_age_yrs',
                    'quantity_alcohol_per_week', 'duration_alcohol',
                    'comments_alcohol', 'tobacco_y_n',
                    'exposure_mode', 'type_passive', 'type_tobacco',
                    'tobacco_consumption_age_yrs', 'tobacco_frequency',
                    'quantity_tobacco_per_week', 'duration_tobacco',
                    'comments_tobacco', 'other_deleterious_habits']
    elif module_name == 'det_by':
        col_list = ['current_breast_cancer_detected_by',
                    'current_breast_cancer_detected_date']
    elif module_name == 'family_cancer':
        col_list = ['familycancer_history_y_n',
                    'type_degreerelation_typerelation_age_familycancer']
    elif module_name == 'bio_info':
        col_list = ['mr_number', 'name', 'aadhaar_card', 'firstvisit_date',
                    'permanent_address', 'current_address', 'phone',
                    'email_id', 'gender', 'age_at_first_visit_yrs',
                    'diagnosis_age_yrs', 'date_of_birth', 'place_birth',
                    'height_cm', 'weight_kg', 'bmi']
    elif module_name == 'general_table':
        col_list = ['condition, diagnosis_date, treatment']
    elif module_name == 'family_cancer':
        col_list = ['type_cancer, relation_to_patient, type_relation,' 
                    'age_at_detection_yrs']
    elif module_name == 'previous_cancer':
        col_list = ['type_cancer, year_diagnosis, surgery, type_surgery,'
                    'duration_surgery, radiation, type_radiation,'
                    'duration_radiation', 'chemotherapy, type_chemotherapy,'
                    'duration_chemotherapy, hormone, type_hormone, '
                    'duration_hormone, alternative, type_alternative, '
                    'duration_alternative, homeremedy, type_homeremedy,'
                    'duration_homeremedy']
    elif module_name == 'nut_sup':
        col_list = ['type_nutritional_supplements, '
                    'quantity_nutritional_supplements_per_day, '
                    'duration_nutritional_supplements']
    elif module_name == 'phys_act_table':
        col_list = ['type_activity, frequency_activity']
    elif module_name == 'breast_feed':
        col_list = ['child_number, feeding_duration, breast_usage_feeding']
    elif module_name == 'bio_info_without_personal_info':
        col_list = ['firstvisit_date', 'gender', 'age_at_first_visit_yrs',
                    'diagnosis_age_yrs', 'date_of_birth',
                    'height_cm', 'weight_kg', 'bmi']
    elif module_name == 'other_test':
        col_list = ['usg_abdomen', 'diagnosis_usg_abdomen',
                    'details_diagnosis_usg_abdomen', 'cect_abd_thorax',
                    'visceral_metastasis_cect_abd_thorax',
                    'details_visceral_metastasis_cect_abd_thorax', 'pet_scan',
                    'visceral_metastasis_pet_scan',
                    'detail_visceral_metastasis_pet_scan',
                    'skeletal_metastasis_pet_scan',
                    'detail_skeletal_metastasis_pet_scan', 'bone_scan',
                    'skeletal_metastasis_bone_scan',
                    'detail_skeletal_metastasis_bone_scan',
                    'update_by', 'last_update']
    else:
        col_list = 'file_number'
    return col_list


def names_info_form_version(module_name):
    if module_name == 'nut_supplements':
        col_list = ['nutritional_supplements_y_n',
                    'type_nutritional_supplements',
                    'quantity_nutritional_supplements',
                    'duration_nutritional_supplements']
    elif module_name == 'phys_act':
        col_list = ['physical_activity_y_n', 'type_physical_activity',
                    'frequency_physical_activity']
    elif module_name == 'med_history':
        col_list = ['any_other_medical_history_y_n',
                    'type_any_other_medical_history',
                    'diagnosis_date_any_other_medical_history',
                    'treatment_any_other_medical_history']
    elif module_name == 'cancer_history':
        col_list = ['previous_cancer_history_y_n', 'type_previous_cancer',
                    'year_diagnosed_previous_cancer',
                    'treatment_previous_cancer',
                    'treatment_type_previous_cancer',
                    'treatment_duration_previous_cancer']
    elif module_name == 'family_details':
        col_list = ['marital_status', 'siblings', 'sisters', 'brothers',
                    'children', 'daughters', 'sons', 'menarche_yrs',
                    'menopause_status', 'age_at_menopause_yrs',
                    'date_last_menstrual_period', 'period_type',
                    'number_pregnancies', 'pregnancy_to_term',
                    'number_abortions', 'age_first_child',
                    'age_first_pregnancy', 'age_last_child',
                    'age_last_pregnancy', 'two_births_in_year',
                    'breast_feeding', 'child_breast_feeding',
                    'duration_breast_feeding', 'breast_usage_breast_feeding',
                    'fertility_treatment_y_n', 'type_fertility_treatment',
                    'details_fertility_treatment',
                    'cycles_fertility_treatment',
                    'success_fertility_treatment', 'type_birth_control_used',
                    'details_birth_control', 'duration_birth_control']
    elif module_name == 'breast_symptoms':
        col_list = ['rb_symptoms', 'rb_symptoms_duration', 'lb_symptoms',
                    'lb_symptoms_duration', 'rb_other_symptoms',
                    'rb_other_symptoms_duration', 'lb_other_symptoms',
                    'lb_other_symptoms_duration', 'metastasis_symptoms']
    elif module_name == 'habits':
        col_list = ['diet', 'alcohol_y_n', 'alcohol_consumption_age_yrs',
                    'quantity_alcohol_per_week', 'duration_alcohol',
                    'comments_alcohol', 'tobacco_y_n', 'exposure_mode',
                    'type_passive', 'type_tobacco',
                    'tobacco_consumptio,n_age_yrs', 'tobacco_frequency',
                    'quantity_tobacco_per_week', 'duration_tobacco',
                    'comments_tobacco', 'other_deleterious_habits']
    elif module_name == 'det_by':
        col_list = ['current_breast_cancer_detected_by',
                    'current_breast_cancer_detected_date']
    elif module_name == 'family_cancer':
        col_list = ['familycancer_history_y_n',
                    'type_degreerelation_typerelation_age_familycancer']
    elif module_name == 'bio_info':
        col_list = ['mr_number', 'name', 'aadhaar_card', 'firstvisit_date',
                    'permanent_address', 'current_address', 'phone',
                    'email_id', 'gender', 'age_at_first_visit_yrs',
                    'diagnosis_age_yrs', 'date_of_birth' 'place_birth',
                    'height_cm', 'weight_kg', 'bmi']
    elif module_name == 'general_table':
        col_list = ['condition, diagnosis_date, treatment']
    elif module_name == 'family_cancer':
        col_list = ['type_cancer, relation_to_patient, type_relation,' 
                    'age_at_detection_yrs']
    elif module_name == 'previous_cancer':
        col_list = ['type_cancer, year_diagnosis, surgery, type_surgery,'
                    'duration_surgery, radiation, type_radiation,'
                    'duration_radiation, chemotherapy, type_chemotherapy,'
                    'duration_chemotherapy, hormone, type_hormone,'
                    'duration_hormone, alternative,'
                    'and child_hnrtype_alternative, duration_alternative, '
                    'homeremedy, type_homeremedy, duration_homeremedy']
    elif module_name == 'nut_sup':
        col_list = ['type_nutritional_supplements,'
                    'quantity_nutritional_supplements_per_day, '
                    'duration_nutritional_supplements']
    elif module_name == 'phys_act_table':
        col_list = ['type_activity, frequency_activity']
    elif module_name == 'breast_feed':
        col_list = ['child_number, feeding_duration, breast_usage_feeding']
    elif module_name == 'other_test':
        col_list = ['usg_abdomen', 'diagnosis_usg_abdomen',
                    'details_diagnosis_usg_abdomen', 'cect_abd_thorax',
                    'visceral_metastasis_cect_abd_thorax',
                    'details_visceral_metastasis_cect_abd_thorax', 'pet_scan',
                    'visceral_metastasis_pet_scan',
                    'detail_visceral_metastasis_pet_scan',
                    'skeletal_metastasis_pet_scan',
                    'detail_skeletal_metastasis_pet_scan', 'bone_scan',
                    'skeletal_metastasis_bone_scan',
                    'detail_skeletal_metastasis_bone_scan',
                    'update_by', 'last_update']

    else:
        col_list = 'file_number'
    return col_list


def name_clinical(module_name):
    if module_name == 'clinical_exam_initial':
        col_list = ['provisional_diagnosis_clinical_examination_ce',
                    'lump_palpable_ce', 'lump_location_ce', 'lump_size_ce',
                    'lump_number_ce' 'lump_consistency_ce', 'lump_fixity_ce',
                    'mastitis_ce', 'mastitis_type_ce', 'tenderness_ce',
                    'nipple_retraction_ce','nipple_discharge_ce',
                    'nipple_discharge_type_ce', 'skin_changes_ce',
                    'skin_change_type_ce','palpable_axillary_nodes_ce',
                    'palpable_axillary_nodes_number_ce',
                    'palpable_axillary_nodes_size_ce',
                    'palpable_axillary_nodes_fixity_ce',
                    'palpable_supraclavicular_nodes_ce',
                    'palpable_supraclavicular_nodes_number_ce',
                    'palpable_supraclavicular_nodes_size_ce',
                    'palpable_supraclavicular_nodes_fixity_ce',
                    'contralateral_breast_ce', 'edema_arm_ce',
                    'rightarm_circumference_cm_ce',
                    'rightarm_elbowdistance_cm_ce',
                    'leftarm_circumference_cm_ce',
                    'leftarm_upperlimbvolume_cc_ce',
                    'leftarm_elbowdistance_cm_ce', 'follow_up_advised_ce',
                    'update_by', 'last_update']
    elif module_name == 'nipple_cytology':
        col_list = ['nipple_cytology', 'date_nipple_cytology',
                    'number_nipple_cytology', 'report_nipple_cytology']
    # elif module_name == 'other_test':
    #     col_list = ['usg_abdomen', 'diagnosis_usg_abdomen', 'details_diagnosis_usg_abdomen', 'cect_abd_thorax',
    #                 'visceral_metastasis_cect_abd_thorax', 'details_visceral_metastasis_cect_abd_thorax', 'pet_scan',
    #                 'visceral_metastasis_pet_scan', 'detail_visceral_metastasis_pet_scan',
    #                 'skeletal_metastasis_pet_scan', 'detail_skeletal_metastasis_pet_scan', 'bone_scan',
    #                 'skeletal_metastasis_bone_scan', 'detail_skeletal_metastasis_bone_scan']
    else:
        col_list = 'file_number'
    return col_list


def names_radio(module_name):
    if module_name == 'mammography':
        col_list = ['file_number', 'reason_report', 'report_date',
                    'mammography_place', 'mammography_indication',
                    'mammography_breast', 'mammography_massnumber',
                    'mammography_masslocation', 'mammography_massshape',
                    'mammography_massmargin', 'mammography_massnipple_cm',
                    'mammography_masssize', 'mammography_masssize_unit',
                    'mammography_calcificationnumber',
                    'mammography_calcificationlocation',
                    'mammography_calcificationtype',
                    'mammography_calcification_comments',
                    'mammography_skin_involvement',
                    'mammography_node_description','mammography_node_size',
                    'mammography_node_size_unit', 'mammography_birad',
                    'mammography_impression', 'tomography_y_n',
                    'update_by', 'last_update']
                    
    elif module_name == 'abvs':
        col_list = ['file_number', 'reason_report', 'report_date',
                    'automated_breast_volume_scanner_abvs',
                    'accession_abvs', 'lesion_abvs', 'lesion_location_abvs',
                    'size_abvs', 'distance_abvs', 'distance_pectmajor_abvs',
                    'diagnosis_abvs','update_by', 'last_update']
    elif module_name == 'ultrasound':
        col_list = ['file_number', 'reason_report', 'report_date', 'usg_status',
                    'usg_date', 'usg_breast', 'usg_mass', 'usg_mass_number',
                    'usg_mass_location', 'usg_mass_clock', 'usg_mass_quadrant',
                    'usg_mass_shape', 'usg_mass_margin', 'usg_mass_echo',
                    'usg_mass_size', 'usg_mass_size_unit', 'usg_calc',
                    'usg_calc_type', 'usg_vascularity', 'usg_birad',
                    'usg_node_description', 'usg_node_size',
                    'usg_node_size_unit', 'e_b_ratio', 'e_b_ratio_description',
                    'shear_wave_mu', 'usg_impression', 'update_by',
                    'last_update']
    elif module_name == 'mri':
        col_list = ['file_number', 'reason_report', 'report_date',
                    'mri_status', 'date_mri', 'accession_number_mri',
                    'mri_breast', 'fibroglandular_tissue_mri',
                    'background_paranchymal_enhancement_level_mri',
                    'background_paranchymal_enhancement_symmetry_mri',
                    'focus_mri', 'mass_mri', 'number_mass_mri',
                    'mass_location_mri', 'mass_shape_mri', 'mass_margin_mri',
                    'mass_internal_enhancement_char_mri',
                    'asso_features_nipple_retraction_mri',
                    'asso_features_nipple_invasion_mri',
                    'asso_features_skin_retraction_mri',
                    'asso_features_skin_thickening_mri',
                    'asso_features_axillary_adenopathy_mri',
                    'asso_features_pectoralismuscle_invasion_mri',
                    'asso_features_chestwall_invasion_mri',
                    'asso_features_architectural_distortion_mri',
                    'asso_features_skin_invasion_mri', 'fat_lesion_mri',
                    'kinetics_initial_mri', 'kinetics_delayed_mri',
                    'non_enhanced_features_mri', 'implant_mri', 'lesion_mri',
                    'lesion_location_mri', 'lesion_depth_mri',
                    'lesion_size_mri', 'distancefromskin_mri',
                    'distancefrompectmaj_mri', 'mri_birad',
                    'user_name_mri', 'last_update_mri']
    else:
        col_list = 'file_number'
    return col_list


def names_radio_mass(module_name):
    if module_name == 'ultrasound':
        col_list = ['file_number', 'mass_id', 'mass_location',
                    'mass_location_clock', 'mass_quadrant', 'mass_shape',
                    'mass_margin', 'mass_echo', 'mass_size',
                    'mass_size_unit', 'update_by', 'last_update']
    elif module_name == 'mammography':
        col_list = ['file_number', 'mass_id', 'mass_location', 'mass_quad',
                    'mass_shape', 'mass_margin', 'mass_distance_nipple',
                    'mass_dimension', 'mass_longest_dimension',
                    'mass_size_unit', 'modality', 'update_by', 'last_update']
    elif module_name == 'calcification_mammography':
        col_list = ['file_number', 'calcification_id',
                    'calcification_location', 'calcification_type',
                    'calicification_comments', 'update_by',
                    'last_update']
    elif module_name == 'mri':
        col_list = ['file_number', 'mass_location', 'mass_name', 'mass_id',
                    'image_type', 'enhancement_type', 'location_clock',
                    'mass_quadrant', 'mass_shape', ' mass_margin', 'mass_echo',
                    'mass_dimension', 'mass_longest_dimension',
                    'mass_size_unit', 'modality', 'update_by', 'last_update']
    else:
        col_list = 'file_number'
    return col_list


def names_radio_calc():
    col_list = ['file_number', 'calcification_id', 'calcification_location',
                'calcification_type', 'calicification_comments']
    return col_list

# def names_biopsy(module_name):
#    if module_name == 'biopsy_report_info':
#        col_list = ['consent_status_biopsy', 'consent_form_status_biopsy', 'block_sr_number_biopsy',
#                    'block_location_id_biopsy', 'block_current_location_biopsy', 'biopsy_report_in_pccm',
    #                    'biopsy_block_id', 'no_of_blocks_biopsy', 'date_of_biopsy', 'lab_id_biopsy', 'biopsy_type']
    #    elif module_name == 'tumour_biopsy_data':
    #        col_list = ['tumour_biopsy_diagnosis', 'tumour_biopsy_diagnosis_grade', 'lymphovascular_emboli_biopsy',
    #                    'dcis_biopsy', 'ihc_report_custody_biopsy', 'tumour_biopsy_er', 'tumour_biopsy_er_percent',
#                    'tumour_biopsy_pr', 'tumour_biopsy_pr_percent', 'tumour_biopsy_her2', 'tumour_biopsy_her2_grade',
#                    'tumour_biopsy_fish', 'tumour_biopsy_ki67_percent']
#    elif module_name == 'lymphnode_biopsy':
#        col_list = ['lymph_node_biopsy_fnac', 'lymph_node_biopsy_location', 'lymph_node_biopsy_diagnosis', 'update_by',
    #                    'last_update']
    #    else:
    #        col_list = 'file_number'
#    return col_list

def block_list(module_name):
    if module_name == 'all':
        col_list = ['file_number', 'patient_name', 'mr_number',
                    'date_of_birth', 'date_first_visit',
                    'block_sr_number', 'block_location', 'block_type',
                    'block_id', 'current_block_location',
                    'blocks_received_at_pccm', 'number_of_blocks',
                    'block_series', 'consent_discussed', 'consent',
                    'update_by', 'last_update']
    elif module_name == 'research':
        col_list = ['block_sr_number', 'block_type', 'block_id',
                    'block_series', 'number_of_blocks',
                    'current_block_location', 'consent_discussed',
                    'consent', 'update_by', 'last_update']
    else:
        col_list = ['file_number']
    return col_list


def info_print_all(module_name):
    if module_name == 'print_edit':
        nut_supp = ['nutritional supplements', 'type of nutritional supplements',
                    'quantity  of nutritional supplements', 'duration of use']
        phys_act = ['physical activity', 'type of physical activity', 'frequency of physical activity']
        med_history = ['other medical history', 'type of medical history', 'date of diagnosis', 'treatment']
        cancer_history = ['previous cancer history', 'type of previous cancer',
                          'year of diagnosis', 'treatment taken',
                          'details of treatment taken', 'duration of treatment']
        family_details = ['marital_status', 'siblings', 'sisters', 'brothers',
                          'children', 'daughters', 'sons', 'age at menarche (yrs)',
                          'menopausal status', 'age at menopause (yrs)',
                          'date of last menstrual period', 'period type',
                          'number of pregnancies', 'pregnancy carried to term (includes abortion after 6 months)', 'number of  abortions',
                          'age of first child', 'age at first pregnancy', 'age of last child', 'age at last pregnancy',
                          'twice births in year', 'breast feeding', 'child breast feeding',
                          'duration of breast feeding', 'breast usage for breast feeding', 'fertility treatment',
                          'type of fertility treatment', 'details of fertility treatment',
                          'cycles of fertility treatment', 'successful fertility treatment',
                          'type of birth control used', 'details of birth control used', 'duration of birth control']
        breast_symptoms = ['right breast symptoms', 'duration of symptoms in right breast', 'left breast symptoms',
                           'duration of symptoms in left breast', 'other symptoms in right breast',
                           'duration of other symptoms in right breast', 'other symptoms in left breast',
                           'duration of other symptoms in left breast', 'metastasis symptoms']
        update = ['updated by', 'date and time of update']
        habits = ['diet', 'alcohol consumption', 'alcohol consumption since age (yrs)',
                  'quantity of alcohol consumed per week', 'duration of alcohol consumption', 'additional comments',
                  'tobacco', 'mode of exposure to tobacco', 'type of passive tobacco exposure',
                  'type of tobacco consumed/exposed to', 'tobacco consumption since age (yrs)',
                  'frequency of tobacco consumption', 'quantity of tobacco consumed per week',
                  'duration tobacco of tobacco consumption', 'additional comments', 'other deleterious habits']
        det_by = ['current breast cancer detected by', 'date of current breast cancer detection']
        family_cancer = ['family cancer history',
                         'type of cancer | degree of relation | type of relation | age at diagnosis']
        bio_info = ['medical record number', 'name', 'aadhaar card number', 'date of first visit', 'permanent address',
                    'current address', 'phone number', 'email id', 'gender', 'current age (yrs)',
                    'age at cancer diagnosis', 'date of birth', 'place of birth', 'height (cm)', 'weight (kg)', 'bmi']
        col_list = bio_info + nut_supp + phys_act + habits + family_details + med_history + cancer_history + \
                   family_cancer + det_by + breast_symptoms + update
    elif module_name == 'det_by':
        col_list = ['current breast cancer detected by', 'date of current breast cancer detection']
    elif module_name == 'nut_supplements':
        col_list = ['nutritional supplements', 'type of nutritional supplements',
                    'quantity  of nutritional supplements', 'duration of use']
    elif module_name == 'phys_act':
        col_list = ['physical activity', 'type of physical activity', 'frequency of physical activity']
    elif module_name == 'med_history':
        col_list = ['other medical history', 'type of medical history', 'date of diagnosis', 'treatment']
    elif module_name == 'cancer_history':
        col_list = ['previous cancer history', 'type of previous cancer', 'year of diagnosis', 'treatment taken',
                    'details of treatment taken', 'duration of treatment']
    elif module_name == 'family_details':
        col_list = ['marital_status', 'siblings', 'sisters', 'brothers', 'children', 'daughters', 'sons',
                    'age at menarche (yrs)', 'menopausal status', 'age at menopause (yrs)',
                    'date of last menstrual period', 'period type', 'number of pregnancies',
                    'pregnancy carried to term (includes abortion after 6 months)', 'number of abortions',
                    'age of first child', 'age at first pregnancy', 'age of last child', 'age at last pregnancy',
                    'twice births in year', 'breast feeding', 'child breast feeding', 'duration of breast feeding',
                    'breast usage for breast feeding', 'fertility treatment', 'type of fertility treatment',
                    'details of fertility treatment', 'cycles of fertility treatment', 'successful fertility treatment',
                    'type of birth control used', 'details of birth control used', 'duration of birth control']
    elif module_name == 'breast_symptoms':
        col_list = ['right breast symptoms', 'duration of symptoms in right breast', 'left breast symptoms',
                    'duration of symptoms in left breast', 'other symptoms in right breast',
                    'duration of other symptoms in right breast', 'other symptoms in left breast',
                    'duration of other symptoms in left breast', 'metastasis symptoms', 'updated by',
                    'date and time of update']
    elif module_name == 'habits':
        col_list = ['diet', 'alcohol consumption', 'alcohol consumption since age (yrs)',
                    'quantity of alcohol consumed per week', 'duration of alcohol consumption', 'additional comments',
                    'tobacco', 'mode of exposure to tobacco', 'type of passive tobacco exposure',
                    'type of tobacco consumed/exposed to', 'tobacco consumption since age (yrs)',
                    'frequency of tobacco consumption', 'quantity of tobacco consumed per week',
                    'duration tobacco of tobacco consumption', 'additional comments', 'other deleterious habits']
    elif module_name == 'family_cancer':
        col_list = ['family cancer history', 'type of cancer | degree of relation | type of relation | age at diagnosis'
                    ]
    elif module_name == 'bio_info':
        col_list = ['medical record number', 'name', 'aadhaar card number', 'date of first visit', 'permanent address',
                    'current address', 'phone number', 'email id', 'gender', 'current age (yrs)',
                    'age at diagnosis (yrs)', 'date of birth', 'place of birth', 'height (cm)', 'weight (kg)', 'bmi']
    else:
        col_list = 'module not found'
    return col_list


def names_nact(module_name):
    if module_name == 'nact_tox_table':
        col_list = ['drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity', 'changedtreatment_toxicity']
    elif module_name == 'nact_drug_table':
        col_list = ['drugs_administered', 'number_cycle', 'cycle_frequency_per_week', 'drug_dose', 'dose_unit']
    elif module_name == 'neo_adjuvant_therapy':
        col_list = ['nact_status', 'place_nact', 'details_nact', 'plan_nact', 'date_start_nact',
                    'patient_weight_nact', 'nact_drugs_administered', 'number_cycles_nact', 'cycle_weekly_frequency',
                    'drugs_totaldose', 'drugs_unit', 'toxicity_type', 'toxicity_grade', 'toxicity_treatment',
                    'toxicity_response', 'toxicity_at_cycle', 'nact_change_due_to_toxicity',
                    'tumour_response_check_method', 'tumour_response_nact', 'tumour_size', 'tumour_size_unit',
                    'nact_response_impression', 'nact_response_node', 'date_tumour_size_checked',
                    'nact_completion_status', 'nact_end_date', 'trastuzumab_use_nact', 'trastuzumab_regime_nact',
                    'trastuzumab_courses_taken_nact', 'hormone_therapy_nact', 'hormone_therapy_type_nact', 'hormone_therapy_duration',
                    'horomone_therapy_side_effects', 'update_by', 'last_update']
    elif module_name == 'clip_information':
        col_list = ['clip_number', 'clip_date', 'clip_insertion_after_cycle']
    else:
        col_list = 'file_number'
    return col_list


def names_chemotherapy(module_name):
    if module_name == 'chemo_tox_table':
        col_list = ['drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity',
                    'changedtreatment_toxicity']
    elif module_name == 'chemo_drug_table':
        col_list = ['drug', 'number_cycle', 'cycle_frequency_per_week',
                    'drug_dose', 'dose_unit']
    elif module_name == 'adjuvant_chemotherapy':
        col_list = ['chemotherapy_status', 'place_chemotherapy',
                    'details_chemotherapy', 'plan_chemotherapy',
                    'date_start_chemotherapy', 'patient_weight_chemotherapy',
                    'drugs_administered', 'number_cycles_chemotherapy',
                    'cycle_weekly_frequency', 'drugs_totaldose', 'drugs_unit',
                    'toxicity_type', 'toxicity_grade', 'toxicity_treatment',
                    'toxicity_response', 'toxicity_at_cycle',
                    'chemotherapy_change_due_to_toxicity',
                    'chemotherapy_completion_status',
                    'chemotherapy_end_date', 'trastuzumab_use_chemotherapy',
                    'trastuzumab_regime_chemotherapy',
                    'trastuzumab_courses_taken_chemotherapy', 'ovary_status',
                    'hormone_therapy_chemotherapy',
                    'hormone_therapy_type_chemotherapy',
                    'hormone_therapy_duration_chemotherapy',
                    'horomone_therapy_side_effects_chemotherapy',
                    'update_by', 'last_update']
    elif module_name == 'tox_table':
        col_list = ['drug_administered', 'toxicity_type', 'toxicity_grade',
                    'treatment', 'response_treatment', 'cycle_toxicity',
                    'changedtreatment_toxicity']
    else:
        col_list = 'file_number'
    return col_list


def names_surgery_information(module_name):
    if module_name == 'surgery_information':
        col_list = ['surgery_date', 'surgery_hospital',
                    'surgery_patient_hospital_id', 'surgery_date_admission',
                    'surgery_hospital_ward', 'surgery_name_anaesthetist',
                    'surgery_name_surgeon', 'surgery_lesion_location',
                    'surgery_type', 'surgery_incision',
                    'surgery_type_subtype', 'surgery_type_level_subtype',
                    'oncoplastic_surgery_type', 'oncoplastic_surgery_flap',
                    'oncoplastic_surgery_plan',
                    'oncoplastic_surgery_tumour_filled_by',
                    'oncoplastic_surgery_nac_graft',
                    'oncoplastic_surgery_primary_pedicle',
                    'oncoplastic_surgery_secondary_pedicle',
                    'reconstruction_surgery_implant_type',
                    'reconstruction_surgery_implant_size',
                    'contralateral_surgery', 'contralateral_surgery_type',
                    'contralateral_surgery_type_details', 'surgery_notes']
    elif module_name == 'node_excision':
        col_list = ['guide_node_excision_surgery', 'frozen_samples_surgery',
                    'gross_tumour_size_surgery', 'skin_surgery',
                    'nodes_type_surgery', 'number_nodes_surgery',
                    'level_nodes_surgergy',
                    'sentinel_node_labelling_method_surgery',
                    'blue_node', 'hot_node', 'blue_hot_node',
                    'non_blue_hot_node', 'palpable_node']
    elif module_name == 'post_surgery':
        col_list = ['chemotherapy_plan', 'radiotherapy_plan', 'other_plans',
                    'drain_removal_date', 'total_drain_days',
                    'days_post_surgery_complications',
                    'post_surgery_complications',
                    'treatment_post_surgery_', 'complications',
                    'days_post_surgery_recurrence', 'recurrence_site',
                    'opd_notes', 'update_by', 'last_update']
    else:
        col_list = 'file_number'
    return col_list


def names_radiation():
    col_list = ['radiation_received', 'radiation_date', 'radiation_type',
                'imrt_dcrt', 'radiation_ipsilateral_breast',
                'radiation_ipsilateral_breast_dosage',
                'radiation_contralateral_breast',
                'radiation_contralateral_breast_dosage',
                'radiation_chest_wall', 'radiation_chest_wall_dosage',
                'radiation_supraclavicular_fossa',
                'radiation_supraclavicular_fossa_dosage', 'radiation_axilla',
                'radiation_axilla_dosage', 'radiation_other_location',
                'radiation_other_location_dosage',
                'radiation_ipsilateral_breast_boost',
                'radiation_ipsilateral_breast_boost_dosage',
                'radiation_contralateral_breast_boost',
                'radiation_contralateral_breast_boost_dosage',
                'radiation_chest_wall_boost',
                'radiation_chest_wall_boost_dosage',
                'radiation_supraclavicular_fossa_boost',
                'radiation_supraclavicular_fossa_boost_dosage',
                'radiation_axilla_boost', 'radiation_axilla_boost_dosage',
                'radiation_other_location_boost',
                'radiation_other_location_boost_dosage',
                'radiation_acute_toxicity', 'radiation_delayed_toxicity',
                'radiation_finish_date', 'radiation_location',
                'radiation_oncologist', 'update_by', 'last_update']
    return col_list


def name_follow_up():
    col_list = ['follow_up_period', 'follow_up_status',
                'follow_up_mammography_date', 'follow_up_mammography',
                'follow_up_usg_date', 'follow_up_usg', 'follow_up_other_test',
                'follow_up_other_test_date', 'follow_up_other_result',
                'follow_up_treatment', 'follow_up_treatment_result',
                'update_by', 'last_update']
    return col_list


def names_longterm(module_name):
    if module_name == 'hormone':
        col_list = ['hormone_indicated', 'hormone_recieved', 'hormone_date',
                    'hormone_type', 'hormone_duration_years',
                    'hormone_discontinued',
                    'hormone_ovary_surpression', 'hormone_therapy_outcome', 'hormone_followup',
                    'horomone_recurrence']
    elif module_name == 'metastasis':
        col_list = ['metastasis_exam', 'date_last_followup', 'time_to_recurrence', 'nature_of_recurrence',
                    'distant_site', 'patient_status_last_followup', 'update_by', 'last_update']
    else:
        col_list = 'file_number'
    return col_list


def name_ffpe_csv():
    col_list = ['patient_name', 'block_sr_number', 'block_location_id', 'block_current_location',
                'file_number', 'received_pccm_date', 'block_id', 'block_series', 'no_of_blocks',
                'block_type', 'input_file_name']
    return col_list


def db_tables():
    tables = ['patient_information_history', 'block_list', 'biopsy_path_report_data', 'clinical_exam', 'radiology',
              'pet_reports', 'neo_adjuvant_therapy', 'surgery_report', 'surgery_path_report_data',
              'adjuvant_chemotherapy', 'radiotherapy', 'hormonetherapy_survival', 'follow_up_data']
    return tables


def print_db_tables():
    tables = ['patient_information_history',
              'block_list',
              'biopsy_path_report_data',
              'clinical_exam',
              'mammography',
              'abvs',
              'ultrasound',
              'mri',
              'pet_reports',
              'neo_adjuvant_therapy',
              'surgery_report',
              'surgery_path_report_data',
              'adjuvant_chemotherapy',
              'radiotherapy',
              'hormonetherapy_survival',
              'follow_up_data']
    return tables


def ffpe_db_tables():
    tables = ['block_list', 'biopsy_path_report_data', 'surgery_path_report_data']
    return tables


def mutation_tables(table):
    if table == 'Germline_Mutations':
        col_list = ['germline_mutation_tested', 'sample_used', 'technology', 'sequenced_at_facility', 
                    'confirmed_by_re-testing', 'does_retesting_confirm_mutation_y_n', 'restesting_method', 'gene', 
                    'exon_number', 'nucleotide_position', 'nucleotide_before', 'nucleotide_after', 'aminoa_position', 
                    'amino_acid_before', 'amino_acid_after', 'variation_dna', 'zygosity', 'clinical_significance', 
                    'inheritance', 'transcript', 'cdna', 'effect_on_mrna', 'protein', 'effect_on_protein', 
                    'protein_databases_reference', 'ethnicities', 'variants_in_vicinity', 'remarks']
    elif table == 'Somatic_Mutations':
        col_list = ['somatic_mutation_tested', 'sample_used', 'percent_tumor_in_the_sample', 
                    'percent_tumor_identification_done_by', 'technology_used_for_germline_mutation_sequencing', 
                    'facility_somatic_mutation_sequenced_at', 'somatic_mutation_sequenced_confirmed_by_re-testing', 
                    'accession_number', 'run_id', 'panel', 'variant_call_id', 'gene', 'gsyntax', 'psyntax', 
                    'selected_psyntax', 'mutation_type', 'variant_classification', 'consequence', 'vaf', 
                    'frequency_from_data', 'dbsnp_frequency', 'exac_frequency', 'nhlbi_frequency', 'domain', 'pathways', 
                    'ethnicities', 'variants', 'remarks']
    else:
        col_list = 'file_number'
    return col_list


def names_biopsy(module_name):
    if module_name == 'biopsy_report_info':
        col_list = ['file_number', 'block_sr_number', 'block_location', 'current_block_location', 
                    'blocks_received_at_pccm', 'fnac_breast', 'fnac_breast_date', 'fnac_slide_id', 'fnac_diagnosis',
                    'fnac_diagnosis_comments', 'reason_path_report', 'biopsy_site', 'biopsy_report_pccm',
                    'biopsy_ihc_report_pccm', 'biopsy_block_id', 'biopsy_number_of_blocks', 'biopsy_block_series',
                    'biopsy_date', 'biopsy_block_source', 'biopsy_lab_id']
    elif module_name == 'biopsy_details':
        col_list = ['biopsy_type', 'biopsy_diagnosis', 'biopsy_comments', 'benign', 'biopsy_tumour_grade', 
                    'biopsy_lymph_emboli', 'dcis_biopsy']
    elif module_name == 'ihc_biopsy_data':
        col_list = ['biopsy_er', 'biopsy_er_percent', 'biopsy_pr', 'biopsy_pr_percent', 'biopsy_her2', 
                    'biopsy_her2_grade', 'biopsy_fish', 'biopsy_ki67', 'biopsy_subtype', 'fnac_lymph_node', 
                    'fnac_lymph_node_location', 'fnac_lymph_node_diagnosis', 'update_by', 'last_update']
    elif module_name == 'review_biopsy':
        col_list = ['review_biopsy_date', 'review_biopsy_source', 'review_biopsy_diagnosis',
                    'review_biopsy_diagnosis_comment', 'review_biopsy_block_id', 'review_biopsy_er',
                    'review_biopsy_er_percent', 'review_biopsy_pr', 'review_biopsy_pr_percent', 'review_biopsy_her2',
                    'review_biopsy_her2_grade', 'review_biopsy_fish', 'review_biopsy_ki67', 'review_update_by',
                    'review_last_update', 'surgery_block_id']
    else:
        col_list = 'file_number'
    return col_list


def names_surgery(module_name):
    if module_name == 'surgery_block_information_0':
        col_list = ['file_number', 'surgery_block_data_type', 'block_sr_number', 'block_location', 
                    'current_block_location', 'surgery_block_id', 'surgery_number_of_blocks', 'surgery_block_series',
                    'breast_cancer_yes_no', 'pathology_report_available_yes_no', 'neoadjuvant_therapy', 
                    'surgery_block_primary_tissue', 'surgery_block_source','date_of_surgery', 'surgeon_s',
                    'surgery_hospital_id', 'surgery_lesion_site', 'surgery_type']
    elif module_name == 'surgery_block_information_1':
        col_list = ['specimen_ressection_size','tumour_block_ref', 'margin_size','cut_margin_size', 'margin_report',
                    'node_block_ref', 'ad_normal_block_ref', 'red_tissue_block_ref', 'tumour_size', 'tumour_size_unit',
                    'tumour_grade', 'surgery_diagnosis', 'surgery_diagnosis_comments', 'dcis_yes_no', 'dcis_percent',
                    'surgery_perineural_invasion', 'surgery_necrosis', 'surgery_lymphovascular_invasion',
                    'percent_lymph_invasion', 'stromal_tils_percent', 'tumour_desmoplastic_response']
    elif module_name == 'surgery_block_information_2':
        col_list = ['surgery_er', 'surgery_er_percent', 'surgery_pr', 'surgery_pr_percent', 'surgery_her2', 
                    'surgery_her2_grade', 'surgery_fish', 'surgery_ki67', 'surgery_subtype', 
                    'sentinel_node_number_removed', 'sentinel_node_number_positive', 'axillary_node_number_removed', 
                    'axillary_node_number_positive', 'apical_node_number_removed', 'apical_node_number_positive', 
                    'surgery_perinodal_spread', 'pathological_pt', 'pathological_pn', 'metastasis', 
                    'pathological_stage', 'clinical_stage', 'update_by', 'last_update']
    elif module_name == 'surgery_block_information_3':
        col_list = ['review_surgery_date', 'review_surgery_source', 'review_surgery_diagnosis',
                    'review_surgery_diagnosis_comment', 'review_surgery_block_id', 'review_surgery_er',
                    'review_surgery_er_percent', 'review_surgery_pr', 'review_surgery_pr_percent',
                    'review_surgery_her2', 'review_surgery_her2_grade', 'review_surgery_fish', 'review_surgery_ki67',
                    'review_update_by', 'review_last_update']
    elif module_name == 'block_type_list':
        col_list = ['tumour', 'node', 'adjacent_normal', 'reduction_tissue']
    elif module_name == 'block_data':
        col_list = ['fk', 'file_number', 'block_id', 'block_reference', 'block_type', 'block_description', 'update_by',
                    'last_update']
    else:
        col_list = 'file_number'
    return col_list


def names_pet(module_name):
    if module_name == 'pet_report_identifier':
        col_list = ['file_number', 'pet_scan_date', 'pet_scan_number', 'pet_scan_source', 'pet_scan_reg_number',
                    'pet_scan_history','pet_carcinoma_status', 'pet_cancer_location', 'pet_recurrence_known',
                    'pet_procedure_body_region', 'pet_procedure_fdg_dose_mci', 'pet_procedure_bsl', 'pet_scanner_name',
                    'pet_procedure_additional_notes']
    elif module_name == 'pet_report_findings':
        col_list = ['pet_general_findings', 'pet_head_neck_normal_report', 'pet_head_neck_abnormal_report',
                    'pet_thorax_normal_report', 'pet_thorax_abnormal_report', 'pet_abdomen_pelvis_normal_report',
                    'pet_abdomen_pelvis_abnormal_report', 'pet_musculoskeletal_normal_report',
                    'pet_musculoskeletal_abnormal_report', 'pet_impression', 'pet_primary_disease_yes_no',
                    'pet_local_spread', 'pet_recurrence_yes_no', 'pet_distant_metastasis']
    elif module_name == 'pet_breast_cancer':
        col_list = ['pet_breast_lesion_size', 'pet_breast_lesion_size_unit', 'pet_breast_lesion_suv',
                    'pet_breast_lesion_location', 'pet_breast_lesion_comments','pet_breast_lesion_type',
                    'pet_breast_nodes_description', 'pet_breast_lesion_skin', 'update_by', 'last_update']
    else:
        col_list = ['file_number']
    return col_list

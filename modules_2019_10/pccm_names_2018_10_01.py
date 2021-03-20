def names_info(module_name):
    if module_name == "nut_supplements":
        col_list = ["Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements",
                    "Duration_Nutritional_supplements"]
    elif module_name == "phys_act":
        col_list = ["Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"]
    elif module_name == "med_history":
        col_list = ["Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History",
                    "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"]
    elif module_name == "cancer_history":
        col_list = ["Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer",
                    "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer", "Treatment_Duration_Previous_Cancer"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period",
                    "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child",
                    "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year",
                    "Breast_feeding", "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding",
                    "Fertility_treatment_y_n", "Type_fertility_treatment", "Details_fertility_treatment",
                    "Cycles_fertility_treatment", "Success_fertility_treatment", "Type_birth_control_used",
                    "Details_birth_control", "Duration_birth_control"]
    elif module_name == "breast_symptoms":
        col_list = ["RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration", "RB_Other_Symptoms",
                    "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration",
                    "Metastasis_Symptoms", "update_by", "last_update"]
    elif module_name == "habits":
        col_list = ["Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week",
                    "Duration_alcohol", "Comments_alcohol", "Tobacco_y_n", "Exposure_Mode", "Type_Passive",
                    "Type_tobacco", "Tobacco_consumption_age_yrs", "Tobacco_Frequency", "Quantity_tobacco_per_week",
                    "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"]
    elif module_name == "det_by":
        col_list = ["Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"]
    elif module_name == "family_cancer":
        col_list = ["FamilyCancer_history_y_n", "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"]
    elif module_name == "bio_info":
        col_list = ["MR_number", "Name", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address", "Current_Address",
                    "Phone", "Email_ID", "Gender", "Age_at_First_Visit_yrs", "Diagnosis_Age_yrs","Date_of_Birth",
                    "Place_Birth", "Height_cm", "Weight_kg","BMI"]
    elif module_name == "general_table":
        col_list = ["File_number, Condition, Diagnosis_date, Treatment"]
    elif module_name == "family_cancer":
        col_list = ['File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs']
    elif module_name == "previous_cancer":
        col_list = ["File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation,"
                    "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone,"
                    "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy,"
                    "Type_HomeRemedy,Duration_HomeRemedy"]
    elif module_name == "nut_sup":
        col_list = ["File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, "
                    "Duration_nutritional_supplements"]
    elif module_name == "phys_act_table":
        col_list = ["File_number, Type_activity, Frequency_activity"]
    elif module_name == "breast_feed":
        col_list = ["File_number, Child_number, Feeding_duration, Breast_usage_feeding"]
    elif module_name == 'bio_info_without_personal_info':
        col_list = ["FirstVisit_Date", "Gender", "Age_at_First_Visit_yrs", "Diagnosis_Age_yrs","Date_of_Birth",
                    "Height_cm", "Weight_kg","BMI"]
    else:
        col_list = "File_number"
    return col_list

def names_info_form_version(module_name):
    if module_name == "nut_supplements":
        col_list = ["Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements",
                    "Duration_Nutritional_supplements"]
    elif module_name == "phys_act":
        col_list = ["Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"]
    elif module_name == "med_history":
        col_list = ["Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History",
                    "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"]
    elif module_name == "cancer_history":
        col_list = ["Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer",
                    "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer", "Treatment_Duration_Previous_Cancer"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period",
                    "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child",
                    "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year",
                    "Breast_feeding", "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding",
                    "Fertility_treatment_y_n", "Type_fertility_treatment", "Details_fertility_treatment",
                    "Cycles_fertility_treatment", "Success_fertility_treatment", "Type_birth_control_used",
                    "Details_birth_control", "Duration_birth_control"]
    elif module_name == "breast_symptoms":
        col_list = ["RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration", "RB_Other_Symptoms",
                    "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration",
                    "Metastasis_Symptoms", "update_by", "last_update"]
    elif module_name == "habits":
        col_list = ["Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week",
                    "Duration_alcohol", "Comments_alcohol", "Tobacco_y_n", "Exposure_Mode", "Type_Passive",
                    "Type_tobacco", "Tobacco_consumption_age_yrs", "Tobacco_Frequency", "Quantity_tobacco_per_week",
                    "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"]
    elif module_name == "det_by":
        col_list = ["Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"]
    elif module_name == "family_cancer":
        col_list = ["FamilyCancer_history_y_n", "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"]
    elif module_name == "bio_info":
        col_list = ["MR_number", "Name", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address", "Current_Address",
                    "Phone", "Email_ID", "Gender", "Age_at_First_Visit_yrs", "Diagnosis_Age_yrs","Date_of_Birth",
                    "Place_Birth", "Height_cm", "Weight_kg","BMI"]
    elif module_name == "general_table":
        col_list = ["File_number, Condition, Diagnosis_date, Treatment"]
    elif module_name == "family_cancer":
        col_list = ['File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs']
    elif module_name == "previous_cancer":
        col_list = ["File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation,"
                    "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone,"
                    "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy,"
                    "Type_HomeRemedy,Duration_HomeRemedy"]
    elif module_name == "nut_sup":
        col_list = ["File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, "
                    "Duration_nutritional_supplements"]
    elif module_name == "phys_act_table":
        col_list = ["File_number, Type_activity, Frequency_activity"]
    elif module_name == "breast_feed":
        col_list = ["File_number, Child_number, Feeding_duration, Breast_usage_feeding"]
    else:
        col_list = "File_number"
    return col_list

def name_clinical(module_name):
    if module_name == "clinical_exam_initial":
        col_list = ["Consent_Status", "Consent_form_status", 'Provisional_Diagnosis_Clinical_Examination_CE',
                    'Lump_Palpable_CE', 'Lump_Location_CE', 'Lump_Size_CE', 'Lump_Number_CE', 'Lump_Consistency_CE',
                    'Lump_Fixity_CE', 'Mastitis_CE', 'Mastitis_type_CE', 'Tenderness_CE', 'Nipple_Retraction_CE',
                    'Nipple_Discharge_CE', 'Nipple_Discharge_Type_CE', 'Skin_changes_CE', 'Skin_change_type_CE',
                    'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE',
                    'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE',
                    'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE',
                    'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE',
                    'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE',
                    'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE',
                    'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE', 'Follow_up_advised_CE',"update_by", "last_update"]
    elif module_name == "nipple_cytology":
        col_list = ["Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"]
    elif module_name == "other_test":
        col_list = ["USG_Abdomen", "Diagnosis_USG_Abdomen", "Details_Diagnosis_USG_Abdomen", "CECT_Abd_Thorax", "Visceral_Metastasis_CECT_Abd_Thorax",
                    "Details_Visceral_Metastasis_CECT_Abd_Thorax", "PET_Scan", "Visceral_Metastasis_PET_Scan", "Detail_Visceral_Metastasis_PET_Scan",
                    "Skeletal_Metastasis_PET_Scan", "Detail_Skeletal_Metastasis_PET_Scan", "Bone_Scan", "Skeletal_Metastasis_Bone_Scan",
                    "Detail_Skeletal_Metastasis_Bone_Scan"]
    else:
        col_list = "File_number"
    return col_list

def names_radio(module_name):
    if module_name == "mammography":
        col_list = ['Mammography','Mammography_Date', 'Mammography_Place', 'Mammography_Indication', 'Mammography_Breast',
                    'Mammography_MassNumber', 'Mammography_MassLocation', 'Mammography_MassShape',
                    'Mammography_MassMargin', 'Mammography_MassNipple_cm', 'Mammography_MassSize' ,
                    'Mammography_MassSize_unit', 'Mammography_CalcificationNumber', 'Mammography_CalcificationLocation',
                    'Mammography_Skin_Lesion','Mammography_CalcificationType', 'Mammography_Birad','Mammography_Impression',
                    'Tomography_y_n']
    elif module_name == "abvs":
        col_list = ["Automated_Breast_Volume_Scanner_ABVS", "Date_ABVS", "Accession_ABVS", "Lesion_ABVS",
                    "Lesion_Location_ABVS", "Size_ABVS", "Distance_ABVS", "Distance_PectMajor_ABVS", "Diagnosis_ABVS"]
    elif module_name == "sonomammo":
        col_list = ['SonoMammography', 'Sonomammo_Date', 'Sonomammo_Breast', 'Sonomammo_Mass', 'Sonomammo_Mass_Number',
                    'Sonomammo_Mass_Location', 'Sonomammo_Mass_Clock','Sonomammo_Mass_Shape', 'Sonomammo_Mass_Margin',
                    'Sonomammo_Mass_Echo', 'Sonomammo_Mass_Size', 'Sonomammo_Mass_Size_Unit', 'Sonomammo_Calc', 'Sonomammo_Calc_Type',
                    'Sonomammo_Vascularity', 'Sonomammo_Birad', 'Sonomammo_Impression', "update_by", "last_update"]
    elif module_name == "mri_breast":
        col_list = ['MRI', 'Date_MRI_Breast', 'AccessionNumber_MRI_Breast', 'MRI_Breast', 'Fibroglandular_Tissue_MRI_Breast',
                    'Background_Paranchymal_Enhancement_Level_MRI_Breast',
                    'Background_Paranchymal_Enhancement_Symmetry_MRI_Breast', 'Focus_MRI_Breast', 'Mass_MRI_Breast',
                    'Number_Mass_MRI_Breast', 'Mass_Location_MRI_Breast','Mass_Shape_MRI_Breast',
                    'Mass_Margin_MRI_Breast', 'Mass_Internal_Enhancement_Char_MRI_Breast',
                    'Asso_features_Nipple_retraction_MRI_Breast', 'Asso_features_Nipple_invasion_MRI_Breast',
                    'Asso_features_Skin_retraction_MRI_Breast', 'Asso_features_Skin_thickening_MRI_Breast',
                    'Asso_features_Axillary_adenopathy_MRI_Breast',
                    'Asso_features_PectoralisMuscle_Invasion_MRI_Breast', 'Asso_features_ChestWall_Invasion_MRI_Breast',
                    'Asso_features_Architectural_distortion_MRI_Breast', 'Asso_features_Skin_Invasion_MRI_Breast',
                    'Fat_Lesion_MRI_Breast', 'Kinetics_Initial_MRI_Breast', 'Kinetics_Delayed_MRI_Breast',
                    'Non_Enhanced_Features_MRI_Breast', 'Implant_MRI_Breast', 'Lesion_MRI_Breast',
                    'Lesion_Location_MRI_Breast', 'Lesion_Depth_MRI_Breast', 'Lesion_Size_MRI_Breast',
                    'DistancefromSkin_MRI_Breast', 'DistanceFromPectMaj_MRI_Breast', 'Category_BI_RADS_MRI_Breast',
                    'user_name_mri', 'last_update_mri']
    else:
        col_list = "File_number"
    return col_list

def names_radio_df (module_name):
    if module_name == "SonnoMammography_Mass":
        col_list = ["Mass_ID", 'Mass_Location', 'Mass_Location_Clock','Mass_Shape', 'Mass_Margin', 'Mass_Echo',
                    'Mass_Size', 'Mass_Size_Unit']
    elif module_name == "Mammography_Mass":
        col_list = ["Mass_ID", 'Mass_Location', 'Mass_Shape', 'Mass_Margin', 'Mass_Distance_Nipple',
                    'Mass_Size', 'Mass_Size_Unit']
    elif module_name == "Calcification_Mammography":
        col_list = ["File_number", "Calcification_ID", 'Calcification_Location', 'Calcification_Type']
    elif module_name == "MRI_Mass":
        col_list = ["Mass_ID", 'Mass_Location', 'Mass_Shape', 'Mass_Margin',
                    'Mass_Internal_Enhancement_Char']
    else:
        col_list = "File_number"
    return col_list


def names_biopsy (module_name):
    if module_name == "biopsy_report_info":
        col_list = ["Consent_Status_Biopsy", "Consent_form_status_biopsy", "Block_SR_Number_Biopsy",
                    "Block_Location_ID_Biopsy", "Block_Current_Location_Biopsy", "Biopsy_Report_in_PCCM",
                    "Biopsy_Block_ID", "No_of_blocks_Biopsy", "Date_of_Biopsy", "Lab_ID_Biopsy", "Biopsy_Type"]
    elif module_name == "tumour_biopsy_data":
        col_list = ["Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Lymphovascular_emboli_biopsy",
                    "DCIS_biopsy", "IHC_report_custody_biopsy", "Tumour_biopsy_ER", "Tumour_biopsy_ER_Percent",
                    "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", "Tumour_biopsy_HER2_Grade",
                    "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"]
    elif module_name == "lymphnode_biopsy":
        col_list = ["Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis", "update_by",
                    "last_update"]
    else:
        col_list = "File_number"
    return col_list


def names_surgery(module_name):
    if module_name == "surgery_block_information_1":
        col_list = ['Block_Type_Surgery_Block', 'Block_SR_Number_Surgery_Block', 'Block_ID_Surgery_Block',
                    'Number_Blocks_Surgery_Block', 'Breast_Cancer_Yes_No_Surgery_Block',
                    'Pathology_Report_available_Yes_No_Surgery_Block', 'Pathology_Lab_Surgery_Block', 'Date_Surgery',
                    'Name_Surgeon', 'Surgery_Hospital_ID', 'Surgery_Lesion_Side', 'NACT', 'Type_Surgery']
    elif module_name == "surgery_block_information_2":
        col_list = [ 'Tumor_block_ref_Surgery_Block', 'Nodes_block_ref_Surgery_Block',
                     'Ad_Normal_block_ref_Surgery_Block', 'Reduction_tissue_block_ref_Surgery_Block',
                     'Tumour_size_Surgery_Block', 'Tumour_size_unit_Surgery_Block', 'Tumour_Grade_Surgery_Block',
                     'Diagnosis_Surgery_Block', 'DCIS_Surgery_Block_yes_no', 'DCIS_Type_Surgery_Block',
                     'DCIS_Percent_Surgery_Block', 'Tumour_Invasion_Surgery_Block', 'Perineural_Invasion_yes_no',
                     'Necrosis_yes_no', 'Vascular_Invasion_Percent_Surgery_Block',
                     'Lymphocyte_Invasion_Percent_Surgery_Block', 'Stroma_Percent_Surgery_Block',
                     'Surgery_Block_Margins_free_involved', 'Involved_Margin_Surgery_Block',
                     'Involved_Margin_Type_Surgery_Block']
    elif module_name == "surgery_block_information_3":
        col_list = ['Tumor_ER_Surgery_Block', 'Tumor_ER_percent_Surgery_Block', 'Tumor_PR_Surgery_Block',
                    'Tumor_PR_percent_Surgery_Block', 'Tumor_HER2_Surgery_Block', 'Tumor_HER2_grade_Surgery_Block',
                    'Tumor_FISH_Surgery_Block', 'Tumor_Ki67_percent_Surgery_Block', 'Sentinel_Node_positive_negative',
                    'Sentinel_Node_Removed', 'Sentinel_Node_Positive', 'Axillary_Node_positive_negative',
                    'Axillary_Node_Removed', 'Axillary_Node_Positive', 'Apical_Node_positive_negative',
                    'Apical_Node_Removed', 'Apical_Node_Positive', 'Perinodal_Spread_Node_yes_no',
                    'Supraclavicular_Involved_Node_yes_no']
    elif module_name == "path_stage":
        col_list = ['pT_Surgery_Block', 'pN_Surgery_Block', 'M_Surgery_Block', 'pTNM_Status_Surgery_Block',
                    'Clinical_Staging_Surgery_Block', "update_by", "last_update"]
    elif module_name == 'block_type_list':
        col_list = ["Tumour", "Node", "Adjacent Normal", "Reduction Tissue"]
    elif module_name == 'block_data':
        col_list = ['File_number', 'block_id', 'block_reference', 'block_type', 'block_description']
    elif module_name == 'diagnosis':
        col_list = ['Ductal carcinoma in situ(DCIS)', 'Invasive Ductal Carcinoma', 'Lobular Carcinoma in Situ (LCS)',
                    'Invasive Lobular Carcinoma (ILC)', 'Granulamatous Mastitis', 'Papillary Carcinoma',
                    'Phylloid Carcinoma', 'Invasive Mammary Carcinoma',  'Invasive Breast Carcinoma']
    else:
        col_list = "File_number"
    return col_list


def info_print_all(module_name):
    if module_name == "Print_edit":
        nut_supp = ["Nutritional supplements", "Type of Nutritional supplements",
                    "Quantity  of Nutritional supplements", "Duration of use"]
        phys_act = ["Physical Activity", "Type of Physical Activity", "Frequency of Physical Activity"]
        med_history = ["Other Medical History", "Type of Medical History", "Date of Diagnosis", "Treatment"]
        cancer_history = ["Previous Cancer History", "Type of Previous Cancer", "Year of Diagnosis", "Treatment taken",
                          "Details of Treatment taken", "Duration of Treatment"]
        family_details = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                          "Age at Menarche (yrs)", "Menopausal Status", "Age at Menopause (yrs)",
                          "Date of last menstrual period", "Period Type", "Number of pregnancies",
                          "Pregnancy carried to term (includes abortion after 6 months)", "Number of abortions",
                          "Age of first child", "Age at first pregnancy", "Age of last child", "Age at last pregnancy",
                          "Twice births in year", "Breast feeding", "Child Breast feeding",
                          "Duration of Breast feeding", "Breast Usage for Breast feeding", "Fertility treatment",
                          "Type of fertility treatment", "Details of fertility treatment",
                          "Cycles of fertility treatment", "Successful fertility treatment",
                          "Type of birth control used", "Details of birth control used", "Duration of birth control"]
        breast_symptoms = ["Right Breast symptoms", "Duration of symptoms in Right Breast", "Left Breast symptoms",
                           "Duration of symptoms in Left Breast", "Other Symptoms in Right Breast",
                           "Duration of other symptoms in Right Breast", "Other Symptoms in Left Breast",
                           "Duration of other symptoms in Left Breast", "Metastasis Symptoms"]
        update = ["Updated By", "Date and time of Update"]
        habits = ["Diet", "Alcohol Consumption", "Alcohol Consumption since age (yrs)",
                  "Quantity of alcohol consumed per week", "Duration of alcohol consumption", "Additional comments",
                  "Tobacco", "Mode of Exposure to Tobacco", "Type of Passive Tobacco Exposure",
                  "Type of tobacco consumed/exposed to", "Tobacco consumption since age (yrs)",
                  "Frequency of Tobacco consumption", "Quantity of tobacco consumed per week",
                  "Duration tobacco of tobacco consumption", "Additional Comments", "Other Deleterious Habits"]
        det_by = ["Current Breast Cancer Detected By", "Date of Current Breast Cancer Detection"]
        family_cancer = ["Family Cancer History",
                         "Type of Cancer | Degree of Relation | Type of Relation | Age at diagnosis"]
        bio_info = ["Medical Record Number", "Name", "Aadhaar Card Number", "Date of First Visit", "Permanent Address",
                    "Current Address", "Phone Number", "Email ID", "Gender", "Current Age (yrs)",
                    "Age at Cancer Diagnosis", "Date of Birth", "Place of Birth", "Height (cm)", "Weight (kg)", "BMI"]
        col_list = bio_info + nut_supp + phys_act + habits + family_details + med_history + cancer_history + \
            family_cancer + det_by + breast_symptoms + update
    elif module_name == "det_by":
        col_list = ["Current Breast Cancer Detected By", "Date of Current Breast Cancer Detection"]
    elif module_name == "nut_supplements":
        col_list = ["Nutritional supplements", "Type of Nutritional supplements",
                    "Quantity  of Nutritional supplements", "Duration of use"]
    elif module_name == "phys_act":
        col_list = ["Physical Activity", "Type of Physical Activity", "Frequency of Physical Activity"]
    elif module_name == "med_history":
        col_list = ["Other Medical History", "Type of Medical History", "Date of Diagnosis", "Treatment"]
    elif module_name == "cancer_history":
        col_list = ["Previous Cancer History", "Type of Previous Cancer", "Year of Diagnosis", "Treatment taken",
                    "Details of Treatment taken", "Duration of Treatment"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Age at Menarche (yrs)", "Menopausal Status", "Age at Menopause (yrs)",
                    "Date of last menstrual period", "Period Type", "Number of pregnancies",
                    "Pregnancy carried to term (includes abortion after 6 months)", "Number of abortions",
                    "Age of first child", "Age at first pregnancy", "Age of last child", "Age at last pregnancy",
                    "Twice births in year", "Breast feeding", "Child Breast feeding", "Duration of Breast feeding",
                    "Breast Usage for Breast feeding", "Fertility treatment", "Type of fertility treatment",
                    "Details of fertility treatment", "Cycles of fertility treatment", "Successful fertility treatment",
                    "Type of birth control used", "Details of birth control used", "Duration of birth control"]
    elif module_name == "breast_symptoms":
        col_list = ["Right Breast symptoms", "Duration of symptoms in Right Breast", "Left Breast symptoms",
                    "Duration of symptoms in Left Breast", "Other Symptoms in Right Breast",
                    "Duration of other symptoms in Right Breast", "Other Symptoms in Left Breast",
                    "Duration of other symptoms in Left Breast", "Metastasis Symptoms", "Updated By",
                    "Date and time of update"]
    elif module_name == "habits":
        col_list = ["Diet", "Alcohol Consumption", "Alcohol Consumption since age (yrs)",
                    "Quantity of alcohol consumed per week", "Duration of alcohol consumption", "Additional comments",
                    "Tobacco", "Mode of Exposure to Tobacco", "Type of Passive Tobacco Exposure",
                    "Type of tobacco consumed/exposed to", "Tobacco consumption since age (yrs)",
                    "Frequency of Tobacco consumption", "Quantity of tobacco consumed per week",
                    "Duration tobacco of tobacco consumption", "Additional Comments", "Other Deleterious Habits"]
    elif module_name == "family_cancer":
        col_list = ["Family Cancer History", "Type of Cancer | Degree of Relation | Type of Relation | Age at diagnosis"
                    ]
    elif module_name == "bio_info":
        col_list = ["Medical Record Number", "Name", "Aadhaar Card Number", "Date of First Visit", "Permanent Address",
                    "Current Address", "Phone Number", "Email ID", "Gender", "Current Age (yrs)",
                    "Age at diagnosis (yrs)", "Date of Birth", "Place of Birth", "Height (cm)", "Weight (kg)", "BMI"]
    else:
        col_list = "Module not found"
    return col_list


def names_nact(module_name):
    if module_name == "NACT_Tox_table":
        col_list = ["File_number", "Drug_Administered", "Toxicity_type", "Toxicity_grade",
                    "Treatment", "Response_Treatment", "Cycle_Toxicity", "ChangedTreatment_Toxicity"]
    elif module_name == "NACT_Drug_Table":
        col_list = ['File_number', 'Number_cycle', 'Drug', 'Drug_dose', 'Dose_unit', 'Cycle_frequency_per_week']
    elif module_name == "Neo_Adjuvant_Therapy":
        col_list = ['NACT_status',  "Place_NACT",  'Details_NACT', 'Plan_NACT',  "Date_start_NACT",
                    "Patient_weight_NACT", "Drugs_Administered", 'Number_Cycles_NACT',  'Cycle_Weekly_Frequency',
                    "Drugs_TotalDose", 'Drugs_unit', "Toxicity_Type", "Toxicity_Grade",  "Toxicity_Treatment",
                    "Toxicity_Response",  "Toxicity_at_Cycle", "NACT_change_due_to_Toxicity",
                    "Tumour_Response_Check_Method",  "Tumour_Response_NACT", "Tumour_size", 'Tumour_size_unit',
                    "Date_tumour_size_checked",  "NACT_completion_status",  "NACT_end_date",
                    "Trastuzumab_use_NACT",  "Trastuzumab_regime_NACT", 'Trastuzumab_courses_taken_NACT',
                    "Hormone_therapy_NACT",  "Hormone_therapy_type_NACT", 'Hormone_therapy_duration',
                    "Horomone_therapy_side_effects",  "update_by",  "last_update"]
    elif module_name == "clip_information":
        col_list = ["Clip_number", "Clip_date", "Clip_Insertion_After_Cycle"]
    else:
        col_list = "File_number"
    return col_list


def names_chemotherapy(module_name):
    if module_name == "Chemo_Tox_table":
        col_list = ["File_number", "Drug_Administered", "Toxicity_type", "Toxicity_grade",
                    "Treatment", "Response_Treatment", "Cycle_Toxicity", "ChangedTreatment_Toxicity"]
    elif module_name == "Chemo_Drug_Table":
        col_list = ['File_number', 'Drug', 'Number_cycle', 'Cycle_frequency_per_week', 'Drug_dose', 'Dose_unit']
    elif module_name == "Adjuvant_ChemoTherapy":
        col_list = ['Chemotherapy_status', "Place_Chemotherapy", 'Details_Chemotherapy', 'Plan_Chemotherapy',
                    "Date_start_Chemotherapy", "Patient_weight_Chemotherapy", "Drugs_Administered",
                    'Number_Cycles_Chemotherapy', 'Cycle_Weekly_Frequency', "Drugs_TotalDose", 'Drugs_unit',
                    "Toxicity_Type", "Toxicity_Grade", "Toxicity_Treatment", "Toxicity_Response", "Toxicity_at_Cycle",
                    "Chemotherapy_change_due_to_Toxicity", "Chemotherapy_completion_status",
                    "Chemotherapy_end_date", "Trastuzumab_use_Chemotherapy", "Trastuzumab_regime_Chemotherapy",
                    'Trastuzumab_courses_taken_Chemotherapy', 'Ovary_Status', "Hormone_therapy_Chemotherapy",
                    "Hormone_therapy_type_Chemotherapy", 'Hormone_therapy_duration_Chemotherapy',
                    "Horomone_therapy_side_effects_Chemotherapy", "update_by", "last_update"]
    elif module_name == "Tox_table":
        col_list = ["File_number", "Drug_Administered", "Toxicity_type", "Toxicity_grade",
                    "Treatment", "Response_Treatment", "Cycle_Toxicity", "ChangedTreatment_Toxicity"]
    else:
        col_list = "File_number"
    return col_list


def names_surgery_information(module_name):
    if module_name == "surgery_information":
        col_list = ["Surgery_Date", "Surgery_Hospital", "Surgery_Patient_Hospital_ID", "Surgery_Date_Admission",
                    "Surgery_Hospital_Ward", "Surgery_Name_Anaesthetist", "Surgery_Name_Surgeon",
                    "Surgery_Lesion_location", "Surgery_Type", "Surgery_Incision", "Surgery_Type_Subtype",
                    "Surgery_Type_Level_Subtype", "Oncoplastic_Surgery_Type", "Oncoplastic_Surgery_Flap",
                    "Oncoplastic_Surgery_Plan", 'Oncoplastic_Surgery_Tumour_filled_by', 'Oncoplastic_Surgery_NAC_Graft',
                    'Oncoplastic_Surgery_Primary_Pedicle', 'Oncoplastic_Surgery_Secondary_Pedicle',
                    'Reconstruction_Surgery_Implant_Type', 'Reconstruction_Surgery_Implant_Size',
                    'Contralateral_Surgery', 'Contralateral_Surgery_Type', 'Contralateral_Surgery_Type_Details',
                    "Surgery_Notes"]
    elif module_name == "node_excision":
        col_list = ["Guide_Node_Excision_Surgery", "Frozen_Samples_Surgery", "Gross_Tumour_Size_Surgery",
                    "Skin_Surgery", "Nodes_Type_Surgery", "Number_Nodes_Surgery", "Level_Nodes_Surgergy",
                    "Sentinel_Node_Labelling_Method_Surgery", "Blue_Node", "Hot_Node", "Blue_Hot_Node",
                    "Non_Blue_Hot_Node", "Palpable_Node"]
    elif module_name == "post_surgery":
        col_list = ["Chemotherapy_plan", "Radiotherapy_plan", "Other_plans", "Drain_removal_date", "Total_drain_days",
                    "Days_post_surgery_complications", "Post_surgery_complications", "Treatment_post_surgery_"
                    "complications", "Days_post_surgery_recurrence", "Recurrence_Site", "OPD_notes", "update_by",
                    "last_update"]
    else:
        col_list = "File_number"
    return col_list


def names_radiation():
    col_list = ["Radiation_received", "Radiation_date", "Radiation_type", "IMRT_DCRT", "Radiation_acute_toxicity",
                "Radiation_Delayed_Toxicity", "Radiation_finish_date", "Radiation_location", "Radiation_Oncologist",
                "update_by", "last_update"]
    return col_list


def name_follow_up():
    col_list = ["Follow_up_Period", "Follow_up_status", "Follow_up_Mammography", "Follow_up_USG",
                "Follow_up_other_test", "Follow_up_other_result", "update_by", "last_update"]
    return col_list


def names_longterm(module_name):
    if module_name == "hormone":
        col_list = ["Hormone_Indicated", "Hormone_Recieved", "Hormone_Date", "Hormone_Type", "Hormone_duration_years",
                    "Hormone_Discontinued", "Hormone_Ovary_Surpression", 'Hormone_Therapy_Outcome', "Hormone_followup",
                    "Horomone_recurrence"]
    elif module_name == "metastasis":
        col_list = ["Metastasis_exam", "Date_last_followup", "Time_to_recurrence", "Nature_of_recurrence",
                    "Distant_site", "Patient_status_last_followup", "update_by", "last_update"]
    else:
        col_list = "File_number"
    return col_list


def db_tables():
    tables = ["Patient_Information_History", "Biopsy_Report_Data", "Clinical_Exam", "Radiology", "Neo_Adjuvant_Therapy",
              "Surgery_Report", "Surgery_Block_Report_Data", "Adjuvant_ChemoTherapy", "Radiotherapy",
              "HormoneTherapy_Survival", "Follow_up_Data"]
    return tables


def mutation_tables(table):
    if table == "Germline_Mutations":
        col_list = ['germline_mutation_tested', 'sample_used', 'technology', 'sequenced_at_facility',
                    'confirmed_by_re-testing', 'does_retesting_confirm_mutation_y_n', 'restesting_method', 'gene',
                    'exon_number', 'nucleotide_position', 'nucleotide_before', 'nucleotide_after', 'aminoa_position',
                    'amino_acid_before', 'amino_acid_after', 'variation_dna', 'zygosity', 'clinical_significance',
                    'inheritance', 'transcript', 'cdna', 'effect_on_mrna', 'protein', 'effect_on_protein',
                    'protein_databases_reference', 'ethnicities', 'variants_in_vicinity', 'remarks']
    elif table == "Somatic_Mutations":
        col_list = ['somatic_mutation_tested', 'sample_used', 'percent_tumor_in_the_sample',
                    'percent_tumor_identification_done_by', 'technology_used_for_germline_mutation_sequencing',
                    'facility_somatic_mutation_sequenced_at', 'somatic_mutation_sequenced_confirmed_by_re-testing',
                    'accession_number', 'run_id', 'panel', 'variant_call_id', 'gene', 'gsyntax', 'psyntax',
                    'selected_psyntax', 'mutation_type', 'variant_classification', 'consequence', 'vaf',
                    'frequency_from_data', 'dbsnp_frequency', 'exac_frequency', 'nhlbi_frequency', 'domain', 'pathways',
                    'ethnicities', 'variants', 'remarks']
    else:
        col_list = 'File_number'
    return col_list


def names_biopsy_new(module_name):
    if module_name == "biopsy_report_info":
        col_list = ['Biopsy_report_PCCM_yes_no', 'IHC_report_PCCM_yes_no', 'Breast_Biopsy', "Block_SR_Number_Biopsy",
                    "Block_Location_ID_Biopsy", "Biopsy_Block_ID", "No_of_blocks_Biopsy", "Date_of_Biopsy",
                    "Lab_ID_Biopsy", "Biopsy_Type", "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade",
                    "Lymphovascular_emboli_biopsy_yes_no", "DCIS_biopsy_yes_no"]
    elif module_name == "tumour_biopsy_data":
        col_list = ["Tumour_biopsy_ER", "Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR",
                    "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", "Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH",
                    "Tumour_biopsy_Ki67_Percent", "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location",
                    "Lymph_Node_biopsy_diagnosis", "update_by", "last_update"]
    elif module_name == 'biopsy_report_info_df':
        col_list = ["Block_SR_Number_Biopsy", "Block_Location_ID_Biopsy", "Biopsy_Block_ID", "No_of_blocks_Biopsy",
                    "Date_of_Biopsy", "Lab_ID_Biopsy", "Biopsy_Type", "Tumour_biopsy_diagnosis",
                    "Tumour_biopsy_diagnosis_grade", "Lymphovascular_emboli_biopsy_yes_no", "DCIS_biopsy_yes_no"]
    else:
        col_list = "File_number"
    return col_list

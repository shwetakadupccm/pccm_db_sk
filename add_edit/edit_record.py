import reports
from main.add_insert_block_data import AddBlockData
from reports.follow_up_month_year import FollowUp
from reports.pet_report import PetReportData


def edit_record(conn, cursor, file_number, table, user_name, folders, file):
    geninfo = reports.gen_info_tables.GenInfo(conn, cursor, file_number, user_name)
    block_data = AddBlockData(folders, file, user_name)
    follow_up = FollowUp(conn, cursor, file_number, user_name)
    pet_reports = PetReportData(conn, cursor, file_number, user_name)
    rt = reports.radiotherapy.RadioTherapy(conn, cursor, file_number, user_name)
    nact = reports.nact.NeoAdjuvant(conn, cursor, file_number, user_name)
    radio = reports.radiology.Radiology(conn, cursor, file_number, user_name)
    if table == "patient_information_history":
        geninfo.edit_data()
    elif table == 'biopsy_path_report_data':
        block_data.add_path_report(table)
    elif table == "clinical_exam":
        reports.clinical_exam.edit_data(conn, cursor, file_number, user_name)
    elif table == "radiology":
        radio.edit_data()
    elif table == 'pet_reports':
        pet_reports.edit_data()
    elif table == "neo_adjuvant_therapy":
        nact.edit_data()
    elif table == "surgery_report":
        reports.surgery_info.edit_data(conn, cursor, file_number, user_name)
    elif table == "adjuvant_chemotherapy":
        reports.chemotherapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "radiotherapy":
        rt.edit_data()
    elif table == "hormonetherapy_survival":
        reports.longterm_therapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "follow_up_data":
        follow_up.edit_data()

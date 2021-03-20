import reports
from main.add_insert_block_data import AddBlockData


def add_new(conn, cursor, file_number, table, user_name, folders, file):
    print(table)
    geninfo = reports.gen_info_tables.GenInfo(conn, cursor, file_number,user_name)
    block_data = AddBlockData(folders, file, user_name)
    follow_up = reports.FollowUp(conn, cursor, file_number, user_name)
    pet_report = reports.PetReportData(conn, cursor, file_number, user_name)
    rt = reports.radiotherapy.RadioTherapy(conn, cursor, file_number, user_name)
    nact = reports.nact.NeoAdjuvant(conn, cursor, file_number, user_name)
    radio = reports.radiology.Radiology(conn, cursor, file_number, user_name)
    if table == "patient_information_history":
        geninfo.add_gen_info()
    elif table == 'biopsy_path_report_data':
        block_data.add_path_report(table)
    elif table == "clinical_exam":
        reports.clinical_exam.add_data(conn, cursor, file_number, user_name)
    elif table in radio.tables:
        radio.add_radio(table)
    elif table == "ultrasound":
        usg.add_data()
    elif table == 'pet_reports':
        pet_report.add_data()
    elif table == "neo_adjuvant_therapy":
        nact.add_data()
    elif table == "surgery_report":
        reports.surgery_info.add_data(conn, cursor, file_number, user_name)
    elif table == 'surgery_path_report_data':
        block_data.add_path_report(table)
    elif table == "adjuvant_chemotherapy":
        reports.chemotherapy.add_data(conn, cursor, file_number, user_name)
    elif table == "radiotherapy":
        rt.add_data()
    elif table == "hormonetherapy_survival":
        reports.longterm_therapy.add_data(conn, cursor, file_number, user_name)
    elif table == "follow_up_data":
        follow_up.add_data()

from reports.ffpe_db import FFPECSVData
from helper_function.ask_y_n_statement import ask_option
import os
import sqlite3
from datetime import date
from add_edit.output_excel import OutputData




def ffpe_csv():
    folder_name,  file_name, database_folder_name, database_name = ('D:/repos/pccm_db/main/DB', "FFPE_new_blocks.csv", 
                                                                   'D:/repos/pccm_db/main/DB', 
                                                                   'PCCM_BreastCancerDB_FFPE_dk_2018-11-20.db')
    check_folder = None
    while check_folder != 'All are correct':
        print('\nFolder location of FFPE new blocks data is set as: \n' + folder_name + '\n')
        print('File name of FFPE new blocks data is set as: \n' + file_name + '\n')
        print('Database file folder is set as \n' + database_folder_name + '\n')
        print('Database file name is set as \n' + database_name + '\n')
        check_folder = ask_option("Do you want to change any options?",
                                  ['FFPE File Folder', 'FFPE File Name', 'Database Folder',
                                   'Database Name', 'All are correct'])
        if check_folder == 'FFPE File Folder':
            print('Folder location of FFPE new blocks data is set as \n' + folder_name + '\n')
            folder_name = input("Please enter folder location of FFPE new blocks data: ")
        elif check_folder == 'FFPE File Name':
            print('File name of FFPE new blocks data is set as: \n' + file_name + '\n')
            file_name = input("Please input correct File name of FFPE new blocks data (with .csv extension): ")
        elif check_folder == 'Database Folder':
            print('Database file folder is set as: \n' + database_folder_name + '\n')
            database_folder_name = input("Please input correct database file destination: ")
        elif check_folder == 'Database Name':
            print('Database file name is set as: \n' + database_name + '\n')
            database_name = input("Please input correct database file name (with .db extension): ")
    conn_path = os.path.join(database_folder_name, database_name)
    conn = sqlite3.connect(conn_path)
    cursor = conn.cursor()
    ffpe_data = FFPECSVData(conn, cursor, folder_name, file_name)
    ffpe_df = ffpe_data.read_file()
    n_rows = ffpe_df.shape[1]
    print(str(n_rows) + ' block entries read from file uploaded')
    ffpe_str = ffpe_df.astype(dtype='str')
    ffpe_data.write_file(ffpe_str)
    print(str(n_rows) + ' block entries added to ' + database_name + ' database')
    output_file_name = 'Uploaded_Database_' + file_name + str(date.today()) + '.xlsx'
    file_information =  database_folder_name, database_name, folder_name, output_file_name
    print_file = OutputData(file_information)
    print_file.output_data()

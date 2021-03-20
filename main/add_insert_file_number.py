def add_insert():
    import sqlite3
    import helper_function.ask_y_n_statement as ask
    import sql.add_update_sql as add_update_sql
    from datetime import datetime
    import os
    import textwrap
    from helper_function.pccm_names import db_tables

    folders = "d:/repos/pccm_db/main/DB"
    file = 'PCCM_BreastCancerDB_check_new_all_2_2019-05-27.db'
    #file = 'PCCM_BreastCancerDB_all_data_rituja_surgery_data.db'
    check_path = False
    while not check_path:
        print ('\nDatabase file '+file+ ' in folder '+folders+' is being used\n')
        check_location = ask.ask_y_n('Is this correct?')
        if not check_location:
            print ("\n File is currently set as "+file)
            file = input('Please enter database file name (with .db extension): ')
            print("\n Folder is currently set as " + folders)
            folders = input('Please enter database folder name (full path as given above): ')
        else:
            check_path = True
    path = os.path.join(folders, file)
    if os.path.isfile(path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        user_name = input("Please input username/user_id: ")
        folder_next = True
        files_table_added = []
        while folder_next:
            check = False
            while not check:
                file_number = input("File Number: ")
                print("File Number: " + file_number)
                check = ask.ask_y_n("Is this file number correct")
            check_table = True
            while check_table:
                table = ask.ask_list("Table", db_tables())
                file_table = file_number + "-" + table
                files_table_added.append(file_table)
                check_table = add_update_sql.check_file(conn, cursor, table, file_number, user_name, folders, file)
            folder_next = ask.ask_y_n("Add/update another record?")
    else:
        note = "current path: '" + path + "' to database is not valid. Check path and database name and run " \
                                          "start_pccm_db() again."
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=note)
        print(string)

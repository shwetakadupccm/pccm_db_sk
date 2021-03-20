import sqlite3
import helper_function.ask_y_n_statement as ask
import os
import textwrap
from helper_function.pccm_names import ffpe_db_tables
from reports.ffpe_db_new import NewBlock
from reports.block_information import BlockInformation
from additional_tables.block_description import check_path_report_entry
import sql.add_update_sql as sql

def get_folder_name():
    folders = "d:/repos/pccm_db/main/DB"
    file = 'PCCM_BreastCancerDB_2019_07_03.db'
    check_path = False
    path = os.path.join(folders, file)
    while not check_path:
        print('\nDatabase file ' + file + ' in folder ' + folders + ' is being used\n')
        check_location = ask.ask_y_n('Is this correct?')
        if not check_location:
            print("\n File is currently set as " + file)
            file = input('Please enter database file name (with .db extension): ')
            print("\n Folder is currently set as " + folders)
            folders = input('Please enter database folder name (full path as given above): ')
            path = os.path.join(folders, file)
        if os.path.isfile(path):
            check_path = True
        else:
            note = "current path: '" + path + "' to database is not valid. Check path and database name and enter " \
                                              "again"
            wrapper = textwrap.TextWrapper(width=100)
            string = wrapper.fill(text=note)
            print(string)
    user_name = input("Please input username/user_id: ")
    return folders, file, user_name


class AddBlockData:
    def __init__(self, folders, file, user_name):
        path = os.path.join(folders, file)
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.user_name = user_name

    @staticmethod
    def get_table():
        table = ask.ask_list("Table", ffpe_db_tables())
        return table

    def add_path_report(self, table):
        file_number = 'test'
        table_type = table.split("_")[0]
        folder_next = True
        while folder_next:
            check = False
            while not check:
                file_number = input("File Number: ")
                print("File Number: " + file_number)
                check = ask.ask_y_n("Is this file number correct")
            block_list_table = BlockInformation(self.conn, self.cursor, file_number)
            pk, block_id, number_of_blocks = block_list_table.get_block_pk(self.user_name,
                                                                           col_filter_value=table_type)
            #print(block_id, number_of_blocks)
            check_path_report_entry(conn=self.conn, cursor=self.cursor, file_number=file_number, table_to_check=table,
                                    pk=pk, block_id=block_id, number_of_blocks=number_of_blocks,
                                    user_name=self.user_name)
            folder_next = ask.ask_y_n("Add/update another file for table " + table + "?")

    def add_block_list(self):
        block_list = NewBlock(self.conn, self.cursor, self.user_name)
        add_data = True
        while add_data:
            categories = ['Add Block', 'Edit Block','Exit']
            new_update = ask.ask_list('you want to do?', categories)
            if new_update == 'Edit Block':
                block_list.edit_data()
                add_data = ask.ask_y_n('Do you want to add/edit another block?')
            elif new_update == 'Add Block':
                file_number = 'test'
                check_file = False
                while not check_file:
                    file_number = input("Enter File Number: ")
                    print("File Number: " + file_number)
                    check_file = ask.ask_y_n("Is this file number correct")
                if not sql.check_file_number_exist(self.cursor, file_number, table='block_list'):
                    block_list.add_data(file_number)
                else:
                    print('This file_number already exists. Add a new block if for ' + file_number)
                    block_type = ask.ask_list('Block type', ['biopsy', 'surgery'])
                    block_list.add_new_pk(file_number, block_type)
                add_data = ask.ask_y_n('Do you want to add/edit another block?')
            else:
                add_data = False

    def add_ffpe(self):
        table_next = True
        while table_next:
            table = AddBlockData.get_table()
            if table == ffpe_db_tables()[0]:
                self.add_block_list()
            else:
                self.add_path_report(table)
            table_next = ask.ask_y_n("Add/update another table?")

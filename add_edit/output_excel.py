import pandas as pd
import os
import sqlite3
from helper_function.ask_y_n_statement import ask_option, ask_y_n
from datetime import date, datetime
from helper_function.pccm_names import print_db_tables
from sql.add_update_sql import table_check
import helper_function.table_dicts as table_dicts
import xlsxwriter

#todo set output file name same as db file name with username and date of output.
class OutputData():
    def __init__(self, data_location_name, user_name):
        self.folder_db, self.db_name, self.output_folder, self.output_name, self.research = data_location_name
        self.conn = sqlite3.connect(os.path.join(self.folder_db, self.db_name))
        self.user_name = user_name

    def print_table(self, writer, table):
        modules = table_dicts.table_module_dict(table)
        if table == 'Patient_Information_History' or table == 'block_list':
            if self.research:
                modules = table_dicts.table_module_research(table)
        columns = []
        if not modules:
            modules = 'no_modules'
            columns = table_dicts.db_dict(table, modules)
        else:
            for module in modules:
                cols = table_dicts.db_dict(table, module)
                columns = columns + cols
        if table!= 'Block_list':
            col_list = table_dicts.create_col_list(columns)
        else:
            col_list = columns
        if self.user_name != 'dk':
            sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
        else:
            sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "' WHERE file_number NOT LIKE '%delete'")
        df = pd.read_sql(sql, self.conn)
        number = df.shape[0]
        df.to_excel(writer, sheet_name=table, startrow=0, index=False, header=True)
        return number

    def print_summary(self, df):
        output_name = 'Summary_' + self.output_name
        ex_path = os.path.join(self.output_folder, output_name)
        writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
        df.reset_index(drop=True, inplace=True)
        df.to_excel(writer, sheet_name="Summary", index=False)
        writer.save()
        return

    def output_data(self):
        cursor = self.conn.cursor()
        tables_to_print = []
        summary_df = pd.DataFrame(columns=["table_name", "number_entries"])
        output_name = self.output_name
        if self.research:
            output_name = 'Research_' + self.output_name
        output_path = os.path.join(self.output_folder, output_name)
        for table in print_db_tables():
            check = table_check(cursor, table)
            if check:
                tables_to_print.append(table)
        if not tables_to_print:
            print("Selected Database has no tables. Please re-start and edit database file")
            return
        else:
            writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
            print('This database contains the following tables:')
            i = 1
            for table in tables_to_print:
                print(str(i) + ". " + table)
                i = i+1
            to_print = ask_option("Do you want to print all tables or only select tables?",
                                  ["All tables", "Select tables"])
            if to_print == "All tables":
                index = 0
                for table in tables_to_print:
                    self.print_table(writer, table)
                    number = self.print_table(writer, table)
                    summary_df.loc[index] = [table, number]
                    index = index + 1
            elif to_print == "Select tables":
                for table in tables_to_print:
                    to_print = ask_y_n("Do you want to print " + table)
                    if to_print:
                        self.print_table(writer, table)
                        number = self.print_table(writer, table)
                        summary_df.loc[table] = [table, number]
            self.print_summary(summary_df)
            print("Data file " + output_name + " has been created at " + self.output_folder + '\n')
        writer.save()


def define_path():
    folder_db, db_name, output_folder, output_name, research = ('E:/pccm_db/main/DB', "PCCM_BreastCancerDB_all_data.db",
                          'E:/pccm_db/main/DB/data_output', datetime.now().strftime('%Y_%m_%d') +
                                                                '_Output_PCCM_BreastCancerDB.xlsx', False)
    check_folder = None
    research = ask_y_n('Do you want to create an output for research?')
    while check_folder != 'All are correct':
        print('\nFolder location of database file is set as: \n' + folder_db + '\n')
        print('Database file name is set as: \n' + db_name + '\n')
        print('Output file destination is set as \n' + output_folder + '\n')
        print('Output file name is set as \n' + output_name + '\n')
        check_folder = ask_option("Do you want to change any options?",
                                  ['Database Folder', 'Database File', 'Output File Destination',
                                   'Output File Name', 'All are correct'])
        if check_folder == 'Database Folder':
            print('Folder location of database file is set as: \n' + folder_db + '\n')
            folder_db = input("Please enter destination folder: ")
        elif check_folder == 'Database File':
            print('Database file name is set as: \n' + db_name + '\n')
            db_name = input("Please input correct database file name: ")
        elif check_folder == 'Output File Destination':
            print('Output file destination is set as: \n' + output_folder + '\n')
            output_folder = input("Please input correct output file destination: ")
        elif check_folder == 'Output File Name':
            print('Output file name is set as: \n' + output_name + '\n')
            file_name = input("Please input correct output file name (without date and .xlsx): ")
            output_name = file_name + '_' + str(date.today()) + '.xlsx'
    data_location_name = folder_db, db_name, output_folder, output_name, research
    return data_location_name


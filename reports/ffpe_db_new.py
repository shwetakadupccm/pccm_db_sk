import pandas as pd
import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
import helper_function.pccm_names as names
from additional_tables.block_description import block_location_format
from helper_function.option_lists import BlockList
import uuid


class NewBlock:

    def __init__(self, conn, cursor, user_name):
        self.user_name = user_name
        self.table_name = 'block_list'
        self.conn = conn
        self.cursor = cursor
        self.columns = names.block_list('all')
        self.columns_db = ['pk'] + self.columns
        self.block_data = pd.DataFrame(columns=self.columns_db)

    def add_block_id(self, file_number):
        block_df = self.block_data
        pk = uuid.uuid4().hex
        data_list = self.columns
        check = False
        while not check:
            check_name = False
            while not check_name:
                patient_name = input('Please enter patient name: '),
                print('Patient name: ' + str(patient_name))
                check_name = ask.ask_y_n('Is name correct')
            mr_number = self.check_block_value_in_db(input_statement='Please enter MR number: ',
                                                     value_name='mr_number', integer=True)
            date_of_birth = self.get_value_and_check_value(col_name='date_of_birth', file_number=file_number,
                                                           input_statement='Please input patient date of birth '
                                                                           '(format: dd.mm.yyyy): ', integer=False)
            date_first_visit = ask.check_date('Please enter date of first visit: ')
            block_sr_number = self.check_block_value_in_db(input_statement='Please enter block serial number: ',
                                                           value_name='block_sr_number', integer=True)
            block_pccm = ask.ask_y_n('Have these blocks been recieved at PCCM?')
            block_location, blocks_received_at_pccm = ['NA', ] * 2
            if block_pccm:
                block_location_check = False
                while not block_location_check:
                    block_location = block_location_format()
                    block_location_check = sql.check_value_not_exist(self.cursor, value_name='block_location',
                                                                     value=block_location, table=self.table_name)
                blocks_received_at_pccm = ask.check_date_or_today('Please enter date blocks recieved at PCCM (or '
                                                                  'today): ')
            consent_discussed, consent = self.get_consent(file_number)
            block_id = self.check_block_value_in_db(input_statement='Please enter block id: ', value_name='block_id',
                                                    integer=False)
            block_type = ask.ask_list('Block type', ['biopsy', 'surgery'])
            if blocks_received_at_pccm == 'NA':
                number_of_blocks, block_series, current_block_location = ['NA', ] * 3
            else:
                number_of_blocks = ask.check_number_input('Please enter number of blocks recieved at PCCM: ',
                                                          'Number of blocks has to be a whole number or NA')
                block_series = input("Series of blocks recieved (Please enter series in the form A-B and separate "
                                     "series by '|' e.g, A-B|E): ")
                current_block_location = ask.ask_list('Current location of block',
                                                      BlockList.edit_values['current_block_location'])
            data_list = [pk, file_number, patient_name, mr_number, date_of_birth, date_first_visit, block_sr_number,
                         block_location, block_type, block_id, current_block_location, blocks_received_at_pccm,
                         number_of_blocks, block_series, str(consent_discussed), consent, self.user_name,
                         sql.last_update()]
            block_df.loc[pk] = data_list
            check, block_df = sql.review_df_row(block_df)
        return data_list[1:], pk

    def update_block_id(self, file_number, block_type):
        block_df = self.block_data
        pk = uuid.uuid4().hex
        data_list = self.columns
        check = False
        while not check:
            patient_name = sql.get_value_no_error(col_name = 'patient_name', table=self.table_name, pk=file_number,
                                                  pk_name='file_number', cursor=self.cursor)
            mr_number = sql.get_value_no_error(col_name='mr_number', table=self.table_name, pk=file_number,
                                               pk_name='file_number', cursor=self.cursor)
            date_of_birth = sql.get_value_no_error(col_name='date_of_birth', table=self.table_name, pk=file_number,
                                                   pk_name='file_number', cursor=self.cursor)
            date_first_visit = sql.get_value_no_error(col_name='date_first_visit', table=self.table_name,
                                                      pk=file_number, pk_name='file_number', cursor=self.cursor)
            block_sr_number = sql.get_value_no_error(col_name = 'block_sr_number', table=self.table_name, pk=file_number,
                                                  pk_name='file_number', cursor=self.cursor)
            block_location = sql.get_value_no_error(col_name='block_location', table=self.table_name, pk=file_number,
                                                     pk_name='file_number', cursor=self.cursor)
            blocks_received_at_pccm = sql.get_value_no_error(col_name='blocks_received_at_pccm', table=self.table_name,
                                                             pk=file_number, pk_name='file_number', cursor=self.cursor)
            consent_discussed = sql.get_value_no_error(col_name = 'consent_discussed', table=self.table_name,
                                                       pk=file_number, pk_name='file_number', cursor=self.cursor)
            consent = sql.get_value_no_error(col_name = 'consent', table=self.table_name, pk=file_number,
                                             pk_name='file_number', cursor=self.cursor)
            block_id = self.check_block_value_in_db(input_statement='Please enter block id: ', value_name='block_id',
                                                    integer=False)
            if blocks_received_at_pccm == 'NA':
                number_of_blocks, block_series, current_block_location = ['NA',] * 3
            else:
                number_of_blocks = ask.check_number_input('Please enter number of blocks recieved at PCCM: ',
                                                          'Number of blocks has to be a whole number or NA')
                block_series = input("Series of blocks recieved (Please enter series in the form A-B and separate "
                                     "series by '|' e.g, A-B|E): ")
                current_block_location = ask.ask_list('Current location of block',
                                                      BlockList.edit_values['current_block_location'])
            data_list = [pk, file_number, patient_name, mr_number, date_of_birth, date_first_visit, block_sr_number,
                         block_location, block_type, block_id, current_block_location, blocks_received_at_pccm,
                         number_of_blocks, block_series, str(consent_discussed), consent, self.user_name,
                         sql.last_update()]
            # print(data_list, self.columns_db)
            block_df.loc[pk] = data_list
            check, block_df = sql.review_df_row(block_df)
        return data_list[1:], pk


    def edit_block_id(self):
        file_number = 'test'
        check_file = False
        while not check_file:
            print('add_update_patient')
            file_number = input("Enter File Number: ")
            print("File Number: " + file_number)
            check_file = ask.ask_y_n("Is this file number correct")
        action = ask.ask_list('What values are to be updated?', ['patient_name', 'mr_number', 'date_of_birth',
                                                                 'date_first_visit','block_sr_number', 'block_location',
                                                                 'block_type', 'block_id', 'current_block_location',
                                                                 'blocks_received_at_pccm', 'number_of_blocks',
                                                                 'block_series', 'consent'])
        columns_action = [action] + ['update_by', 'last_update']
        update_user = [self.user_name, sql.last_update()]
        if action == 'consent':
            data = list(self.get_consent(file_number)) + update_user
            print(data)
            sql.update_multiple_key(self.conn, self.cursor, self.table_name,
                                    columns=['consent_discussed', 'consent', 'update_by', 'last_update'],
                                    key_name='file_number', key_value=file_number, data= data)
        elif action in {'patient_name', 'block_sr_number', 'block_location', 'blocks_received_at_pccm', 'mr_number',
                        'date_of_birth', 'date_first_visit'}:
            data_old = sql.get_value_no_error(col_name=action, table=self.table_name, pk=file_number,
                                              pk_name='file_number', cursor=self.cursor)
            print(action + ' is currently set as: ' + data_old)
            change = ask.ask_y_n('Do you want to change this?')
            if change:
                data_new = ['NA'] + update_user
                check = False
                while not check:
                    if action in {'blocks_recieved_at_pccm', 'date_of_birth', 'date_first_visit'}:
                        data = ask.check_date('Please enter ' + action +': ')
                    elif action == 'block_location':
                        data = block_location_format()
                    else:
                        data = input('Please input ' + action)
                    if action in BlockList.unique_values:
                        check = sql.check_value_not_exist(self.cursor, action, data, self.table_name)
                    else:
                        check = True
                    data_new = [data] + update_user
                sql.update_multiple_key(self.conn, self.cursor, self.table_name, columns=columns_action,
                                        key_name='file_number', key_value=file_number, data=data_new)
        elif action in {'current_block_location', 'number_of_blocks', 'block_series', 'block_type', 'block_id'}:
            check = False
            block_list = sql.extract_select_column_key(self.conn, self.columns, self.table_name, col_select='block_id',
                                                     key_name='file_number', key_value=file_number)

            block_id = ask.ask_list(action + ' information is to be entered for: ', block_list)
            pk = sql.extract_select_column_key(self.conn, self.columns_db, self.table_name, col_select='pk',
                                               key_name='block_id', key_value=block_id)
            # function returns a set so need to convert to str.
            pk = list(pk)[0]
            data = action
            while not check:
                print('BlockList.edit_values[action]: ',BlockList.edit_values[action])
                data = ask.ask_list(action + ' of ' +  block_id, BlockList.edit_values[action])
                if action in BlockList.unique_values:
                    check = sql.check_value_not_exist(self.cursor, action, data, self.table_name)
                else:
                    check = True
            if data is set:
                data = list(data)
            data_new = [data] + update_user
            print(data_new, pk)
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, columns=columns_action, key_name='pk',
                                    key_value=str(pk), data=data_new)

    def check_block_value_in_db(self, input_statement, value_name, integer):
        check_value = False
        value = value_name
        while not check_value:
            if integer and value != 'block_not_available':
                value = ask.check_number_input(input_statement, error=value_name + 'has to be a number')
            else:
                value = input(input_statement)
            if value != 'block_not_available':
                check_value = sql.check_value_not_exist(self.cursor, value_name, value, self.table_name)
        return value

    def get_value_and_check_value(self, col_name, file_number, input_statement, integer):
        pk = file_number
        check = False
        value = col_name
        check_value = True
        while not check:
            value = sql.get_value_no_error(col_name, self.table_name, pk, 'file_number', self.cursor)
            if not value or not check_value:
                value = self.check_block_value_in_db(input_statement, value_name=col_name, integer=integer)
            print(col_name.capitalize(), ': ', value)
            check_value = ask.ask_y_n('Is this correct?')
            if check_value:
                check = True
        return value

    def get_consent(self, file_number):
        consent_discussed = sql.get_value_no_error('consent_discussed', self.table_name, file_number,
                                                   'file_number', self.cursor)
        consent = sql.get_value_no_error('consent', self.table_name, file_number, 'file_number', self.cursor)
        if not consent_discussed:
            consent_discussed = ask.ask_y_n('Has the consent form been discussed with the patient/family? ')
        if not consent and consent_discussed:
            consent = ask.ask_y_n('Did patient give consent?', yes_ans='consent_given',
                                  no_ans='consent_not_given')
        elif not consent and not consent_discussed:
            consent = 'consent_TBD'
        print('consent_discussed: ' + str(consent_discussed), 'consent: ' + consent)
        check = ask.ask_y_n('Is this correct?')
        if not check:
            check_review = False
            data = [str(consent_discussed), consent]
            col_list = ['consent_discussed', 'consent']
            while not check_review:
                consent_discussed = ask.ask_y_n('Has the consent form been discussed with the patient/family? ')
                consent = ask.ask_y_n('Did patient give consent?', yes_ans='consent_given', no_ans='consent_not_given')
                data = [str(consent_discussed), consent]
                check_review = sql.review_input(file_number, col_list, data)
            sql.update_multiple_key(conn=self.conn, cursor=self.cursor, table=self.table_name, columns=col_list,
                                    key_name='file_number', key_value=file_number, data=data)
        return str(consent_discussed), consent

    def check_block_value_not_exist(self, value_name, value, table):
        if value == 'no_block_available':
            return True
        else:
            sql_statement = "SELECT rowid FROM " + table + " WHERE " + value_name + " = ?"
            self.cursor.execute(sql_statement, (value,))
            data = self.cursor.fetchall()
            if len(data) == 0:
                return True
            else:
                print('This ' + value_name + ' already exists. Please check source and enter another value')
                return False

    def add_data(self, file_number):
        add_block = True
        while add_block:
            data, pk = self.add_block_id(file_number)
            sql.add_pk_fk_to_table(self.conn, self.cursor, self.table_name, col_name='pk', pk=pk)
            sql.update_multiple_key(self.conn, self.cursor, self.table_name, columns=self.columns, key_name='pk',
                                    key_value=pk, data=data)
            add_block = ask.ask_y_n('Add another block?')

    def edit_data(self):
        edit_block = True
        while edit_block:
            self.edit_block_id()
            edit_block = ask.ask_y_n('Edit another block?')

    def add_new_pk(self, file_number, block_type):
        data, pk = self.update_block_id(file_number, block_type)
        sql.add_pk_fk_to_table(self.conn, self.cursor, self.table_name, col_name='pk', pk=pk)
        sql.update_multiple_key(self.conn, self.cursor, self.table_name, columns=self.columns, key_name='pk',
                                key_value=pk, data=data)

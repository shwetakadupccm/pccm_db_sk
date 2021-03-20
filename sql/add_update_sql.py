import datetime as dt
import helper_function.ask_y_n_statement as ask
import uuid
import pandas as pd
import helper_function.table_dicts as table_dicts


def update_single(conn, cursor, table, column, file_number, var):
    # update a single column in a sql db. Key is user defined.
    sql_update = "UPDATE " + table + " SET " + column + "= ? WHERE file_number = '" + file_number + "'"
    cursor.execute(sql_update, [var])
    conn.commit()


def update_single_pk(conn, cursor, table, column, pk_value, pk, var):
    # update a single column in a sql db. Key is user defined.
    sql_update = "UPDATE " + table + " SET " + column + "= ? WHERE " + pk_value + " = '" + pk + "'"
    cursor.execute(sql_update, [var])
    conn.commit()


def update_single_key(conn, cursor, table, col_list, key_name, key_value, var):
    # update a single column in a sql db. Key is user defined.
    sql_update = "UPDATE " + table + " SET " + col_list + "= ? WHERE " + key_name + "= '" + key_value + "'"
    cursor.execute(sql_update, [var])
    conn.commit()


def insert(conn, cursor, table, columns, data):
    # insert data in multiple cols in a sql db. adds a new row
    col_number = len(data)
    place_holder = ["?"] * col_number
    place_str = ",".join(place_holder)
    sql_insert = "INSERT INTO " + table + "(" + columns + ") VALUES (" + place_str + ")"
    cursor.execute(sql_insert, data)
    conn.commit()


def insert_file_number(conn, cursor, file_number):
    # insert data in multiple cols in a sql db. adds a new row
    sql_insert = "INSERT INTO Patient_Information_History(file_number) VALUES (?)"
    cursor.execute(sql_insert, file_number)
    conn.commit()


def update_multiple(conn, cursor, table, columns, file_number, data):
    # update multiple columns in a sql db. Key is file_number.
    print(data)
    col_number = len(data)
    for index in range(0, col_number):
        sql_update = "UPDATE " + table + " SET " + columns[index] + "= ? WHERE file_number = '" + file_number + "'"
        var = data[index]
        cursor.execute(sql_update, [var])
    conn.commit()


def update_multiple_key(conn, cursor, table, columns, key_name, key_value, data):
    # update multiple columns in a sql db. Key is defined at use.
    col_number = len(data)
    # print('col_number is ' + str(col_number))
    for index in range(0, col_number):
        sql_update = "UPDATE " + table + " SET " + columns[index] + "= ? WHERE " + key_name + "= '" + key_value + "'"
        var = data[index]
        # print(sql_update, var)
        cursor.execute(sql_update, [var])
    conn.commit()


def add_columns(cursor, table, column):
    sql_statement = "ALTER TABLE " + table + " ADD " + column
    cursor.execute(sql_statement)


def add_columns_old(cursor, table, columns):
    col_number = len(columns)
    for index in range(0, col_number):
        sql_add = "ALTER TABLE " + table + " ADD " + columns[index]
        cursor.execute(sql_add)


def review_input(file_number, columns, data):
    col_number = len(data)
    print("Entries for database are as follows : ")
    for index in range(0, col_number):
        try:
            print(columns[index] + ": " + data[index])
        except TypeError:
            print('col' + str(columns[index]) + str(data[index]))
    ans = ask.ask_y_n("Are entries for file " + file_number + " correct ?", True, False)
    return ans


def review_data(conn, cursor, table, file_number, col_list):
    sql_statement = ('SELECT ' + ", ".join(col_list) + ' FROM ' + table + " WHERE file_number = '" + file_number + "'")
    data = cursor.execute(sql_statement)
    data_list = data.fetchall()
    data_list = list(data_list[0])
    col_number = len(col_list)
    if data_list == [None]*len(data_list):
        print("This section of the database has not been entered")
        enter = ask.ask_y_n("Do you want to enter now")
        return enter
    if None in set(data_list):
        print("Some entries are missing from the database: ")
        for index in range(0, col_number):
            print(col_list[index] + " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to proceed?", ["Edit all", "Add new data only"])
        if enter == "Edit all":
            return True
        else:
            edit_few(conn, cursor, table, col_list, file_number, data_list)
    else:
        print("Entries present in database are as follows : ")
        for index in range(0, col_number):
            print(col_list[index] + " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to", ["Edit all", "Edit some entries", "Edit None"])
        if enter == "Edit some entries":
            for index in range(0, col_number):
                print(col_list[index] + " : " + str(data_list[index]))
                edit = ask.ask_y_n("Edit")
                if edit:
                    data = input("Data for " + col_list[index] + ": ")
                    update_single(conn, cursor, table, col_list[index], file_number, data)
            return False
        elif enter == "Edit all":
            return True
        else:
            return False


def review_data_key(conn, cursor, table, key_name, key_value, columns, col_name, col_value):
    if 'file_number' in columns:
        # remove 1st position from column names (assumes it is file_number)
        col_list = columns[1:]
    else:
        col_list = columns
    sql_statement = 'SELECT ' + ", ".join(col_list) + ' FROM ' + table + " WHERE " + key_name + "= '" + key_value + "'"
    data = cursor.execute(sql_statement)
    data_list = data.fetchall()
    if not data_list:
        print("This " + col_name + ' ' + col_value + ' has not been entered in ' + table)
        enter = ask.ask_y_n("Do you want to enter now")
        if enter:
            add_pk_fk_to_table(conn, cursor, table, col_name=key_name, pk=key_value)
            print('added new row for this ' + key_name)
            return enter
    else:
        data_list = list(data_list[0])
    col_number = len(col_list)
    if data_list == [None]*len(data_list):
        print("This section of the database has not been entered")
        enter = ask.ask_y_n("Do you want to enter now")
        return enter
    elif None in set(data_list):
        print("Some entries are missing from the database: ")
        for index in range(0, col_number):
            print(col_list[index] + " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to proceed?", ["Edit all", "Add new data only"])
        if enter == "Edit all":
            return True
        else:
            enter = edit_few(conn, cursor, table, col_list, key_value, data_list)
            return enter
    else:
        print("Entries present in database are as follows : ")
        for index in range(0, col_number):
            print(col_list[index] + " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to", ["Edit all", "Edit some entries", "Edit None"])
        if enter == "Edit some entries":
            for index in range(0, col_number):
                print(col_list[index] + " : " + str(data_list[index]))
                edit = ask.ask_y_n("Edit")
                if edit:
                    data = input("Data for " + col_list[index] + ": ")
                    update_single_pk(conn, cursor, table, col_list[index], pk_value=key_name, pk=key_value, var=data)
            return False
        elif enter == "Edit all":
            return True
        else:
            return False


def edit_few(conn, cursor, table, col_list, file_number, data_list):
    col_number = len(col_list)
    for index in range(0, col_number):
        if data_list[index] is None:
            data = input("Data for "+col_list[index]+": ")
            update_single(conn, cursor, table, col_list[index], file_number, data)
    return False


def edit_few_key(conn, cursor, table, col_list, key_name, key_value, data_list):
    col_number = len(col_list)
    for index in range(0, col_number):
        if data_list[index] is None:
            data = input("Data for "+col_list[index]+": ")
            update_single_key(conn, cursor, table, col_list[index], key_name, key_value, data)
    return False


def check_file(conn, cursor, table, file_number, user_name, folders, file):
    from add_edit.edit_record import edit_record
    from add_edit.add_new import add_new
    from reports.radiology import Radiology
    if table != 'radiology':
        sql_statement = "SELECT rowid FROM " + table + " WHERE file_number = ?"
        cursor.execute(sql_statement, (file_number, ))
        data = cursor.fetchall()
        if len(data) == 0:
            if table not in {"follow_up_data", "pet_reports", 'radiology'}:
                cursor.execute("INSERT INTO " + table + "(file_number) VALUES ('" + file_number + "')")
            print(file_number + " does not exist in table " + table + ". Enter new record")
            add_new(conn, cursor, file_number, table, user_name, folders, file)
        else:
            todo = ask.ask_list(file_number + " already exists in table " + table + ".", ["Edit record",
                                                                                        "Add new record for same file number",
                                                                                         "Edit None"])
            if todo == "Edit record":
                edit_record(conn, cursor, file_number, table, user_name, folders, file)
            elif todo == "Add new record for same file number":
                print("Add additional record module TBD")
        ask_table = ask.ask_y_n("Add another table?")
    else:
        radio = Radiology(conn, cursor, file_number, user_name)
        tables = radio.tables
        for tab in tables:
            ask_table = True
            while ask_table:
                sql_statement = "SELECT rowid FROM " + tab + " WHERE file_number = ?"
                cursor.execute(sql_statement, (file_number, ))
                dat = cursor.fetchall()
                if len(dat) == 0:
                    print(file_number + " does not exist in table " + tab)
                    enter_tab = ask.ask_y_n('Enter data?')
                    if enter_tab:
                        cursor.execute("INSERT INTO " + tab + "(file_number) VALUES ('" + file_number + "')")
                        add_new(conn, cursor, file_number, tab, user_name, folders, file)
                else:
                    todo = ask.ask_list(file_number + " already exists in table " + tab + ".", ["Edit record", "Edit None"])
                    if todo == "Edit record":
                        edit_record(conn, cursor, file_number, tab, user_name, folders, file)
            #     data.append(dat)
            # print(data, 'length data is =', len(data))          
            # # remove later - test_function
                ask_table = ask.ask_y_n("Add another data set for " + tab + "?")
    return ask_table


def review_df(df):
    print_df(df)
    check = ask.ask_y_n("Is data entered correct?")
    return check


def table_check(cursor, table_name):
    sql_statement = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + table_name + "'"
    cursor.execute(sql_statement)
    [table_exists] = cursor.fetchall()
    test = list(table_exists)[0]
    return test


def view_multiple(conn, table, col_list, file_number):
    sql_statement = ('SELECT ' + ", ".join(col_list) + ' FROM ' + table + " WHERE file_number = '" + file_number + "'")
    df = pd.read_sql(sql_statement, conn)
    print_df(df)
    enter = ask.ask_list("Do you want to add or edit data", ["Add data", 'Edit data', 'Do not add or edit'])
    return enter


def delete_multiple(cursor, table, file_number):
    sql_statement = "DELETE FROM " + table + " WHERE file_number = '" + file_number + "'"
    cursor.execute(sql_statement)


def delete_rows(cursor, table, col_name, col_data):
    sql_statement = "DELETE FROM " + table + " WHERE "+col_name+" = '" + col_data + "'"
    cursor.execute(sql_statement)


def review_df_row(df):
    check_row = len(df)-1
    print(df.iloc[check_row].to_string())
    check = ask.ask_y_n("Is data entered correct?")
    if check:
        return check, df
    else:
        df = df.drop(df.index[check_row])
        return check, df


def get_sql_data(file_number, conn, module, table):
    columns = []
    cols = table_dicts.db_dict(table, module)
    columns = columns + cols
    col_list = table_dicts.create_col_list(columns)
    sql_statement = ('SELECT ' + ", ".join(col_list) + " FROM '" + str(table) + "' WHERE file_number = '" +
                     file_number + "'")
    df = pd.read_sql(sql_statement, conn)
    return df


def get_value(col_name, table, pk, pk_name, cursor, error_statement):
    try:
        sql_statement = "SELECT " + col_name + " FROM " + table + " WHERE " + pk_name + " = '" + pk + "'"
        cursor.execute(sql_statement)
        value_ = cursor.fetchall()
        value = value_[0][0]
    except (ValueError, IndexError):
        value = input(error_statement)
    return value


def get_value_no_error(col_name, table, pk, pk_name, cursor):
    try:
        sql_statement = "SELECT " + col_name + " FROM " + table + " WHERE " + pk_name + " = '" + pk + "'"
        cursor.execute(sql_statement)
        value_ = cursor.fetchall()
        value = value_[0][0]
    except (ValueError, IndexError):
        value = False
    return value


def print_df(df):
    rows = df.shape[0]
    for row in range(0, rows):
        print(df.iloc[row].to_string() + '\n')


def edit_table(df, pk_col, df_col, update_by):
    import sql.add_update_sql as sql
    rows = df.shape[0]
    for row in range(0, rows):
        print(df.iloc[row].to_string() + '\n')
    to_correct = ask.ask_y_n("Are entries correct?")
    if not to_correct:
        print('To delete a single entry select No here and proceed')
        to_correct = ask.ask_y_n("Re-enter entire table?")
        if to_correct:
            return to_correct, df
        else:
            change_row = True
            while change_row:
                pk_list = list(df[pk_col])
                print(pk_list)
                pk = input("Enter " + pk_col + " to change: ")
                index = pk_list.index(pk)
                to_do = True
                while to_do:
                    print(df.loc[index, :])
                    print("\nTo delete a single entry select 'file_number' column here and change file number by \n",
                          "appending (_delete) eg., 123/13 file becomes 123/13_delete\n")
                    col_change = ask.ask_option("Name of column to change", df_col)
                    old_val = df.loc[index, col_change]
                    print(old_val + '\n')
                    new_val = input("Enter correct value for " + col_change + ' for ' + pk + ": ")
                    df.loc[index, col_change] = new_val
                    df.ix[index, 'update_by'] = update_by
                    df.ix[index, 'last_update'] = sql.last_update()
                    print(df.iloc[index].to_string() + '\n')
                    to_do = ask.ask_y_n("Make more changes to " + pk_col + ' ' + pk + '?')
                sql.print_df(df)
                change_row = ask.ask_y_n("Change another row?")
            to_correct = False
    return to_correct, df

# def edit_table(df, pk_col, df_col, update_by):
#     print('To delete a single entry select No here and proceed')
#     to_correct = ask.ask_y_n("Re-enter entire table?")
#     if to_correct:
#         return to_correct, df
#     else:
#         change_row = True
#         while change_row:
#             pk_list = list(df[pk_col])
#             pk_list = ['None' if pk is None else pk for pk in pk_list]
#             print(pk_list)
#             pk = input("Enter " + pk_col + " to change: ")
#             index = pk_list.index(pk)
#             to_do = True
#             while to_do:
#                 print(df.loc[index, :])
#                 #print(df.loc[index])
#                 print("\nTo delete a single entry select 'file_number' column here and change file number by \n",
#                       "appending (_delete) eg., 123/13 file becomes 123/13_delete\n")
#                 col_change = ask.ask_option("Name of column to change", df_col)
#                 old_val = df.loc[index, col_change]
#                 print(str(old_val) + '\n')
#                 # if old_val is None it will become 'None'
#                 new_val = input("Enter correct value for " + col_change + ' for ' + pk + ": ")
#                 df.loc[index, col_change] = new_val
#                 df.ix[index, 'update_by'] = update_by
#                 df.ix[index, 'last_update'] = last_update()
#                 print(df.iloc[index].to_string() + '\n')
#                 to_do = ask.ask_y_n("Make more changes to " + pk_col + ' ' + pk + '?')
#             print_df(df)
#             change_row = ask.ask_y_n("Change another row?")
#         to_correct = False
#     return to_correct, df


def retrieve_with_pk_to_edit(df, value_col, table, cursor, pk=False, value_row_to_edit=False):
    print('To delete a single entry select No here and proceed')
    to_correct = ask.ask_y_n("Re-enter entire table?")
    if to_correct:
        return pk, value_row_to_edit
    else:
        value_list = list(df[value_col])
        value_list = ['None' if value is None else value for value in value_list]
        print(value_list)
        value = input("Enter " + value_col + " to change: ")
        pk = get_value_no_error(col_name='pk', table=table, pk=str(value), pk_name=value_col, cursor=cursor)
    return pk, str(value_row_to_edit)


def check_db_value(col_name, table, file_number, cursor, error_statement):
    try:
        sql_statement = "SELECT " + col_name + " FROM " + table + " WHERE file_number = '" + file_number + "'"
        cursor.execute(sql_statement)
        value_ = cursor.fetchall()
        value = value_[0][0]
        print(col_name.capitalize().replace('_', ' ') + ": " + str(value))
        check = ask.ask_y_n('Is this correct')
        if not check:
            value = input(error_statement)
    except (IndexError, ValueError):
        value = input(error_statement)
    return value


def last_update():
    update_stamp = dt.datetime.now().strftime("%Y_%m_%d|%H_%M")
    return update_stamp


def create_pk():
    pk = uuid.uuid4().hex
    return pk


def check_file_number_exist(cursor, file_number, table):
    sql_statement = "SELECT rowid FROM " + table + " WHERE file_number = ?"
    cursor.execute(sql_statement, (file_number,))
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


def check_pk_fk_exist(cursor, col_filter, pk, table):
    sql_statement = "SELECT rowid FROM " + table + " WHERE " + col_filter + " = ?"
    cursor.execute(sql_statement, (pk,))
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


def check_value_not_exist(cursor, value_name, value, table):
    sql_statement = "SELECT rowid FROM " + table + " WHERE " + value_name + " = ?"
    cursor.execute(sql_statement, (value,))
    data = cursor.fetchall()
    if len(data) == 0:
        return True
    else:
        print('This ' + value_name + ' already exists. Please check source and enter another value')
        return False


def extract_multiple_value_select_column(conn, columns, table='block_list', file_number='test', col_select='block_id',
                                         col_filter='block_type', col_filter_value='biopsy'):
    # extracts multiple values (columns) form a row/rows in a table defined by presence of a filter value
    # (col_filter_value) in a defined column (col_filter). Returns only a single column (col_select)

    sql_statement = ('SELECT ' + ", ".join(columns) + " FROM '" + table + "' WHERE file_number = '" + file_number +
                     "' AND " + col_filter + " = '" + col_filter_value + "'")
    df = pd.read_sql(sql_statement, conn)
    data = set(df[col_select])
    return list(data)


def extract_multiple_value_select_column_pk(conn, columns, table='block_list',
pk='test', col_select='block_id', col_filter='block_type', col_filter_value='biopsy'):
    sql_statement = ('SELECT ' + ", ".join(columns) + " FROM '" + table + "' WHERE pk = '" + pk +
                     "' AND " + col_filter + " = '" + col_filter_value + "'")
    df = pd.read_sql(sql_statement, conn)
    data = set(df[col_select])
    if len(data) == 1:
        data = list(data)[0]
    else:
        data = list(data)
    return data


def extract_select_column_key(conn, columns, table, col_select, key_name, key_value):
    # extracts multiple values (columns) form a row/rows in a table defined by presence of a key value
    # (key_value) in a defined column (key_name). Returns a set from only a single column (col_select)
    sql_statement = ('SELECT ' + ", ".join(columns) + " FROM '" + table + "' WHERE " + key_name + " = '" + key_value +
                     "'")
    df = pd.read_sql(sql_statement, conn)
    data = set(df[col_select])
    if len(data) == 1:
        data = list(data)[0]
    else:
        data = list(data)
    return data


def add_pk_fk_to_table(conn, cursor, table, col_name, pk):
    sql_insert = "INSERT INTO " + table + "(" + col_name + ") VALUES (?)"
    cursor.execute(sql_insert, (pk, ))
    conn.commit()

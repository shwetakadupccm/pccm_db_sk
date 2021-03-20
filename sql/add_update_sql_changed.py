import helper_function.ask_y_n_statement as ask
import add_edit.add_new as add_new
import add_edit.edit_record as edit_record
    
	
def update_single(conn, cursor, table, column, file_number, var):
    # update a single column in a sql db. Key is file_number.
    sql_update = "UPDATE " + table + " SET " + column + "= ? WHERE file_number = '" + file_number + "'"
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

def insert_file_number (conn, cursor, file_number):
    # insert data in multiple cols in a sql db. adds a new row
    sql_insert = "INSERT INTO Patient_Information_History(file_number) VALUES (?)"
    cursor.execute(sql_insert, file_number)
    conn.commit()

def update_multiple(conn, cursor, table, columns, file_number, data):
    # update multiple columns in a sql db. Key is file_number.
    col_number = len(data)
    for index in range(0, col_number):
        sql_update = "UPDATE " + table + " SET " + columns[index] + "= ? WHERE file_number = '" + file_number + "'"
        var = data[index]
        cursor.execute(sql_update, [var])
    conn.commit()


def add_columns(cursor, table, columns):
    col_number = len(columns)
    for index in range(0, col_number):
        sql_add = "ALTER TABLE " + table + " ADD " + columns[index]
        cursor.execute(sql_add)

def review_input (file_number, columns, data):
    col_number = len (data)
    print ("Entries for database are as follows : ")
    for index in range (0, col_number):
        print (columns[index] +": " + data[index])
    ans = ask.ask_y_n("Are entries for file "+ file_number+ " correct ?", True, False)
    return ans

def review_data (conn, cursor, table, file_number, col_list):
    sql_statement = ('SELECT '+ ", ".join(col_list) +' FROM '+ table + " WHERE file_number = '" +file_number+"'")
    data = cursor.execute(sql_statement)
    data_list = data.fetchall()
    data_list = list(data_list[0])
    col_number = len(col_list)
    if data_list== [None]*len(data_list):
        print("This section of the database has not been entered")
        enter = ask.ask_y_n("Do you want to enter now")
        return enter
    if None in set(data_list):
        print("Some entries are missing from the database: ")
        for index in range (0, col_number):
            print (col_list[index]+ " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to proceed?", ["Edit all", "Add new data only"])
        if enter == "Edit all":
            return True
        else:
            edit_few(conn, cursor, table, col_list, file_number, data_list)
    else:
        print("Entries present in database are as follows : ")
        for index in range (0, col_number):
            print (col_list[index]+ " : " + str(data_list[index]))
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

def edit_few(conn, cursor, table, col_list, file_number, data_list):
    col_number = len (col_list)
    for index in range (0, col_number):
        if data_list[index] == None:
            data = input ("Data for "+col_list[index]+": ")
            update_single(conn, cursor, table, col_list[index], file_number, data)
    return False


def check_file(conn, cursor, table, file_number, user_name, folders):
    sql_statement = "SELECT rowid FROM " + table + " WHERE file_number = ?"
    cursor.execute(sql_statement, (file_number, ))
    data = cursor.fetchall()
    if len(data) == 0:
        if table != "Follow_up_Data":
            cursor.execute("INSERT INTO " + table + "(file_number) VALUES ('" + file_number + "')")
        print(file_number + " does not exist in table " + table + ". Enter new record")
        add_new.add_new(conn, cursor, file_number, table, user_name,folders)
    else:
        todo = ask.ask_option(file_number + " already exists in table " + table + ".",
                                            ["Edit record", "Add new record for same file number", "Edit None"])
        if todo == "Edit record":
            edit_record.edit_record(conn, cursor, file_number, table, user_name, folders)
        elif todo == "Add new record for same file number":
            print("Add additional record module TBD")
    ask_table = ask.ask_y_n("Add another table?")
    return ask_table

def review_df(df):
   print(df.to_string())
   check = ask.ask_y_n("Is data entered correct?")
   return check


def table_check(cursor, table_name):
    x = cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + table_name + "'")
    [table_exists] = cursor.fetchall()
    test = list(table_exists)[0]
    return test


def view_multiple(conn, table, col_list, file_number):
    import pandas as pd
    from helper_function.ask_y_n_statement import ask_option
    sql_statement = ('SELECT '+ ", ".join(col_list) +' FROM '+ table + " WHERE file_number = '" +file_number+"'")
    df = pd.read_sql(sql_statement, conn)
    print_df(df)
    enter = ask_option("Do you want to add or edit data", ["Add data", 'Edit data', 'Do not add or edit'])
    return enter


def delete_multiple(cursor, table, file_number):
    sql_statement = "DELETE FROM " + table + " WHERE file_number = '" + file_number + "'"
    cursor.execute(sql_statement)


def delete_rows(cursor, table, col_name, col_data):
    sql_statement = "DELETE FROM " + table + " WHERE "+col_name+" = '" + col_data + "'"
    cursor.execute(sql_statement)

def review_df_row(df):
    import helper_function.ask_y_n_statement as ask
    check_row = len(df)-1
    print(df.iloc[check_row].to_string())
    check = ask.ask_y_n("Is data entered correct?")
    if check:
        return check, df
    else:
        df = df.drop(df.index[check_row])
        return check, df

def get_sql_data(file_number, conn, module, table):
    import helper_function.table_dicts as table_dicts
    import pandas as pd
    columns = []
    cols = table_dicts.db_dict(table, module)
    columns = columns + cols
    col_list = table_dicts.create_col_list(columns)
    sql_statement = ('SELECT ' + ", ".join(col_list) + " FROM '" + str(table) + "' WHERE file_number = '" + file_number + "'")
    df = pd.read_sql(sql_statement, conn)
    return df

def get_value(col_name, table, file_number, cursor, error_statement):
    try:
        sql_statement = "SELECT "+col_name+" FROM " +table+" WHERE file_number = '" + file_number + "'"
        cursor.execute(sql_statement)
        value_ = cursor.fetchall()
        value = value_[0][0]
    except:
        value = input(error_statement)
    return value

def print_df(df):
    rows = (df.shape)[0]
    for row in range(0, rows):
        print(df.iloc[row].to_string() + '\n')

def edit_table(df, pk_col, df_col):
    import helper_function.ask_y_n_statement as ask
    rows = (df.shape)[0]
    for row in range(0,rows):
        print(df.iloc[row].to_string()+'\n')
    to_correct = ask.ask_y_n("Are entries correct?")
    if not to_correct:
        to_correct = ask.ask_y_n("Re-enter entire table?")
        if to_correct:
            return to_correct, df
        else:
            change_row = True
            while change_row:
                pk_list = list(df[pk_col])
                print(pk_list)
                pk = input("Enter " + pk_col + " to change: ")
                index = pk_list.index(id)
                to_do = True
                while to_do:
                    print(df.loc[index, :])
                    col_change = ask.ask_option("Name of column to change", df_col)
                    old_val = df.loc[index, col_change]
                    print(old_val + '\n')
                    new_val = input("Enter correct value for " + col_change + ' for ' + pk + ": ")
                    df.loc[index, col_change] = new_val
                    print(df.iloc[index].to_string() + '\n')
                    to_do = ask.ask_y_n("Make more changes to " + pk_col + ' ' + pk + '?')
                print_df(df)
                change_row = ask.ask_y_n("Change another row?")
            to_correct = False
    return to_correct, df


def get_block_id_multiple (col_name, table, file_number, block_type, cursor):
    #mutliple results for block_id with multiple entries and 1 block_type
    try:
        sql_statement = "SELECT "+ col_name +" FROM " +table+" WHERE file_number = '" + file_number + "' AND block_type = '"\
              + block_type + "'"
        cursor.execute(sql_statement)
        values = cursor.fetchall()
        value = [value[0] for value in values]
    except:
        value = 'NA'
    return value

def last_update():
    from datetime import datetime
    last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
    return last_update
import pandas as pd
import helper_function.ask_y_n_statement as ask

class AddUpdateEditSQL:

    def __init__(self, conn, cursor, table, column, file_number, data):
        self.conn = conn
        self.cursor = cursor
        self.table = table
        self.column = column
        self.file_number = file_number
        self.data = data

    def update_single(self, var):
        # update a single column in a sql db. Key is file_number.
        sql_update = "UPDATE " + self.table + " SET " + self.column + "= ? WHERE file_number = '" + self.file_number + \
                     "'"
        self.cursor.execute(sql_update, [var])
        self.conn.commit()

    def insert(self):
        # insert data in multiple cols in a sql db. adds a new row
        col_number = len(self.data)
        place_holder = ["?"] * col_number
        place_str = ",".join(place_holder)
        sql_insert = "INSERT INTO " + self.table + "(" + self.column + ") VALUES (" + place_str + ")"
        self.cursor.execute(sql_insert, self.data)
        self.conn.commit()

    def insert_file_number (self):
        # insert data in multiple cols in a sql db. adds a new row
        sql_insert = "INSERT INTO Patient_Information_History(file_number) VALUES (?)"
        self.cursor.execute(sql_insert, self.file_number)
        self.conn.commit()

    def update_multiple(self):
        # update multiple columns in a sql db. Key is file_number.
        col_number = len(self.data)
        for index in range(0, col_number):
            sql_update = "UPDATE " + self.table + " SET " + self.column[index] + "= ? WHERE file_number = '" \
                         + self.file_number + "'"
            var = self.data[index]
            self.cursor.execute(sql_update, [var])
        self.conn.commit()

    def add_columns(self):
        col_number = len(self.column)
        for index in range(0, col_number):
            sql_add = "ALTER TABLE " + self.table + " ADD " + self.column[index]
            self.cursor.execute(sql_add)


    def edit_few(self):
        col_number = len (self.column)
        for index in range (0, col_number):
            if self.data[index] == None:
                data = input ("Data for "+self.column[index]+": ")
                AddUpdateEditSQL.update_single(self, data)
        return False

    def view_multiple(self):
        sql_view = ('SELECT '+ ", ".join(self.column) +' FROM '+ self.table + " WHERE file_number = '" +self.file_number+"'")
        df = pd.read_sql(sql_view, self.conn)
        print_df(df)
        enter = ask.ask_option("Do you want to add or edit data", ["Add data", 'Edit data'])
        return enter



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

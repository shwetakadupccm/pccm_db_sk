import helper_function.ask_y_n_statement as ask
from sql.add_update_sql import update_single, edit_few
import add_edit.add_new as add_new
import add_edit.edit_record as edit_record


class ReviewSQL:
    def __init__(self, conn, cursor, file_number, user_name, table, columns, data):
        self.table = table
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.columns = columns
        self.data = data

    def review_input(self):
        col_number = len(self.data)
        print("Entries for database are as follows : ")
        for index in range(0, col_number):
            print(self.columns[index] + ": " + self.data[index])
        ans = ask.ask_y_n("Are entries for file " + self.file_number + " correct ?", True, False)
        return ans

    def review_data(self):
        sql = ('SELECT ' + ", ".join(self.columns) + ' FROM ' + self.table + " WHERE file_number = '" +
               self.file_number + "'")
        data = self.cursor.execute(sql)
        data_list = data.fetchall()
        data_list = list(data_list[0])
        col_number = len(self.columns)
        if data_list == [None]*len(data_list):
            print("This section of the database has not been entered")
            enter = ask.ask_y_n("Do you want to enter now")
            return enter
        if None in set(data_list):
            print("Some entries are missing from the database: ")
            for index in range(0, col_number):
                print(self.columns[index] + " : " + str(self.data[index]))
            enter = ask.ask_option("Do you want to proceed?", ["Edit all", "Add new data only"])
            if enter == "Edit all":
                return True
            else:
                edit_few(self.conn, self.cursor, self.table, self.columns, self.file_number, self.data)
        else:
            print("Entries present in database are as follows : ")
            for index in range(0, col_number):
                print(self.columns[index] + " : " + str(self.data[index]))
            enter = ask.ask_option("Do you want to", ["Edit all", "Edit some entries", "Edit None"])
            if enter == "Edit some entries":
                for index in range(0, col_number):
                    print(self.columns[index] + " : " + str(self.data[index]))
                    edit = ask.ask_y_n("Edit")
                    if edit:
                        data = input("Data for " + self.columns[index] + ": ")
                        update_single(self.conn, self.cursor, self.table, self.columns, self.file_number, data)
                return False
            elif enter == "Edit all":
                return True
            else:
                return False

    def check_file(self, folders):
        sql = "SELECT rowid FROM " + self.table + " WHERE file_number = ?"
        self.cursor.execute(sql, (self.file_number,))
        data = self.cursor.fetchall()
        if len(data) == 0:
            if self.table != "Follow_up_Data":
                self.cursor.execute("INSERT INTO " + self.table + "(file_number) VALUES ('" + self.file_number + "')")
            print(self.file_number + " does not exist in table " + self.table + ". Enter new record")
            add_new.add_new(self.conn, self.cursor, self.file_number, self.table, self.user_name, folders)
        else:
            todo = ask.ask_option(self.file_number + " already exists in table " + self.table + ".", ["Edit record",
                                                                                                      "Add new record "
                                                                                                      "for same file "
                                                                                                      "number",
                                                                                                      "Edit None"])
            if todo == "Edit record":
                edit_record.edit_record(self.conn, self.cursor, self.file_number, self.table, self.user_name, folders)
            elif todo == "Add new record for same file number":
                print("This option is not available for this table")
        asked = ask.ask_y_n("Add another table?")
        return asked

    @staticmethod
    def review_df(df):
        print(df.to_string())
        check = ask.ask_y_n("Is data entered correct?")
        return check

    def table_check(self):
        x = self.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + self.table + "'")
        [table_exists] = self.cursor.fetchall()
        test = list(table_exists)[0]
        return test

    @staticmethod
    def review_df_row(df):
        check_row = len(df) - 1
        print(df.iloc[check_row].to_string())
        check = ask.ask_y_n("Is data entered correct?")
        if check:
            return check, df
        else:
            df = df.drop(df.index[check_row])
            return check, df

    @staticmethod
    def print_df(df):
        rows = df.shape[0]
        for row in range(0, rows):
            print(df.iloc[row].to_string() + '\n')

    @staticmethod
    def edit_table(df, pk_col, df_col):
        rows = df.shape[0]
        for row in range(0, rows):
            print(df.iloc[row].to_string() + '\n')
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
                    pk_change = input("Enter " + pk_col + " to change: ")
                    index = pk_list.index(id)
                    to_do = True
                    while to_do:
                        print(df.loc[index, :])
                        col_change = ask.ask_option("Name of column to change", df_col)
                        old_val = df.loc[index, col_change]
                        print(old_val + '\n')
                        new_val = input("Enter correct value for " + col_change + ' for ' + pk_change + ": ")
                        df.loc[index, col_change] = new_val
                        print(df.iloc[index].to_string() + '\n')
                        to_do = ask.ask_y_n("Make more changes to " + pk_col + ' ' + pk_change + '?')
                    ReviewSQL.print_df(df)
                    change_row = ask.ask_y_n("Change another row?")
                to_correct = False
        return to_correct, df

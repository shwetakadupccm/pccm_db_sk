import helper_function.ask_y_n_statement as ask
import sql.add_update_sql as sql
from helper_function.pccm_names import name_follow_up as names
import pandas as pd
from reports.longterm_therapy import patient_status


class FollowUp():
    def __init__(self, conn, cursor, file_number, user_name):
        self.conn = conn
        self.cursor = cursor
        self.file_number = file_number
        self.user_name = user_name
        self.table = "follow_up_data"
        self.col_list = names()

    def follow_up(self):
        follow = True
        follow_index = 0
        col_list = ["file_number"] + names()

        follow_up_data = pd.DataFrame(columns=col_list)
        while follow:
            check = False
            while not check:
                time_follow = ask.ask_option("Follow-up Period", ["3 months", "6 months", "9 months", "1 year",
                                                                  "1 year, 3 months", "1 year, 6 months", "1 year, 9 months",
                                                                                "2 years", "2 years, 6 months", "3 years",
                                                                                "3 years, 6 months", "4 years",
                                                                                "4 years, 6 months", "5 years", "6 years",
                                                                                "7 years", "8 years", "9 years", "10 years",
                                                                                "Other"])
                follow_status = patient_status()
                follow_mammo, follow_mammo_date, follow_usg, follow_usg_date  = ("NA",)*4
                is_mammo = ask.ask_y_n('Is follow up mammogramm present?')
                if is_mammo:
                    follow_mammo_date = ask.check_date('Date of follow-up Mammograph? ')
                    follow_mammo = input("Results of Mammography (Please enter in the format (Observation(mass/calc/lesion "
                                         "etc)/Location/BIRADs)): ")
                is_usg = ask.ask_y_n('Is follow up USG abdomen/Pelvis present?')
                if is_usg:
                    follow_usg_date = ask.check_date('Date of follow-up USG abdomen/Pelvis? ')
                    follow_usg = input("Results of USG abdomen/Pelvis (Please enter in the format (Observation"
                                       "(mass/calc/lesion etc)/Location/BIRADs)): ")
                other_type_date, other_type, other_result = ("NA",) * 3
                follow_other = ask.ask_y_n("Are there other reports in follow-up?")
                if follow_other:
                    other_type_date_list = []
                    other_type_list = []
                    other_result_list = []
                    while follow_other:
                        other_type_date = ask.check_date('Date of other test: ')
                        other_type = input("Type of other report: ")
                        other_result = input("Result of "+other_type+": ")
                        other_type_date_list.append(other_type_date)
                        other_type_list.append(other_type)
                        other_result_list.append(other_result)
                        follow_other = ask.ask_y_n("Add more reports?")
                    all_data = [other_type_date_list, other_type_list, other_result_list]
                    all_data = ask.join_lists(all_data, "; ")
                    other_type_date, other_type, other_result = all_data
                follow_up_treatment = ask.ask_y_n('Was any oncological treatment given after follow up?')
                if not follow_up_treatment:
                    follow_up_treatment, follow_up_treatment_result = ['no_treatment_given',] * 2
                else:
                    follow_up_treatment = input('What follow up treatment was given?')
                    follow_up_treatment_result = input('What was the result of follow-up treatment ' +
                                                       follow_up_treatment + '?')
                data_list = [self.file_number, time_follow, follow_status, follow_mammo_date, follow_mammo,
                             follow_usg_date, follow_usg, other_type, other_type_date, other_result, follow_up_treatment,
                             follow_up_treatment_result, self.user_name, sql.last_update()]
                follow_up_data.loc[follow_index] = data_list
                check, follow_up_data = sql.review_df_row(follow_up_data)
            follow_index = follow_index + 1
            follow_up_period = list(follow_up_data.loc[:, "follow_up_period"])
            print("\n Follow up periods added: " + "; ".join(follow_up_period) + '\n')
            follow = ask.ask_y_n("Add another follow-up period?")
        return follow_up_data


    def add_data(self):
        data = self.follow_up()
        data.to_sql(self.table, self.conn, index=False, if_exists="append")


    def edit_data(self):
        enter = sql.view_multiple(self.conn, self.table, self.col_list, self.file_number)
        if enter == "Add data":
            data = self.follow_up()
            data.to_sql(self.table, self.conn, index=False, if_exists="append")
        elif enter == "Edit data":
            col_list_all = ["file_number"] + self.col_list
            sql_statement = ('SELECT ' + ", ".join(col_list_all) + " FROM '" + self.table + "' WHERE file_number = '" +
                             self.file_number + "'")
            df = pd.read_sql(sql_statement, self.conn)
            #df = df.dropna()
            # any row with None in it will be deleted.
            sql.print_df(df)
            # check_edit = False
            # while check_edit:
            check_edit, df = sql.edit_table(df, pk_col='follow_up_period', df_col=names(), update_by=self.user_name)
            if check_edit:
                sql.delete_rows(self.cursor, self.table, "file_number", self.file_number)
                df = self.follow_up()
                df.to_sql(self.table, self.conn, index=False, if_exists="append")
            else:
                sql.delete_rows(self.cursor, self.table, "file_number", self.file_number)
                df.to_sql("follow_up_data", self.conn, index=False, if_exists="append")
        else:
            print('\n No edits will be made to this t able\n')

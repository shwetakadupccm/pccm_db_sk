import textwrap
import datetime

def ask_option(category, options):
    option_remove = ["Data not available", "Other"]
    for remove in option_remove:
        try:
            options.remove(remove)
        except:
            options
    options = options + ["Data not in Report", "Requires Follow-up", "Requires Specialist Input", 'Other']
    option_list = []
    val = []
    for index in range(0, len(options)):
        var = [(str(index + 1) + ". " + options[index])]
        val.append(str(index + 1))
        option_list.append(var)
    option_flat = [item for sublist in option_list for item in sublist]
    option_flat = " ".join(option_flat)
    check = False
    while not check:
        print("\n","Enter " + category, "\n")
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=option_flat)
        print(string, "\n")
        answer = input("Enter option number: ")
        check = answer in set(val)
    ans_int = int(answer) - 1
    option_ = options[ans_int]
    if option_ == "Other":
        option = input("Details: ")
    else:
        option = option_
    return option

def ask_y_n(question: object, yes_ans: object = True, no_ans: object = False) -> object:
    option_list = ["1. Yes", "2. No"]
    option_flat = " ".join(option_list)
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2"}
    if answer == "1":
        option = yes_ans
    else:
        option = no_ans
    return option


def join_lists(all_data, sep):
    data_return = []
    for index in all_data:
        data_joint = sep.join(index)
        data_return.append(data_joint)
    return data_return

def ask_y_n_na(question, yes_ans = "Yes", no_ans = "No",
               na_ans = "Requires Follow-up"):
    option_flat = "1. Yes 2. No 3. " + na_ans
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2", "3"}
    if answer == "1":
        option = yes_ans
    elif answer == "2":
        option = no_ans
    else:
        option = na_ans
    return option

def ask_option_y_n(question, yes_ans = "Yes", no_ans = "No",
               ans_3 = "Requires Follow up", ans_4 = "Requires Specialist Input"):
    option_list = ["1. Yes", "2. No", "3. Requires Follow up", "4. Requires Specialist Input"]
    option_flat = " ".join(option_list)
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2", "3", "4"}
    if answer == "1":
        option = yes_ans
    elif answer == "2":
        option = no_ans
    elif answer == "3":
        option = ans_3
    else:
        option = ans_4
    return option
    return option


def check_date(date_string):
    checked_date = False
    inputDate = 'NA'
    while not checked_date:
        error = '\nDate entered is not valid\nDate must be in past and in dd.mm.yyyy format or NA\n'
        inputDate = input('\n' + date_string + '\n')
        is_valid_date = True
        if inputDate.lower() != 'na':
            try:
                day, month, year = inputDate.split('.')
                check_length = (len(year)==4 and len(day)==2 and len(month)==2)
                if not check_length:
                    is_valid_date = False
                    print(error)
                else:
                    try:
                       datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        print(error)
                        is_valid_date  = False
            except ValueError:
                print(error)
                is_valid_date = False
            if is_valid_date:
                checked_date = datetime.datetime.today() > datetime.datetime(int(year), int(month), int(day))
                if not checked_date:
                    print(error)
        else:
            checked_date= ask_y_n('Date is ' + inputDate + '. Is that correct?')
    return inputDate


def edit_table(df, pk_col, df_col, update_by):
    import sql.add_update_sql as sql
    rows = (df.shape)[0]
    for row in range(0,rows):
        print(df.iloc[row].to_string()+'\n')
    to_correct = ask_y_n("Are entries correct?")
    if not to_correct:
        print('To delete a single entry select No here and proceed')
        to_correct = ask_y_n("Re-enter entire table?")
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
                    col_change = ask_option("Name of column to change", df_col)
                    old_val = df.loc[index, col_change]
                    print(old_val + '\n')
                    new_val = input("Enter correct value for " + col_change + ' for ' + pk + ": ")
                    df.loc[index, col_change] = new_val
                    df.ix[index, 'update_by'] = update_by
                    df.ix[index, 'last_update'] = sql.last_update()
                    print(df.iloc[index].to_string() + '\n')
                    to_do = ask_y_n("Make more changes to " + pk_col + ' ' + pk + '?')
                sql.print_df(df)
                change_row = ask_y_n("Change another row?")
            to_correct = False
    return to_correct, df


def ask_list(category, choices):
    if type(choices) is not list:
        options = list(choices)
    elif choices == ['x']:
        options = ['Enter Value']
    else:
        options = choices
    option_list = []
    val = []
    i=1
    for option in options:
        var = [(str(i) + ". " + option)]
        val.append(str(i))
        option_list.append(var)
        i = i+1
    option_flat = [item for sublist in option_list for item in sublist]
    option_flat = " ".join(option_flat)
    check = False
    while not check:
        print("\n", "Enter " + category, "\n")
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=option_flat)
        print(string, "\n")
        answer = input("Enter option number: ")
        check = answer in set(val)
    ans_int = int(answer) - 1
    option_ = options[ans_int]
    if option_.lower() == "other":
        option = input("Details: ")
    elif option_.lower() =='enter value':
        option = input('Enter value of ' + category + ': ')
    else:
        option = option_
    return option


def check_number_input(number_statement, error):
    number = input(number_statement)
    number_check = False
    while not number_check:
        if number.upper() == 'NA':
            number_check = ask_y_n('Number is entered as NA. Is that correct?')
        else:
            try:
                int(number)
                number_check = True
            except ValueError:
                try:
                    float(number)
                    number_check = True
                except [ValueError, TypeError]:
                    print(error)
                    number_check = False
                    number = input(number_statement)
    return number


def check_date_or_today(date_string):
    checked_date = False
    inputDate = 'NA'
    error = '\nDate entered is not valid\nDate must be in past and in dd.mm.yyyy format or NA\n' 
    while not checked_date:
        inputDate = input('\n' + date_string + '\n')
        if inputDate.lower() == 'today':
            inputDate = datetime.date.today().strftime('%d.%m.%Y')
            checked_date = True
        else:
            is_valid_date = True
            if inputDate.lower() != 'na':
                try:
                    day, month, year = inputDate.split('.')
                    check_length = (len(year)==4 and len(day)==2 and len(month)==2)
                    if not check_length:
                        is_valid_date = False
                        print(error)
                    else:
                        try:
                            datetime.datetime(int(year), int(month), int(day))
                        except ValueError:
                            print(error)
                            is_valid_date  = False
                except ValueError:
                    print(error)
                    is_valid_date = False
                if is_valid_date:
                    checked_date = datetime.datetime.today() > datetime.datetime(int(year), int(month), int(day))
                    if not checked_date:
                        print(error)
            else:
                checked_date= ask_y_n('Date is ' + inputDate + '. Is that correct?')
    return inputDate


def nested_list(data_list):
    while any(isinstance(i, list) for i in data_list):
        data_list = [datum for data in data_list for datum in data]
    return data_list


def create_yes_no_options(data_type, yes='yes', no='no', not_cancer='not_breast_cancer'):
    base = data_type.lower().replace(" ", "_")
    ans_yes = base + "_" + yes
    ans_no = base + "_" + no
    na_ans = base + '_data_not_in_report'
    options = [ans_yes, ans_no, na_ans, not_cancer]
    return options

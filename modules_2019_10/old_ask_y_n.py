import modules.ask_y_n_statement as ask


def ask_symptom(symp_state):
    symp_y_n = input("Symptom of " + symp_state + "? (y/n) ")
    if str.lower(symp_y_n) == "y":
        symp_breast_right = input("Right Breast y/n: ")
        if str.lower(symp_breast_right) == "y":
            symp_breast_right = symp_state
            symp_duration_right = input("Duration of symptoms in right breast: ")
        else:
            symp_breast_right = None
            symp_duration_right = None
        symp_breast_left = input("Left Breast y/n: ")
        if str.lower(symp_breast_left) == "y":
            symp_breast_left = symp_state
            symp_duration_left = input("Duration of symptoms in left breast: ")
        else:
            symp_breast_left = None
            symp_duration_left = None
    else:
        symp_breast_right = None
        symp_duration_right = None
        symp_breast_left = None
        symp_duration_left = None
    RB = [symp_breast_right, symp_duration_right]
    LB = [symp_breast_left, symp_duration_left]
    data = [RB, LB]
    return data

def get_symptom(symp_state):
    all_data = []
    for index in range(0, len(symp_state)):
        var = ask_symptom(symp_state[index])
        all_data.append(var)
    return all_data

def get_rb_lb(all_data, pos):
    data_list = []
    data_index = len(all_data)
    for index in range(0, data_index):
        var = all_data[index][pos]
        data_list.append(var)
    return (data_list)

def other_symp(conn, cursor, file_number, table):
    import sql.add_update_sql as sql
    add_symp = True
    all_data = []
    while add_symp:
        other_symp = input("Type of symptom: ")
        symp_breast_right = input("Right Breast y/n: ")
        if str.lower(symp_breast_right) == "y":
            symp_breast_right = other_symp
            symp_duration_right = input("Duration of symptoms in right breast: ")
        else:
            symp_breast_right = None
            symp_duration_right = None
        symp_breast_left = input("Left Breast y/n: ")
        if str.lower(symp_breast_left) == "y":
            symp_breast_left = other_symp
            symp_duration_left = input("Duration of symptoms in left breast: ")
        else:
            symp_breast_left = None
            symp_duration_left = None
        RB = [symp_breast_right, symp_duration_right]
        LB = [symp_breast_left, symp_duration_left]
        data = [RB, LB]
        all_data.append(data)
        add_symp =  ask.ask_y_n("Include more symptoms?")
    rb = get_rb_lb(all_data, 0)
    rb_symp = list(filter(None, get_rb_lb(rb, 0)))
    rb_dur = list(filter(None, get_rb_lb(rb, 1)))
    lb = get_rb_lb(all_data, 1)
    lb_symp = list(filter(None, get_rb_lb(lb, 0)))
    lb_dur = list(filter(None, get_rb_lb(lb, 1)))
    data = [rb_symp, rb_dur, lb_symp, lb_dur]
    for index in range(0, len(data)):
        if not data[index]:
            data[index] = ["No other symptoms"]
        else:
            data[index] = ["; ".join(data[index])]
    data_flat = [item for sublist in data for item in sublist]
    new_data = tuple(data_flat)
    columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "RB_Other_Symptoms_duration"
    sql.update_multiple(conn, cursor, table, columns, file_number, new_data)
    return (new_data)
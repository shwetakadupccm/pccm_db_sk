import numpy as np
import random
from datetime import datetime
# import IndianNameGenerator
from dateutil.relativedelta import relativedelta


def gen_date(base_date):
    days = np.arange(0, 3650)
    base_date = np.datetime64(base_date)
    random_date = base_date + np.random.choice(days)
    return str(random_date)


def get_dob():
    base_date = np.datetime64('1931-01-01')
    years = np.arange(0, 75*365)
    dob = base_date + np.random.choice(years)
    return str(dob)


def get_age(base_date):
    end_date = datetime.today()
    base_time_obj = datetime.strptime(base_date, '%Y-%m-%d')
    age = relativedelta(end_date, base_time_obj).years
    return age


def get_years(start_date, end_date):
    end_time_obj = datetime.strptime(str(end_date), '%Y-%m-%d')
    start_time_obj = datetime.strptime(str(start_date), '%Y-%m-%d')
    years = relativedelta(end_time_obj, start_time_obj).years
    return years


def get_choice(options):
    i = random.randint(0, len(options)-1)
    return options[i]


def get_file_id():
    year = random.randint(10, 21)
    number = random.randint(10, 1000)
    file_number = str(number) + '/' + str(year)
    return file_number


def get_yes_no_na():
    options = ['yes', 'no', 'na']
    i = random.randint(0, len(options)-1)
    return options[i]


def get_bool():
    i = bool(random.getrandbits(1))
    return i


def get_yes_no():
    i = bool(random.getrandbits(1))
    ans = 'no'
    if i:
        ans = 'yes'
    return ans


def get_number(max_no):
    i = random.randint(1, max_no)
    return i


def get_number_lt(min_lt, max_lt):
    if max_lt < min_lt:
        max_lt = min_lt + 1
    i = random.randint(min_lt, max_lt)
    return i


# def get_name(): 
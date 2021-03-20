import helper_function.ask_y_n_statement as ask
import os
import pandas as pd
import helper_function.option_lists as options
import datetime
import re
# import numpy as np


class I2B2:
    """ class I2B2 is a set of functions useful in converting pccm_db tables to facts.csv file suitable for i2b2 etl.
    It includes some basic validation of data for data types expected by concepts.csv.

    scode is a simple code that is used as a key to retrieve other values associated with that code
    such as the 1. formal code i.e. fcode (from public db formats)
    2. the options available if it is Enum type of value, i.e, categorical - these are retrieved from other
    available dicts in pccm_db - to maintain uniformity and ease of programming.
    3. to identify column names from input db when creating facts"""

    def __init__(self, db_file_name, version_name, db_type, partial=False):
        self.db_file_name = db_file_name
        self.version_name = version_name
        self.db_type = db_type
        self.partial = partial

    def create_i2b2_fact(self):
        file_dir = os.path.join('d:\\repos', 'i2b2', self.version_name)
        db_path = os.path.join(file_dir, self.db_file_name)
        fact_path = os.path.join(file_dir, 'facts.csv')
        invalid_path = os.path.join(file_dir, 'invalid_facts.csv')
        concept_path = os.path.join(file_dir, 'concepts.csv')
        concept = pd.read_csv(concept_path)
        fact_df = pd.DataFrame(columns=['EncounterID', 'mrn', 'code', 'ProviderID', 'StartDate', 'ModifierCD',
                                        'InstanceNum', 'value', 'UnitCD'])
        invalid = pd.DataFrame(columns=['file_number', 'column', 'value'])
        db_df = pd.read_excel(db_path)
        db_df = db_df.fillna('NA')
        if self.partial:
            db_df = db_df.head()
        col_list = db_df.columns.to_list[1:]
        patient_number = range(0, len(list(db_df['file_number'])))
        for patient in patient_number:
            patient_id = list(db_df['file_number'])[patient-1]
            print(str(patient) + ': ' + patient_id)
            for col in options.DateCols.col_date.keys():
                if col in col_list:
                    query_stat = "file_number == '" + patient_id + "'"
                    value = list(db_df.query(query_stat)[col])
                    value = " ".join(map(str, value))
                    try:
                        start_date = ask.date_format_datetime(value).strftime("%Y-%m-%d")
                    except ValueError:
                        start_date = datetime.date.today().strftime('%Y-%m-%d')
                        index = patient_id + col
                        invalid.loc[index] = [patient_id, col, value]
                    col_facts = options.DateCols.col_date.get(col)
                    for col_fact in col_facts:
                        value = list(db_df.query(query_stat)[col_fact])
                        value = " ".join(map(str, value))
                        '''scode is a simple code that is used as a key to retrieve other values associated with that code 
                        such as the 1. formal code i.e. fcode (from public db formats)
                        2. the options available if it is Enum type of value, i.e, categorical - these are retrieved from other 
                        available dicts in pccm_db - to maintain uniformity and ease of programming. 
                        3. to identify column names from input db when creating facts
                        4. Identify the appropriate date column to use for StartDate'''
                        scode = options.cd_db_dict(self.db_type).get(col_fact)
                        code = options.cd_formal_cd_dict(self.db_type).get(scode)
                        unit = options.cd_unit_dict(self.db_type).get(scode)
                        patient_id = str.replace(patient_id, "/", "-")
                        index = patient_id + col_fact
                        valid_fact = ValidateFact(concept, value, code)
                        if not valid_fact:
                            index = patient
                            invalid.loc[index] = [patient_id, col, value]
                        fact_df_row = [None, patient_id, code, None, start_date, None, None, value, unit]
                        fact_df.loc[index] = fact_df_row
        fact_df.to_csv(fact_path, sep=',', header=True, index=False, na_rep='')
        invalid.to_csv(invalid_path, sep=',', header=True, index=False)

    # def validate_fact(self, code, value):
    #     file_dir = os.path.join('d:/repos', '', self.version_name)
    #     concept_path = os.path.join(file_dir, 'concept.csv')
    #     con_df = pd.read_csv
    #     codetypes = con_df['code', 'type']
    #     for type_val in codetypes['type']:
    #         opt_dict = {}
    #         if type_val.startswith('Enum'):
    #             opts = str.split(type_val, '(')[1]
    #             opts = str.split(opts, '|')
    #             opts_list = [(str.removeprefix(opt, '"')) for opt in opts]
    #             opts_list = [(str.removesuffix(opt, '"')) for opt in opts]
    #             code = codetypes.query("type == '" + type_val + "'")[0]
    #             dict_var = {code: opts_list}
    #             opt_dict = opt_dict.update(dict_var)
    #     facts_path = os.path.join(file_dir, self.db_file_name)
    #     facts = pd.read_excel(facts_path)
    #     for code in opt_dict.keys():
    #         db_col_name = options.cd_db_dict(self.db_type).get(code)
    #
    # def create_false_data(self, n_ids):
    #     rn = np.random.randint(low=1, high=900, size=n_ids,dtype='int64')
    #     rn_id = 'fake_' + rn


# def create_enum(scode):
    # opts_list =
#todo: check validatefact methods. Not catching anything except absent dates.

class ValidateFact:

    def __init__(self, concept, value, code):
        self.concept = concept
        self.value = value
        self.fact_type = self.concept.query('code == "' + code + '"')

    def get_params(self):
        x = self.fact_type.replace(' ', '')
        x = x.split('"')
        params = []
        for param in x:
            if param not in {'Enum(', ',', ')'}:
                params.append(param)
        return params

    def check_for_single_value(self):
        test = True
        check = re.search('[:|;]', self.value)
        print(check)
        if not check:
            test = False
        return test

    def get_check_fact(self):
        test = False
        check = self.check_for_single_value()
        if check:
            test = self.value
        elif re.search('^Enum', self.fact_type):
            params = self.get_params()
            if self.value in params:
                test = self.value
        elif self.fact_type == 'PosInt':
            try:
                test = int(self.value)
            except ValueError:
                return test == self.value
        elif self.fact_type == 'String':
            test = str(self.value)
        else:
            test = False
        return test == self.value


if __name__ == "__main__":
    i2b2 = I2B2(db_file_name='426_test_dk.xlsx', version_name='i2b2-clinical_1', db_type='ffpe', partial=True)
    # will execute only when run as default script
    i2b2.create_i2b2_fact()


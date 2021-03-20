import helper_function.ask_y_n_statement as ask
from helper_function.option_lists import PathReports
import pandas as pd

class GetFacts:

    def __init__(self, concept, table):
        self.concept = pd.read_csv(concept)
        self.table = table

    def get_code_table(self):
        concept_cd = list(self.concept[['ConceptCD']].values)
        table_names = i2b2_dict.get(self.table)
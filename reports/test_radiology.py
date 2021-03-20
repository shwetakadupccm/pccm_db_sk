from unittest import TestCase
import pandas as pd
from additional_tables.radio_tables import MassCalcification
import mock
import module



class TestRadiology(TestCase):

    def __init__(self, table, col_list):
        super().__init__()
        self.table = table
        self.col_list = col_list

    def test_function(self):
        with mock.patch.object(__builtins__, 'input', lambda: 'some_input'):
            assert module == 'expected_output'

    if __name__ == "__main__":
        import helper_function.pccm_names as pccm_names
        table = 'mammography'
        col_list = pccm_names.names_radio_mass(table)
        # execute only if run as a script
        masscalc = MassCalcification(table, mammo_breast='right_breast', file_number='test', user_name='dk')
        masscalc.mammo_mass('1')
        masscalc.multiple_mass()


    TestCase.assertIs(self)
    pass

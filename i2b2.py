from i2b2.code_table import I2B2

if __name__ == "__main__":
    i2b2 = I2B2(db_file_name='426_test_dk.xlsx', version_name='i2b2-clinical_1', db_type='ffpe', partial=False)
    # will execute only when run as default script
    i2b2.create_i2b2_fact()

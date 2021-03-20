from add_edit import update_db_columns

folder_path = 'D://WorkDocs//Documents//db_ops//2021_02_22//all_db'
for db in db_list:
dB = 'PCCM_BreastCancerDB_2020_12_11_RB.db'
table = 'radiotherapy'
update = update_db_columns.UpdateColumns(folder_path, dB, table)
df, old_col = update.get_input_data()
update.drop_old_table()
update.create_table()
update.add_data(old_col, df)

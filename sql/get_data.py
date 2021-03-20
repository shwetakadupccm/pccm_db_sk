import helper_function.table_dicts as table_dicts
import pandas as pd

class GetSQL():

    def __init__(self,file_number, conn, module, table):
        self.file_number =  file_number
        self.conn = conn
        self.module = module
        self.table = table

def get_sql_data(file_number, conn, module, table):

    columns = []
    cols = table_dicts.db_dict(table, module)
    columns = columns + cols
    col_list = table_dicts.create_col_list(columns)
    sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + str(table) + "' WHERE file_number = '" + file_number + "'")
    df = pd.read_sql(sql, conn)
    return df

def get_value (col_name, table, file_number, cursor, error_statement):
    try:
        sql = "SELECT "+col_name+" FROM " +table+" WHERE file_number = '" + file_number + "'"
        cursor.execute(sql)
        value_ = cursor.fetchall()
        value = value_[0][0]
    except:
        value = input(error_statement)
    return value

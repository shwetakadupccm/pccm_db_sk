import smtplib
from email.mime.text import MIMEText
import add_edit.create_update_df as update
import helper_function.pccm_names as names
import pandas as pd
import os
import sqlite3

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'prashanti.database'
password = 'pccm123!'
sender = 'prashanti.database.gmail.com'
targets = ['dakelkar@gmail.com']
folders = "D:/repos/pccm_db/main/DB/from_linux"
file = "PCCM_BreastCancerDB_all_data_clean_28052018.db"
path = os.path.join(folders, file)
conn = sqlite3.connect(path)
cursor = conn.cursor()
status= []
file_number_all=pd.DataFrame()
for index in names.db_tables():
    index_status, file_number_table = update.weekly_data(conn, cursor, index)
    file_number_all = file_number_all.append(file_number_table)
    if type(index_status) == list:
        status_statement = 'Table ' + index + ' has a total of entries ' + str(
            index_status[0]) + ', New entries in past ' \
                               '7 days - ' + str(index_status[1])
    else:
        status_statement = 'Table '+ index+ ' ' +str(index_status)
        #+'by '+str(index_status[2]))
    status.append(status_statement)
status = "\n".join(status)
#file_number_all needs to be formatted further. change nan to False, change column order to File_number and then tables
# as arranged in db_tables. Have a summary column can logical be added up.. or replace by 0, 1 and then sum column can
# be added.
msg = MIMEText(status)
msg['Subject'] = 'PCCM Database status'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()

# add capability to send list of files added, with yes/no in each table.
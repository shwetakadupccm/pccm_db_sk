import os
from add_edit.email_db import send_email

send_email()
folders = "d:/repos/pccm_db/main/to_email"
file_sent = os.listdir(folders)
files = "; ".join(file_sent)
print("Files " + files + " sent by email")
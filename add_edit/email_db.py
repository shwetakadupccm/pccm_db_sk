import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
import os


def change_file_names():
    folders = "d:/repos/pccm_db/main/to_email"
    file_names = os.listdir(folders)
    names = []
    for file_name in file_names:
        if file_name.endswith('.db'):
            name = file_name[:-3]
            name = name + str(date.today()) + '.dbx'
            file_name_old = os.path.join(folders, file_name)
            file_name_new = os.path.join(folders, name)
            os.rename(file_name_old, file_name_new)
            names.append(file_name_new)
    return names


def send_email():
    """

    :rtype: object
    """
    subject = 'Database update for ' + str(date.today())+'\n\n'
    htmlbody = 'Attached are the database files updated for this week\n\n - Database operations'
    sender = 'prashanti.database@gmail.com'
    senderpass = 'pccm123!'
    recipients = ['dakelkar@gmail.com']
    attachments = change_file_names()
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    body = htmlbody
    msg.attach(MIMEText(body, 'plain'))
    for f in attachments:
        with open(f, "r+b") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % f)
            msg.attach(part)
#    server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.starttls()
    server.login(sender, senderpass)
    text = msg.as_string()
    server.sendmail(sender, recipients, text)
    server.quit()
    print('Email to ' + ", ".join(recipients) + ' has been sent with attachments '
          + "; ".join(attachments))
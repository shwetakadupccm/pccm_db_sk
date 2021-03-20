#from: https://datamakessense.com/easy-scheduled-emailing-with-python-for-typical-bi-needs/

# to query:
import sys
import ast
from datetime import datetime
from datetime import date
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText




class DbMail:
    def __init__(self):
        self.subject = 'Database update for '+ str(date.today())
        self.htmlbody = ''
        self.sender = 'prashanti.database.gmail.com'
        self.senderpass = 'pccm123!'
        self.recipients = ['dakelkar@gmail.com']
        self.attachments = change_file_names()

    def send(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.sender
        msg['Subject'] = self.subject
        msg['To'] = ", ".join(self.recipients)  # to must be array of the form ['mailsender135@gmail.com']
        msg.preamble = "preamble goes here"
        # check if there are attachments if yes, add them
        if self.attachments:
            self.attach(msg)
        # add html body after attachments
        msg.attach(MIMEText(self.htmlbody, 'html'))
        # send
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(self.sender, self.senderpass)
        s.sendmail(self.sender, self.recipients, msg.as_string())
        # test
        print (msg)
        s.quit()

    def htmladd(self, html):
        self.htmlbody = self.htmlbody + '<p></p>' + html

    def attach(self, msg):
        for f in self.attachments:

            ctype, encoding = mimetypes.guess_type(f)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"

            maintype, subtype = ctype.split("/", 1)

            if maintype == "text":
                fp = open(f)
                # Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "image":
                fp = open(f, "rb")
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "audio":
                fp = open(f, "rb")
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(f, "rb")
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=f)
            attachment.add_header('Content-ID', '<{}>'.format(f))
            msg.attach(attachment)

    def addattach(self, files):
        self.attachments = self.attachments + files


# example below
if __name__ == '__main__':
    # subject and recipients
    mymail = DbMail()
    # start html body. Here we add a greeting.
    mymail.htmladd('Hi, attached are the database files updated for this week')
    # Further things added to body are separated by a paragraph, so you do not need to worry about newlines for new sentences
    # here we add a line of text and an html table previously stored in the variable
    #mymail.htmladd('Daily sales')
    #mymail.htmladd(htmlsalestable)
    # another table name + table
    #mymail.htmladd('Daily bestsellers')
    #mymail.htmladd(htmlbestsellertable)
    # add image chart title
    #mymail.htmladd('Weekly sales chart')
    # attach image chart
    # mymail.addattach(['saleschartweekly.jpg'])
    # refer to image chart in html
    #mymail.htmladd('<img src="cid:saleschartweekly.jpg"/>')
    # attach another file
    #mymail.addattach(['bimail.py'])
    # send!
    mymail.send()
# Python code to illustrate Sending mail from
# from your gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("prashanti.database", "pccm123!")

# message to be sent
message = 'Madhura, \n For your records the email was set up with the following parameters: \n ' \
          'name: Prashanti Orchid, \n' \
          'password: pccm123!, \n' \
          'birthdate: April 1, 1990'

# sending the mail
s.sendmail("prashanti.database@gmail.com", "devakik@hotmail.com", message)

# terminating the session
s.quit()
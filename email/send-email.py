# #############################################
# Example of sending an email
# #############################################

# imports

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# set variables

smtpServer = 'smtp.server.com'
smptPort = 25
user = 'username'
pwd = 'password'
sender_email = 'my@email.com'
# for multple recpients, build a list of email addresses receiver_email = ['first@email.com', 'second@email.com']
receiver_email = 'someone@email.com'
message = 'Message in body of email.'


# build message

msg = MIMEMultipart()
msg['Subject'] = 'Subject Text'
msg['From'] = sender_email
# for multiple recipients, use the list msg['To'] = ", ".join(receiver_email)
msg['To'] = receiver_email
msg.attach(MIMEText(message, 'plain'))

# if you need to attach a file

fileondisk = 'my_file.txt'
f = open(fileondisk)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=fileondisk)
msg.attach(attachment)

# send email

smtpObject = smtplib.SMTP(smtpServer, smptPort)
smtpObject.sendmail(sender_email, receiver_email, msg.as_bytes)
smtpObject.quit


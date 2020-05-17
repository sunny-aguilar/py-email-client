#!/usr/bin/env python3
#
#   This script implements a simple email client to prepare an email for
#   sending. The email and SMTP modules are used as the workhorses behind the
#   email and the OS module is used to work with the Operating System.
#
#
#   Author:     Sandro Aguilar
#   Date:       May 16, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# import os.path, mimetypes, smtplib, getpass
# from email.message import EmailMessage

# message = EmailMessage()

sender = 'me@gmail.com'
recipient = 'you@gmail.com'

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}'.format(sender, recipient)

# # email body
body = """Hey there!

    I'm learning to send emails using Python!"""

message.set_content(body)


# # MIME data
# attachment_path = './banana.gif'
# attachment_filename = os.path.basename(attachment_path)

# mime_type, _ = mimetypes.guess_type(attachment_path)
# print(mime_type)

# mime_type, mime_subtype = mime_type.split('/', 1)
# print(mime_type)
# print(mime_subtype)

# # add attachment
# with open(attachment_path, 'rb') as ap:
#     message.add_attachment(ap.read(),
#     maintype=mime_type,
#     subtype=mime_subtype,
#     filename=os.path.basename(attachment_path))


# # show message
# # print(message)


# # create a mail server
# mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# mail_server.starttls()
# mail_pass = getpass.getpass('Password?')
# # print(mail_pass)

# # login
# mail_server.login(sender, mail_pass)

# # send mail
# mail_server.send_message(message)

# # close connection
# mail_server.quit()


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# mail_content = '''Hello,
# This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
# Thank You
# '''

# #The mail addresses and password
# sender_address = 'sunny.aguilar@gmail.com'
# sender_pass = 'a1s2d3F$G%'
# receiver_address = 'vluedevil@yahoo.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 465) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')


import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
except:
    print('Something went wrong...')
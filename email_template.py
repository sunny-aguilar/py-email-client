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
import os.path, mimetypes, smtplib
from email.message import EmailMessage

message = EmailMessage()

sender = 'me@example.com'
recipient = 'you@example.com'

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}'.format(sender, recipient)

# email body
body = """Hey there!

    I'm learning to send emails using Python!"""

message.set_content(body)


# MIME data
attachment_path = './banana.gif'
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

# add attachment
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
    maintype=mime_type,
    subtype=mime_subtype,
    filename=os.path.basename(attachment_path))


# show message
print(message)

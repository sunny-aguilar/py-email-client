#!/usr/bin/env python3
#
#   This script implements a simple email client to prepare an email for
#   sending.
#
#
#   Author:     Sandro Aguilar
#   Date:       May 16, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os.path, mimetypes
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

print(message)


# MIME data
attachment_path = './banana.gif'
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)


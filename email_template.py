#!/usr/bin/env python3
#
#   This script implements a simple email client to prepare an email for
#   sending.
#
#
#   Author:     Sandro Aguilar
#   Date:       May 16, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
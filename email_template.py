#!/usr/bin/env python3
#
#   This script interacts with an API in order to upload client reviews on
#   the client's website. API is implemented using Django.
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


print(message)
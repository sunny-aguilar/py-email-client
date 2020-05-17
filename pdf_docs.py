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
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# report object
report = SimpleDocTemplate('report.pdf')

# get styles
styles = getSampleStyleSheet()

# report title
report_title = Paragraph('A Complete Inventory of My Fruit', styles['h1'])

# build report
report.build([report_title])
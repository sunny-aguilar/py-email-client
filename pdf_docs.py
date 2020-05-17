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
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# table data
fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# report object
report = SimpleDocTemplate('report.pdf')

# get styles
styles = getSampleStyleSheet()

# add report title
report_title = Paragraph('A Complete Inventory of My Fruit', styles['h1'])

# add table style
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]

# add pie graph
report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

# add report table data
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')

# build report
report.build([report_title, report_table, report_chart])
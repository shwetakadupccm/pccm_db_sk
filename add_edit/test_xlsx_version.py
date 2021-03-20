import xlsxwriter

workbook = xlsxwriter.Workbook('textbox.xlsx')
worksheet = workbook.add_worksheet()

print (xlsxwriter.__version__)

text = 'A simple textbox with some text'
worksheet.insert_textbox(4, 1, text)

workbook.close()
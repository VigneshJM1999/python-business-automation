import openpyxl
from openpyxl.styles import Font

wb = openpyxl.load_workbook('inventory.xlsx')
sheet = wb['Sheet1']

bold_font = Font(bold=True)

for cell in sheet['B2:B100']:
    if isinstance(cell[0].value, (int, float)) and cell[0].value < 10:
        cell[0].font = bold_font

wb.save('inventory_formatted.xlsx')
print("Formatting complete. Saved new file.")
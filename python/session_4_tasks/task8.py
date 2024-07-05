"""
Python program to parse header file and read all prototypess of function
and insert it into excel sheet with unique ID stat with IDX0

"""
from openpyxl import Workbook

wb = Workbook()

sheet = wb.active



prototypes = []
with open("calculator.h", "r") as f:
    for i, line in enumerate(f.readlines()):
        row = []
        row.append(line)
        row.append(f"ID{i}")
        prototypes.append(row)


sheet.append(["Prototype", "ID"])

for prototype in prototypes:
    sheet.append(prototype)

wb.save("prototypes.xlsx")
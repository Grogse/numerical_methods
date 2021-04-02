import numpy as np
import ludecomposition as lu
import oem

import openpyxl as excel
from openpyxl.styles import Alignment


data = np.loadtxt('input.txt')

wb = excel.Workbook()
ws = wb.active
j = 1

matrix_a = data[:, :len(data[0]) - 1]
vector_b = np.squeeze(np.asarray(data[:, len(data[0]) - 1:]))
matrix_lu = lu.matrix_to_lu(matrix_a)

x_1 = lu.solve_slay(matrix_lu, vector_b)
x_2 = oem.solve_slay(data)

ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=2)
ws.merge_cells(start_row=1, start_column=4, end_row=1, end_column=5)

ws.cell(row=j, column=1).value = 'LU'
ws.cell(row=j, column=4).value = 'OEM'

ws.cell(row=j, column=1).alignment = Alignment(horizontal='center')
ws.cell(row=j, column=4).alignment = Alignment(horizontal='center')

for i, k in zip(x_1, x_2):
    ws.cell(row=j + 1, column=1).value = 'x_' + str(j)
    ws.cell(row=j + 1, column=1).alignment = Alignment(horizontal='center')

    ws.cell(row=j + 1, column=4).value = 'x_' + str(j)
    ws.cell(row=j + 1, column=4).alignment = Alignment(horizontal='center')

    ws.cell(row=j + 1, column=2).value = i
    ws.cell(row=j + 1, column=2).alignment = Alignment(horizontal='center')

    ws.cell(row=j + 1, column=5).value = k
    ws.cell(row=j + 1, column=5).alignment = Alignment(horizontal='center')
    j += 1

wb.save("answer.xlsx")
wb.close()

print(x_1)
print(x_2)
print(np.array_equal(x_1, x_2))

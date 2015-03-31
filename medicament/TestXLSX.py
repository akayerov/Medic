'''
Created on 31 марта 2015 г.

@author: a_kayerov
'''
import openpyxl

wb = openpyxl.load_workbook("c:\\test.xlsx")
#sheet = wb['list1']
sheet = wb.active
val = sheet['A2'].value
sheet['A1'] = 1399
wb.save('c:\\test3.xlsx')


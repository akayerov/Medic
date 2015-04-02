# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.oper_with_base import create_new_report, save_doc, get_name
from medicament.models import Doc1
from django.db.models import Sum
from random import random
import openpyxl


def create_report_form1(periodInt, datef):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
    '''
    return create_new_report(1,Doc1,periodInt,datef)

def save_doc_form1(request, type, id_doc):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
    '''
    return save_doc(Doc1,set_fields_form1, is_valid_form1, request, type, id_doc)


def set_fields_form1(request, doc):
    ''' Заполнение полей модели данными формы . 
        Специфично для каждой формы
    '''
    doc.c1_1 = request.POST['c1_1'] 
    doc.c1_2 = request.POST['c1_2'] 
    doc.c1_3 = request.POST['c1_3'] 
    doc.c1_4 = request.POST['c1_4'] 
    doc.c1_5 = request.POST['c1_5'] 

    doc.c2_6 = request.POST['c2_6'] 
    doc.c2_7 = request.POST['c2_7'] 
    doc.c2_8 = request.POST['c2_8'] 

    doc.c3_1 = request.POST['c3_1'] 
    doc.c3_2 = request.POST['c3_2'] 
    doc.c3_3 = request.POST['c3_3'] 
    doc.c3_4 = request.POST['c3_4'] 
    doc.c3_5 = request.POST['c3_5'] 
    doc.c3_6 = request.POST['c3_6'] 
    doc.c3_7 = request.POST['c3_7'] 
    doc.c3_8 = request.POST['c3_8'] 

    doc.c4_1 = request.POST['c4_1'] 
    doc.c4_2 = request.POST['c4_2'] 
    doc.c4_3 = request.POST['c4_3'] 
    doc.c4_4 = request.POST['c4_4'] 
    doc.c4_5 = request.POST['c4_5'] 
    doc.c4_6 = request.POST['c4_6'] 
    doc.c4_7 = request.POST['c4_7'] 
    doc.c4_8 = request.POST['c4_8'] 


def is_valid_form1(doc):
    ''' Проверка заполнения формы на корректность 
        Специфично для каждой формы
    '''
    if int(doc.c1_1) < int(doc.c1_2) + int(doc.c1_3) + int(doc.c1_4) + int(doc.c1_5):
        ret = [False,'Итого по строке 1 меньше суммы по столбцам'] 
        return ret
    elif int(doc.c3_1) < int(doc.c3_2) + int(doc.c3_3) + int(doc.c3_4) + int(doc.c3_5) + int(doc.c3_6) + int(doc.c3_7) + int(doc.c3_8):
        ret = [False,'Итого по строке 3 меньше суммы по столбцам'] 
        return ret
    elif int(doc.c4_1) < int(doc.c4_2) + int(doc.c4_3) + int(doc.c4_4) + int(doc.c4_5) + int(doc.c4_6) + int(doc.c4_7) + int(doc.c4_8):
        ret = [False,'Итого по строке 4 меньше суммы по столбцам'] 
        return ret
    else:
        ret = [True,'OK']
        return ret

def calc_sum_form1(doc):
    ''' Возвращает Суммы данных отчетов
    '''
    aq = doc.aggregate(Sum('c1_1'),Sum('c1_2'),Sum('c1_3'),Sum('c1_4'),Sum('c1_5'), \
                       Sum('c2_6'),Sum('c2_7'),Sum('c2_8'), \
                       Sum('c3_1'),Sum('c3_2'),Sum('c3_3'),Sum('c3_4'),Sum('c3_5'),Sum('c3_6'),Sum('c3_7'),Sum('c3_8'), \
                       Sum('c4_1'),Sum('c4_2'),Sum('c4_3'),Sum('c4_4'),Sum('c4_5'),Sum('c4_6'),Sum('c4_7'),Sum('c4_8'), \
                      )
    
    s = [["Нозологии, рецептов",0,0,0,0,0,0,0,0],["Федеральные:льготополучатели",0,0,0,0,0,0,0,0],["Федеральные:рецепты",0,0,0,0,0,0,0,0],["Региональные:рецепты",0,0,0,0,0,0,0,0]]
   
    s[0][1] = aq['c1_1__sum']
    s[0][2] = aq['c1_2__sum']
    s[0][3] = aq['c1_3__sum']
    s[0][4] = aq['c1_4__sum']
    s[0][5] = aq['c1_5__sum']

    s[1][6] = aq['c2_6__sum']
    s[1][7] = aq['c2_7__sum']
    s[1][8] = aq['c2_8__sum']
 
    s[2][1] = aq['c3_1__sum']
    s[2][2] = aq['c3_2__sum']
    s[2][3] = aq['c3_3__sum']
    s[2][4] = aq['c3_4__sum']
    s[2][5] = aq['c3_5__sum']
    s[2][6] = aq['c3_6__sum']
    s[2][7] = aq['c3_7__sum']
    s[2][8] = aq['c3_8__sum']
 
    s[3][1] = aq['c4_1__sum']
    s[3][2] = aq['c4_2__sum']
    s[3][3] = aq['c4_3__sum']
    s[3][4] = aq['c4_4__sum']
    s[3][5] = aq['c4_5__sum']
    s[3][6] = aq['c4_6__sum']
    s[3][7] = aq['c4_7__sum']
    s[3][8] = aq['c4_8__sum']
     
 
    return s

def exp_to_excel_form1(doc):
    res =  calc_sum_form1(doc)
    name_file = get_name("\\medicament\\Form\\Form1.xlsx")

    wb = openpyxl.load_workbook(name_file)
    sheet = wb.active
    sheet['B8'] = res[0][1]
    sheet['C8'] = res[0][2]
    sheet['D8'] = res[0][3]
    sheet['E8'] = res[0][4]
    sheet['F8'] = res[0][5]

    sheet['G10'] = res[1][6]
    sheet['H10'] = res[1][7]
    sheet['I10'] = res[1][8]

    sheet['B11'] = res[2][1]
    sheet['C11'] = res[2][2]
    sheet['D11'] = res[2][3]
    sheet['E11'] = res[2][4]
    sheet['F11'] = res[2][5]
    sheet['G11'] = res[2][6]
    sheet['H11'] = res[2][7]
    sheet['I11'] = res[2][8]

    sheet['B13'] = res[3][1]
    sheet['C13'] = res[3][2]
    sheet['D13'] = res[3][3]
    sheet['E13'] = res[3][4]
    sheet['F13'] = res[3][5]
    sheet['G13'] = res[3][6]
    sheet['H13'] = res[3][7]
    sheet['I13'] = res[3][8]

    name_file =  get_name("\\medicament\\Form\\rep" + str(int(random()*100000000)) + ".xlsx") 
    wb.save(name_file)
    
    return name_file


    

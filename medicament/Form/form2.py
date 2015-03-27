# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.oper_with_base import create_new_report, save_doc
from medicament.models import Doc2

def create_report_form2(periodInt, datef):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
    '''
    return create_new_report(2,Doc2,periodInt,datef)

def save_doc_form2(request, type, id_doc):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
    '''
    return save_doc(Doc2,set_fields_form2, is_valid_form2,request, type, id_doc)

def set_fields_form2(request, doc):
    ''' Заполнение полей модели данными формы. 
        Специфично для каждой формы
    '''
    doc.c1_1 = request.POST['c1_1'] 
    doc.c1_2 = request.POST['c1_2'] 
    doc.c1_3 = request.POST['c1_3'] 
    doc.c1_4 = request.POST['c1_4'] 
    doc.c1_5 = request.POST['c1_5'] 
    doc.c1_6 = request.POST['c1_6'] 
    doc.c1_7 = request.POST['c1_7'] 
    doc.c1_8 = request.POST['c1_8'] 

    doc.c2_1 = request.POST['c2_1'] 
    doc.c2_2 = request.POST['c2_2'] 
    doc.c2_3 = request.POST['c2_3'] 
    doc.c2_4 = request.POST['c2_4'] 
    doc.c2_5 = request.POST['c2_5'] 

    doc.c3_1 = request.POST['c3_1'] 
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


def is_valid_form2(doc):
    ''' Проверка заполнения формы на корректность 
        Специфично для каждой формы
    '''
    if int(doc.c1_1) < int(doc.c1_2) + int(doc.c1_3) + int(doc.c1_4) + int(doc.c1_5) + int(doc.c1_6) + int(doc.c1_7) +  + int(doc.c1_8):
        ret = [False,'Итого по строке 1 меньше суммы по столбцам'] 
        return ret
    else:
        ret = [True,'OK']
        return ret
    
def calc_sum_form2(doc):
    ''' Возвращает Суммы данных отчетов
    '''
    s = [["Строка1",0,0,0,0,0,0,0,0],["Строка2",0,0,0,0,0,0,0,0],["Строка3",0,0,0,0,0,0,0,0],["Строка4",0,0,0,0,0,0,0,0]]
    for d in doc:
        s[0][1] = s[0][1] + d.c1_1
        s[0][2] = s[0][2] + d.c1_2
        s[0][3] = s[0][3] + d.c1_3
        s[0][4] = s[0][4] + d.c1_4
        s[0][5] = s[0][5] + d.c1_5
        s[0][6] = s[0][6] + d.c1_6
        s[0][7] = s[0][7] + d.c1_7
        s[0][8] = s[0][8] + d.c1_8

        s[1][1] = s[1][1] + d.c2_1
        s[1][2] = s[1][2] + d.c2_2
        s[1][3] = s[1][3] + d.c2_3
        s[1][4] = s[1][4] + d.c2_4
        s[1][5] = s[1][5] + d.c2_5

        s[2][1] = s[2][1] + d.c3_1
        s[2][5] = s[2][5] + d.c3_5
        s[2][6] = s[2][6] + d.c3_6
        s[2][7] = s[2][7] + d.c3_7
        s[2][8] = s[2][8] + d.c3_8

        s[3][1] = s[3][1] + d.c4_1
        s[3][2] = s[3][2] + d.c4_2
        s[3][3] = s[3][3] + d.c4_3
        s[3][4] = s[3][4] + d.c4_4
        s[3][5] = s[3][5] + d.c4_5
        s[3][6] = s[3][6] + d.c4_6
        s[3][7] = s[3][7] + d.c4_7
        s[3][8] = s[3][8] + d.c4_8
    return s


    

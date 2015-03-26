# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.models import Document,Doc_type, Hosp, Period, Role, Comment, Doc_Hosp
from django.core.exceptions import ObjectDoesNotExist
from pyexcelerate import Workbook
from random import random


def create_new_report(type,periodInt, datef):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
    '''
    period = Period.objects.get(pk=periodInt)
    num_rec = Document.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    
    for dh in Doc_Hosp.objects.filter(doc_type = type):
        doc = Document.objects.create(hosp=dh.hosp, period=period, datef=datef)
#        doc.save()
  
    return True

def add_action_in_comment(request, doc,  action):
    ''' Добавить лог действий по документу в комментарий
    '''
    comment = Comment.objects.create()
    comment.document = doc
    comment.action = action
    comment.user = request.user
    comment.save()
    return True

def save_doc(request,question_id):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
    '''
    doc = Document.objects.get(pk=question_id);
    set_fields(request,doc)

    if 'button_save' in request.POST:
        ret_mess = is_valid(doc)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.status = Document.EDIT
        doc.save()
    elif 'button_send_control' in request.POST:
        ret_mess = is_valid(doc)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.status = Document.WAITCONTROL
        actionComment = Comment.ON_CONTROL
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    elif 'button_isOK' in request.POST:
        doc.status = Document.COMPELETE
        actionComment = Comment.CONTROL_YES
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    elif 'button_isNotOK':    
        doc.status = Document.NEEDCHANGE
        actionComment = Comment.CONTROL_NO
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    return [True,'OK']

def set_fields(request,doc):
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


def is_valid(doc):
    ''' Проверка заполнения формы на корректность 
        Специфично для каждой формы
    '''
    if int(doc.c1_1) < int(doc.c1_2) + int(doc.c1_3) + int(doc.c1_4) + int(doc.c1_5) + int(doc.c1_6) + int(doc.c1_7) +  + int(doc.c1_8):
        ret = [False,'Итого по строке 1 меньше суммы по столбцам'] 
        return ret
    else:
        ret = [True,'OK']
        return ret
   
    
def calc_sum(doc):
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

def export_to_excel(doc):
    res = calc_sum(doc)
#    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # data is a 2D array
    wb = Workbook()
    wb.new_sheet("sheet name", data=res)
    name_file = ".\\static\\rep" + str(int(random()*100000000)) + ".xlsx" 
    wb.save(name_file)
    return name_file

    

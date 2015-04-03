# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.models import Document,Doc_type, Hosp, Period, Role, Comment, Doc_Hosp,Doc1,Doc2
from django.core.exceptions import ObjectDoesNotExist
import os
# хорошо  создает!
#from pyexcelerate import Workbook
# Умееет читать и изменять!!!!
import openpyxl
import datetime

def get_ids(str_id):
    l = str_id.split(',')
    return l

def create_new_report(type,doc,periodInt, datef):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
    '''
    period = Period.objects.get(pk=periodInt)
    num_rec = doc.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    for dh in Doc_Hosp.objects.filter(doc_type = type):
        odoc = doc.objects.create(hosp=dh.hosp, period=period, datef=datef)
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

def save_doc( tdoc, set_fields, is_valid, request, type, id_doc):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
    '''
    doc = tdoc.objects.get(pk=id_doc);


    if 'button_save' in request.POST:
        set_fields(request, doc)
        ret_mess = is_valid(doc)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.status = Document.EDIT
        doc.date_mod = datetime.datetime.now()
        doc.save()
    elif 'button_send_control' in request.POST:
        set_fields(request, doc)
        ret_mess = is_valid(doc)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.status = Document.WAITCONTROL
        actionComment = Comment.ON_CONTROL
        doc.date_mod = datetime.datetime.now()
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    elif 'button_isOK' in request.POST:
        ret_mess = is_valid(doc)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.date_mod = datetime.datetime.now()
        doc.status = Document.COMPELETE
        actionComment = Comment.CONTROL_YES
# Уступка - дает право изменять документ при согласовании, однако пройдя внутреннюю проверку is_valid
        set_fields(request, doc)
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    elif 'button_isNotOK':    
        doc.status = Document.NEEDCHANGE
        actionComment = Comment.CONTROL_NO
        doc.date_mod = datetime.datetime.now()
        doc.save()
        add_action_in_comment(request, doc, actionComment)
    return [True,'OK']

def get_name(namefile):
    return os.path.dirname(os.path.dirname(__file__)) +  namefile

    

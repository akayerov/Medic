# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.models import Document,Doc_type, Hosp, Period, Role, Region, Comment, Doc_Hosp,Doc1,Doc2
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

def create_new_report(type,doc,periodInt, datef, copyfunc):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
        Ищем документы за прежний период, если находим, то заполняем
    '''
    period = Period.objects.get(pk=periodInt)
    period_prev = period.prev
    num_rec = doc.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    for dh in Doc_Hosp.objects.filter(doc_type = type):
        odoc = doc.objects.create(hosp=dh.hosp, period=period, datef=datef)
        # если предыдущий период есть, попробуем заполнить документ из предыдущего
        if period_prev:       
            doc_prevList = doc.objects.filter(period = period_prev, hosp = dh.hosp, status='F')
            if doc_prevList:
                doc_prev = doc_prevList[0]
                copyfunc(doc_prev, odoc)
                odoc.save()
    return True

def get_doc_prev(doc, tdoc):
    '''
      Возвращает ЗАВЕРШЕННЫЙ документ предудущего периода или ничего
    '''
    period = Period.objects.get(pk=doc.period.id)
    period_prev = doc.period.prev
    doc_prevList = tdoc.objects.filter(period = period_prev, hosp = doc.hosp , status='F')
    if doc_prevList:
        return doc_prevList[0]
    else:
        return None


def add_action_in_comment(request, doc,  action):
    ''' Добавить лог действий по документу в комментарий
    '''
#    comment = Comment.objects.create()
    comment = Comment()
    comment.document = doc
    comment.action = action
    comment.user = request.user
    comment.save()
    return True

def save_doc( tdoc, set_fields, is_valid, request, type, id_doc, mode_comment):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
    '''
    doc = tdoc.objects.get(pk=id_doc);
    doc_prev = get_doc_prev(doc, tdoc)

    if 'button_save' in request.POST or 'button_export' in request.POST:
        set_fields(request, doc)
        ret_mess = is_valid(doc, doc_prev)
        doc.status = Document.EDIT
        doc.date_mod = datetime.datetime.now()
        doc.save()
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
    elif 'button_send_control' in request.POST:
        set_fields(request, doc)
        ret_mess = is_valid(doc, doc_prev)
        if not ret_mess[0]:      # [False,"Error_mess"]
            doc.status = Document.EDIT
            doc.date_mod = datetime.datetime.now()
            doc.save()
            return ret_mess 
        doc.status = Document.WAITCONTROL
        actionComment = Comment.ON_CONTROL
        doc.date_mod = datetime.datetime.now()
        doc.save()
        if mode_comment:
            add_action_in_comment(request, doc, actionComment)
    elif 'button_isOK' in request.POST:
        ret_mess = is_valid(doc,doc_prev)
        if not ret_mess[0]:      # [False,"Error_mess"]
            return ret_mess 
        doc.date_mod = datetime.datetime.now()
        doc.status = Document.COMPELETE
        actionComment = Comment.CONTROL_YES
# Уступка - дает право изменять документ при согласовании, однако пройдя внутреннюю проверку is_valid
        set_fields(request, doc)
        doc.save()
        if mode_comment:
            add_action_in_comment(request, doc, actionComment)
    elif 'button_isNotOK':    
        doc.status = Document.NEEDCHANGE
        actionComment = Comment.CONTROL_NO
        doc.date_mod = datetime.datetime.now()
        doc.save()
        if mode_comment:
            add_action_in_comment(request, doc, actionComment)
    return [True,'OK']

def get_name(namefile):
    return os.path.dirname(os.path.dirname(__file__)) +  namefile

def get_period(iperiod):
    if iperiod > 0:
        return Period.objects.get(pk=iperiod)
    else:
        return None

def get_region(iregion):
    if iregion > 0:
        return Region.objects.get(pk=iregion)
    else:
        return None

def get_period_namef(iperiod):
    if iperiod > 0:
        p = Period.objects.get(pk=iperiod)
        res = p.name + " (" + p.dateb.strftime("%d/%m/%y") + "-" + p.datee.strftime("%d/%m/%y") +")"
        return res
    else:
        return ""


# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.models import Document,Doc_type, Hosp, Period, Role, Comment, Doc_Hosp
from django.core.exceptions import ObjectDoesNotExist

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
    doc.c1_1 = request.POST['c1_1'] 
    if 'button_save' in request.POST:
        doc.status = Document.EDIT
        doc.save()
    elif 'button_send_control' in request.POST:
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



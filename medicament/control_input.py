# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from medicament.models import Document,Doc_type, Hosp, Period, Role
from django.core.exceptions import ObjectDoesNotExist

def create_new_report(type,period):
    ''' Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
    '''
    num_rec = Document.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    
    return False



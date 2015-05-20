# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from django.db.models import Sum
from random import random
import openpyxl
from openpyxl.styles import Font

from medicament.oper_with_base import create_new_report, save_doc, get_name, get_period_namef, get_region_name
from medicament.models import Doc3
from _datetime import datetime


def create_report_form3(periodInt, datef):
    ''' Создание новых документов (в новом периоде)
        Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
        copy_fields_formX - функция начального заполнения
    '''
    return create_new_report(3,Doc3,periodInt,datef, copy_fields_form3)

def save_doc_form3(request, type, id_doc, mode_comment):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
        Установить собственый параментрв DOCx,set_fields_formx, is_valid_formx
    ''' 
    return save_doc(Doc3,set_fields_form3, is_valid_form3, request, type, id_doc, mode_comment)


def copy_fields_form3(ds, dd):
    ''' Копирование полей - указать все поля для копирования 
        Для каждой формы, 
        ВЫЗЫВАЕТСЯ ТОЛЬКО ДЛЯ ДОКУМЕНТОВ В СОСТОЯНИИ ЗАВЕШЕНО- незаполненные и несогласаованные документы такой обработке не подлежат!
    '''
    dd.c1_1_1 = ds.c1_1_1 
    dd.c1_1_2 = ds.c1_1_2 
    dd.c1_2   = ds.c1_2
    dd.c2_1   = ds.c2_1
    dd.c2_2   = ds.c2_2
    dd.c3_1   = ds.c3_1
    dd.c3_2_1 = ds.c3_2_1
    dd.c3_2_2 = ds.c3_2_2
    dd.c4_1   = ds.c4_1 

def set_fields_form3(request, doc):
    ''' Заполнение полей модели данными формы . 
        Для каждой формы
    '''

    doc.c1_1_1 = request.POST['c1_1_1'] 
    doc.c1_1_2 = request.POST['c1_1_2'] 
    doc.c1_2 = request.POST['c1_2'] 
    doc.c2_1 = request.POST['c2_1'] 
    doc.c2_2 = request.POST['c2_2'] 
    doc.c3_1 = request.POST['c3_1'] 
    doc.c3_2_1 = request.POST['c3_2_1'] 
    doc.c3_2_2 = request.POST['c3_2_2'] 
    doc.c4_1 = request.POST['c4_1'] 
    


def is_valid_form3(doc, doc_prev):
    ''' Проверка заполнения формы на корректность 
    '''
    ret = [True,'OK']
    return ret

def calc_sum_form3(doc):
    ''' Возвращает Суммы данных отчетов
    '''
#    assert False
    aq0= doc.aggregate(Sum('c1_1_1'),Sum('c1_1_2'),Sum('c1_2'),Sum('c2_1'),Sum('c2_2'), Sum('c3_1'), \
                       Sum('c3_2_1'),Sum('c3_2_2'),Sum('c4_1'),Sum('c2_4_3'), \
         )
    
    s = [["2.1. Число врачей (без аспирантов, интернов и ординаторов), работающих в медицинских организациях субъекта Российской Федерации ", aq0['c2_1__sum']],
         ["2.2. Число среднего медицинского персонала, работающего в медицинских организациях субъекта Российской Федерации",aq0['c2_2__sum']],
         ]

    return s





def exp_to_excel_form3(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form3(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    if mode == 1:
        name_file = get_name("/static/Form/Form3.xlsx")
    else:
        name_file = get_name("/static/Form/Form3_All.xlsx")

    wb = openpyxl.load_workbook(name_file)
    sheet = wb.active
    sheet['B2'] = speriod
    sheet['B1'] = sregion
    if mode==0:
        sheet['B310'] = "Статистика по отчету"  
        sheet['B311'] = "Организаций предоставляющих, Всего"
        sheet['C311'] = stat.rec_all
        sheet['B312'] = "Отобрано в отчет, Всего"
        sheet['C312'] = stat.rec_fltr
        sheet['B313'] = "Завершено"
        sheet['C313'] = stat.rec_complete
        sheet['B314'] = "Согласование"
        sheet['C314'] = stat.rec_soglas
        sheet['B315'] = "Корректировка"
        sheet['C315'] = stat.rec_correct
        sheet['B316'] = "Редактирование"
        sheet['C316'] = stat.rec_edit


    startrow = 7 
    for i in range(0,296):
        srA = "B" + str(startrow + i)
        srB = "C" + str(startrow + i)
        sheet[srA] = res[i][0]
        sheet[srB] = res[i][1]
# вывод только для конкретной МО для все  не выводится        
    if mode == 1:
#        res = calc_valf3_form2(doc)
        startrow = 307 
        for i in range(0,38):
            srA = "B" + str(startrow + i)
            srB = "C" + str(startrow + i)
            sheet[srA] = res[i][0]
            sheet[srB] = res[i][1]
                
        sheet['A346'] = "Выведено в системе Мед+ " + str(datetime.now()) 
        sheet['A346'].font = Font(size=5)
    else:
        sheet['A318'] = "Выведено в системе Мед+ " + str(datetime.now()) 
        sheet['A318'].font = Font(size=5)
 
 #   name_file =  get_name("\\medicament\\Form\\rep" + str(int(random()*100000000)) + ".xlsx") 
    name_file =  get_name("/medicament/Form/rep" + str(int(random()*100000000)) + ".xlsx") 
    wb.save(name_file)
    
    return name_file


    

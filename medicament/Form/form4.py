# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
import os
from django.db.models import Sum
from random import random
import openpyxl
from openpyxl.styles import Font

from medicament.oper_with_base import create_new_report, save_doc, get_name, get_period_namef, get_region_name, get_name_input
from medicament.models import Document,Doc_type, Hosp, Period, Role, Region, Comment, Doc_Hosp,Doc1,Doc2, Rows
from medicament.oper_with_base import handle_uploaded_file

from medicament.modelsDoc4 import Doc4, Doc4Tab1000, Doc4Tab2000, Doc4Tab3000, Doc4Tab4000, Doc4Tab5000, Doc4Tab5001, Doc4Tab6000, Doc4Tab7000

from _datetime import datetime
from _overlapped import NULL


def create_report_form4(periodInt, datef):
    ''' Создание новых документов (в новом периоде)
        Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
        copy_fields_formX - функция начального заполнения
    '''
    # Более сложная функция создания новых отчетов - дополнительно создаются записи в подчиненных таблицах
    type = 4
    period = Period.objects.get(pk=periodInt)
    period_prev = period.prev
    num_rec = Doc4.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    for dh in Doc_Hosp.objects.filter(doc_type = type):
        odoc = Doc4.objects.create(hosp=dh.hosp, period=period, datef=datef)
        create_tab(4,odoc)     # создаем табличные части для нового отчета 4 - код мониторинга
        # если предыдущий период есть, попробуем заполнить документ из предыдущего
        if period_prev:       
            doc_prevList = Doc4.objects.filter(period = period_prev, hosp = dh.hosp, status='F')
            if doc_prevList:
                doc_prev = doc_prevList[0]
                copy_fields_form4(doc_prev, odoc)
                odoc.save()
                 
#    return create_new_report(4,Doc4,periodInt,datef, copy_fields_form4)
    return True

def create_tab(type, odoc):
    ''' создадим табличные записи для нового отчета 
    '''
    row = Rows.objects.filter(type  = type, table = 'tab1000')
    for r in row:
        otab1000 = Doc4Tab1000.objects.create(doc=odoc, row=r )
        otab1000.c3 = 100
        otab1000.c4 = 101
        otab1000.save()
    row = Rows.objects.filter(type  = type, table = 'tab2000')
    for r in row:
        otab2000 = Doc4Tab2000.objects.create(doc=odoc, row=r )
        otab2000.c3 = 200
        otab2000.c4 = 201
        otab2000.save()
    row = Rows.objects.filter(type  = type, table = 'tab3000')
    for r in row:
        otab3000 = Doc4Tab3000.objects.create(doc=odoc, row=r )
        otab3000.c3 = 300
        otab3000.c4 = 301
        otab3000.save()
    row = Rows.objects.filter(type  = type, table = 'tab4000')
    for r in row:
        otab4000 = Doc4Tab3000.objects.create(doc=odoc, row=r )
        otab4000.c4 = 400
        otab4000.c5 = 401
        otab4000.save()
    row = Rows.objects.filter(type  = type, table = 'tab5000')
    for r in row:
        otab5000 = Doc4Tab5000.objects.create(doc=odoc, row=r )
        otab5000.c4 = 500
        otab5000.c5 = 501
        otab5000.save()
    row = Rows.objects.filter(type  = type, table = 'tab5001')
    for r in row:
        otab5001 = Doc4Tab5001.objects.create(doc=odoc, row=r )
        otab5001.c4 = 500
        otab5001.c5 = 501
        otab5001.save()
    row = Rows.objects.filter(type  = type, table = 'tab6000')
    for r in row:
        otab6000 = Doc4Tab6000.objects.create(doc=odoc, row=r )
        otab6000.c4 = 600
        otab6000.c5 = 601
        otab5001.save()
    row = Rows.objects.filter(type  = type, table = 'tab7000')
    for r in row:
        otab7000 = Doc4Tab7000.objects.create(doc=odoc, row=r )
        otab7000.c4 = 700
        otab7000.c5 = 701
        otab7000.save()



def save_doc_form4(request, type, id_doc, mode_comment):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
        Установить собственый параментрв DOCx,set_fields_formx, is_valid_formx
    ''' 
    return save_doc(Doc4,set_fields_form4, is_valid_form4, request, type, id_doc, mode_comment)

def copy_fields_form4(ds, dd):
    pass
     

def set_fields_form4(request, doc):
    ''' Заполнение полей модели данными формы . 
        Для каждой формы
    '''
    if 'button_save' in request.POST:
        type = 4
    # поля формы (вне табличных частей)
        doc.KodMO = request.POST['KodMO']   
        doc.c7002 = request.POST['c7002'] 
    
    # Табличные части
    # tab1000
        table = 'tab1000'    
        tabrs = Doc4Tab1000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c4")]
            tab.save()
    # tab2000
        table = 'tab2000'    
        tabrs = Doc4Tab2000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c4")]
            tab.save()
            
    #  прочие табличные части заполнить аналогично
        row = Rows.objects.filter(type  = type, table = 'tab3000')
        for r in row:
            pass
        row = Rows.objects.filter(type  = type, table = 'tab4000')
        for r in row:
            pass
        row = Rows.objects.filter(type  = type, table = 'tab5000')
        for r in row:
            pass
        row = Rows.objects.filter(type  = type, table = 'tab5001')
        for r in row:
            pass
        row = Rows.objects.filter(type  = type, table = 'tab6000')
        for r in row:
            pass
        row = Rows.objects.filter(type  = type, table = 'tab7000')
        for r in row:
            pass

    


def is_valid_form4(doc, doc_prev):
    ''' Проверка заполнения формы на корректность 
    '''
    ret = [True,'OK']
    return ret

def calc_sum_form4(doc):
    ''' Возвращает Суммы данных отчетов
        В отличие от предыдущих отчетов кроме основной DOC используются дополнительные таблицы 
    '''
#   Суммирование по основной части документа
    period = doc[0].period
    aq1= doc.aggregate(Sum('c7002')
         )
    s1 = [["1. Показатель 7002", aq1['c7002__sum']],
        ]

#   суммирование табличных частей документа
#   ТАБЛИЦА 1000
    row = Rows.objects.filter(type  = 4, table = 'tab1000')
    s1000 = []
    for r in row:
        tab1000 = Doc4Tab1000.objects.filter(doc__period=period, row=r )
        aq1000 = tab1000.aggregate(Sum('c3'),Sum('c4'))
        obj = [tab1000[0].row,aq1000['c3__sum'],aq1000['c4__sum']]
        s1000.append(obj) 
#        print("Строки таблицы 1000")
#        for t in tab1000: 
#            print(t.row, t.c3, t.c4)
#   ТАБЛИЦА 2000
    row = Rows.objects.filter(type  = 4, table = 'tab2000')
    s2000 = []
    for r in row:
        tab2000 = Doc4Tab2000.objects.filter(doc__period=period, row=r )
        aq2000 = tab2000.aggregate(Sum('c3'),Sum('c4'))
        obj = [tab2000[0].row,aq2000['c3__sum'],aq2000['c4__sum']]
        s2000.append(obj) 
#        print("Строки таблицы 2000")
#        for t in tab2000: 
#            print(t.row, t.c3, t.c4)
# аналогично

# в сл строке довавить остальные табличные части
    res = {'doc':s1,'tab1000':s1000,'tab2000':s2000}
    return res





def exp_to_excel_form4(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form4(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    if mode == 1:
        name_file = get_name("/static/Form/Form4.xlsx")
    else:
        name_file = get_name("/static/Form/Form4_All.xlsx")

    wb = openpyxl.load_workbook(name_file)
    print(wb.get_sheet_names())

    tab = 'Doc'
    sheet = wb[tab]
#    sheet = wb.active
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

# Обшая часть
    startrow = 7 
    i = 0
    d = res['doc']
    for elem in d:
        srA = "B" + str(startrow + i)
        srB = "C" + str(startrow + i)
        sheet[srA] = elem[0]
        sheet[srB] = elem[1]
        i += 1
# Таблицы
    tab = 'tab1000'
    sheet1 = wb[tab]
    startrow = 12
    i = 0
    t = res[tab]
#    assert False
    for line in t:
        srA = "B" + str(startrow + i)
        srB = "C" + str(startrow + i)
        srC = "D" + str(startrow + i)
        sheet1[srA] = line[0].name
        sheet1[srB] = line[1]
        sheet1[srC] = line[2]
        i += 1
    
    
    sheet['A50'] = "Выведено в системе Мед+ " + str(datetime.now()) 
    sheet['A50'].font = Font(size=5)
 
 #   name_file =  get_name("\\medicament\\Form\\rep" + str(int(random()*100000000)) + ".xlsx") 
    name_file =  get_name("/medicament/Form/rep" + str(int(random()*100000000)) + ".xlsx") 
    wb.save(name_file)
    
    return name_file


def ret_val(sheetval):
    if sheetval == None:
        return 0
    else:    
        return sheetval
        
    
def load_from_excel_form4(request, doc_id):
    '''  загрузка формы их соответствующего Excel файла
    '''
#              
    namefile = handle_uploaded_file(request.FILES['filename'])
    doc  =  Doc4.objects.get(pk=doc_id)
    name_file = (namefile)
    wb = openpyxl.load_workbook(name_file)

# Общая часть
    tab = 'Doc'
    sheet = wb[tab]
    doc.c7002 = sheet["C7"].value
    doc.save()

# Таблицы
    tab = 'tab1000'
    sheet = wb[tab]
    tabrs = Doc4Tab1000.objects.filter(doc=doc)
    startrow = 12
    i = 0 
    for tab in tabrs:
        sr = "C" + str(startrow + i)
        tab.c3 = ret_val(sheet[sr].value)
# аналогично другие поля таблицы tab1000        
        i += 1
        tab.save()
        
 # Другие табличный части  налогично   
    os.remove(namefile)    

# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from django.db.models import Sum
from random import random
import openpyxl
from openpyxl.styles import Font

from medicament.oper_with_base import create_new_report, save_doc, get_name, get_period_namef, get_region_name, get_name_input
from medicament.models import Document,Doc_type, Hosp, Period, Role, Region, Comment, Doc_Hosp,Doc1,Doc2, Rows

from medicament.modelsDoc4 import Doc4, Doc4Tab1000, Doc4Tab2000, Doc4Tab3000, Doc4Tab4000, Doc4Tab5000, Doc4Tab5001, Doc4Tab6000, Doc4Tab7000

from _datetime import datetime


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
    ''' создатим табличные записи для нового отчета 
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
    '''
#    assert False
    aq0= doc.aggregate(Sum('c1_1_1'),Sum('c1_1_2'),Sum('c1_2'),Sum('c2_1'),Sum('c2_2'), Sum('c3_1'), \
                       Sum('c3_2_1'),Sum('c3_2_2'),Sum('c4_1'), \
         )
    
    s = [["1. Показатель 1_1_1", aq0['c1_1_1__sum']],
         ["2. Позазатель 1_1_2", aq0['c1_1_2__sum']],
         ]

    return s





def exp_to_excel_form4(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form4(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    if mode == 1:
        name_file = get_name("/static/Form/Form4.xlsx")
    else:
        name_file = get_name("/static/Form/Form4_All.xlsx")

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


    

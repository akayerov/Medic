# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from django.db.models import Sum
from random import random
import openpyxl
from openpyxl.styles import Font

from medicament.oper_with_base import create_new_report, save_doc, get_name, get_period_namef, get_region_name
from medicament.models import Doc2
from _datetime import datetime


def create_report_form2(periodInt, datef):
    ''' Создание новых документов (в новом периоде)
        Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
        copy_fields_formX - функция начального заполнения
    '''
    return create_new_report(2,Doc2,periodInt,datef, copy_fields_form2)

def save_doc_form2(request, type, id_doc, mode_comment):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
        Установить собственый параментрв DOCx,set_fields_formx, is_valid_formx
    ''' 
    return save_doc(Doc2,set_fields_form2, is_valid_form2, request, type, id_doc, mode_comment)


def copy_fields_form2(ds, dd):
    ''' Копирование полей - указать все поля для копирования 
        Для каждой формы, 
        ВЫЗЫВАЕТСЯ ТОЛЬКО ДЛЯ ДОКУМЕНТОВ В СОСТОЯНИИ ЗАВЕШЕНО- незаполненные и несогласаованные документы такой обработке не подлежат!
    '''
    dd.c2_1 = ds.c2_1
    dd.c2_2 = ds.c2_2
    dd.c2_3 = ds.c2_3
    dd.c2_3_1 = ds.c2_3_1
    dd.c2_3_2 = ds.c2_3_2
    dd.c2_3_3 = ds.c2_3_3
    dd.c2_4 = ds.c2_4
    dd.c2_4_1 = ds.c2_4_1
    dd.c2_4_2 = ds.c2_4_2
    dd.c2_4_3 = ds.c2_4_3
    dd.c2_5 = ds.c2_5
    dd.c2_13_1 = ds.c2_13_1
    dd.c2_13_2 = ds.c2_13_2
    dd.c2_13_3 = ds.c2_13_3
    dd.c2_13_4 = ds.c2_13_4
    dd.c2_13_5 = ds.c2_13_5
    dd.c2_13_6 = ds.c2_13_6
    dd.c2_13_7 = ds.c2_13_7
    dd.c2_13_8 = ds.c2_13_8
    dd.c2_13_9 = ds.c2_13_9
    dd.c2_13_10= ds.c2_13_10
    dd.c2_13_11= ds.c2_13_11
    dd.c2_13_12= ds.c2_13_12
    dd.c2_13_13= ds.c2_13_13
    dd.c2_13_14= ds.c2_13_14
    dd.c2_13_15= ds.c2_13_15
    dd.c2_13_16= ds.c2_13_16
    dd.c2_13_17= ds.c2_13_17
    dd.c2_13_18= ds.c2_13_18
    dd.c2_13_19= ds.c2_13_19
    dd.c2_13_20= ds.c2_13_20
    dd.c2_13_21= ds.c2_13_21
    dd.c2_13_22= ds.c2_13_22
    dd.c2_13_23= ds.c2_13_23
    dd.c2_13_24= ds.c2_13_24
    dd.c2_13_25= ds.c2_13_25
    dd.c2_13_26= ds.c2_13_26
    dd.c2_13_27= ds.c2_13_27
    dd.c2_13_28= ds.c2_13_28
    dd.c2_13_29= ds.c2_13_29
    dd.c2_13_30= ds.c2_13_30
    dd.c2_13_31= ds.c2_13_31
    dd.c2_13_32= ds.c2_13_32
    dd.c2_13_33= ds.c2_13_33
    dd.c2_13_34= ds.c2_13_34
    dd.c2_13_35= ds.c2_13_35
    dd.c2_13_36= ds.c2_13_36
    dd.c2_13_37= ds.c2_13_37
    dd.c2_13_38= ds.c2_13_38
    dd.c2_13_39= ds.c2_13_39
    dd.c2_13_40= ds.c2_13_40
    dd.c2_13_41= ds.c2_13_41
    dd.c2_6   = ds.c2_6
    dd.c2_7   = ds.c2_7
    dd.c2_8   = ds.c2_8
    dd.c2_9   = ds.c2_9
    dd.c2_10  = ds.c2_10
    dd.c2_11  = ds.c2_11
    dd.c2_12  = ds.c2_12
    dd.c2_13  = ds.c2_13
    dd.c2_13_1  = ds.c2_13_1
    dd.c2_13_2  = ds.c2_13_2
    dd.c2_13_3  = ds.c2_13_3
    dd.c2_13_4  = ds.c2_13_4
    dd.c2_13_5  = ds.c2_13_5
    dd.c2_13_6  = ds.c2_13_6
    dd.c2_13_7  = ds.c2_13_7
    dd.c2_13_8  = ds.c2_13_8
    dd.c2_13_9  = ds.c2_13_9
    dd.c2_13_10 = ds.c2_13_10
    dd.c2_13_11 = ds.c2_13_11
    dd.c2_13_12 = ds.c2_13_12
    dd.c2_13_13 = ds.c2_13_13
    dd.c2_13_14 = ds.c2_13_14
    dd.c2_13_15 = ds.c2_13_15
    dd.c2_13_16 = ds.c2_13_16
    dd.c2_13_17 = ds.c2_13_17
    dd.c2_13_18 = ds.c2_13_18
    dd.c2_13_19 = ds.c2_13_19
    dd.c2_13_20 = ds.c2_13_20
    dd.c2_13_21 = ds.c2_13_21
    dd.c2_13_22 = ds.c2_13_22
    dd.c2_13_23 = ds.c2_13_23
    dd.c2_13_24 = ds.c2_13_24
    dd.c2_13_25 = ds.c2_13_25
    dd.c2_13_26 = ds.c2_13_26
    dd.c2_13_27 = ds.c2_13_27
    dd.c2_13_28 = ds.c2_13_28
    dd.c2_13_29 = ds.c2_13_29
    dd.c2_13_30 = ds.c2_13_30
    dd.c2_13_31 = ds.c2_13_31
    dd.c2_13_32 = ds.c2_13_32
    dd.c2_13_33 = ds.c2_13_33
    dd.c2_13_34 = ds.c2_13_34
    dd.c2_13_35 = ds.c2_13_35
    dd.c2_13_36 = ds.c2_13_36
    dd.c2_13_37 = ds.c2_13_37
    dd.c2_13_38 = ds.c2_13_38
    dd.c2_13_39 = ds.c2_13_39
    dd.c2_13_40 = ds.c2_13_40
    dd.c2_13_41 = ds.c2_13_41
    dd.c2_13_42 = ds.c2_13_42
    dd.c2_13_43 = ds.c2_13_43
    dd.c2_13_44 = ds.c2_13_44
    dd.c2_13_45 = ds.c2_13_45
    dd.c2_13_46 = ds.c2_13_46
    dd.c2_13_47 = ds.c2_13_47
    dd.c2_13_48 = ds.c2_13_48
    dd.c2_13_49 = ds.c2_13_49
    dd.c2_13_50 = ds.c2_13_50
    dd.c2_13_51 = ds.c2_13_51
    dd.c2_13_52 = ds.c2_13_52
    dd.c2_13_53 = ds.c2_13_53
    dd.c2_13_54 = ds.c2_13_54
    dd.c2_13_55 = ds.c2_13_55
    dd.c2_13_56 = ds.c2_13_56
    dd.c2_13_57 = ds.c2_13_57
    dd.c2_13_58 = ds.c2_13_58
    dd.c2_13_59 = ds.c2_13_59
    dd.c2_13_60 = ds.c2_13_60
    dd.c2_13_61 = ds.c2_13_61
    dd.c2_13_62 = ds.c2_13_62
    dd.c2_13_63 = ds.c2_13_63
    dd.c2_13_64 = ds.c2_13_64
    dd.c2_13_65 = ds.c2_13_65
    dd.c2_13_66 = ds.c2_13_66
    dd.c2_13_67 = ds.c2_13_67
    dd.c2_13_68 = ds.c2_13_68
    dd.c2_13_69 = ds.c2_13_69
    dd.c2_13_70 = ds.c2_13_70
    dd.c2_13_71 = ds.c2_13_71
    dd.c2_13_72 = ds.c2_13_72
    dd.c2_13_73 = ds.c2_13_73
    dd.c2_13_74 = ds.c2_13_74
    dd.c2_13_75 = ds.c2_13_75
    dd.c2_13_76 = ds.c2_13_76
    dd.c2_13_77 = ds.c2_13_77
    dd.c2_13_78 = ds.c2_13_78
    dd.c2_13_79 = ds.c2_13_79
    dd.c2_13_80 = ds.c2_13_80
    dd.c2_13_81 = ds.c2_13_81
    dd.c2_13_82 = ds.c2_13_82
    dd.c2_13_83 = ds.c2_13_83
    dd.c2_13_84 = ds.c2_13_84
    dd.c2_13_85 = ds.c2_13_85
    dd.c2_13_86 = ds.c2_13_86
    dd.c2_13_87 = ds.c2_13_87
    dd.c2_13_88 = ds.c2_13_88
    dd.c2_13_89 = ds.c2_13_89
    dd.c2_13_90 = ds.c2_13_90
    dd.c2_13_91 = ds.c2_13_91
    dd.c2_13_92 = ds.c2_13_92
    dd.c2_13_93 = ds.c2_13_93
    dd.c2_13_94 = ds.c2_13_94
    dd.c2_13_95 = ds.c2_13_95
    dd.c2_13_96 = ds.c2_13_96
    dd.c2_13_97 = ds.c2_13_97
    dd.c2_13_98 = ds.c2_13_98
    dd.c2_13_99 = ds.c2_13_99
    dd.c2_13_100= ds.c2_13_100
    dd.c2_13_101= ds.c2_13_101
    dd.c2_13_102= ds.c2_13_102
    dd.c2_13_103= ds.c2_13_103
    dd.c2_13_104= ds.c2_13_104
    dd.c2_13_105= ds.c2_13_105
    dd.c2_13_106= ds.c2_13_106
    dd.c2_13_107= ds.c2_13_107
    dd.c2_13_108= ds.c2_13_108
    dd.c2_13_109= ds.c2_13_109
    dd.c2_13_110= ds.c2_13_110
    dd.c2_13_111= ds.c2_13_111
    dd.c2_13_112= ds.c2_13_112
    dd.c2_13_113= ds.c2_13_113
    dd.c2_13_114= ds.c2_13_114
    dd.c2_13_115= ds.c2_13_115
    dd.c2_13_116= ds.c2_13_116
    dd.c2_13_117= ds.c2_13_117
    dd.c2_13_118= ds.c2_13_118
    dd.c2_13_119= ds.c2_13_119
    dd.c2_13_120= ds.c2_13_120
    dd.c2_13_121= ds.c2_13_121
    dd.c2_13_122= ds.c2_13_122
    dd.c2_13_123= ds.c2_13_123
    dd.c2_13_124= ds.c2_13_124
    dd.c2_14= ds.c2_14
    dd.c2_14_1  = ds.c2_14_1
    dd.c2_14_2  = ds.c2_14_2
    dd.c2_14_3  = ds.c2_14_3
    dd.c2_14_4  = ds.c2_14_4
    dd.c2_14_5  = ds.c2_14_5
    dd.c2_14_6  = ds.c2_14_6
    dd.c2_14_7  = ds.c2_14_7
    dd.c2_14_8  = ds.c2_14_8
    dd.c2_14_9  = ds.c2_14_9
    dd.c2_14_10 = ds.c2_14_10
    dd.c2_14_11 = ds.c2_14_11
    dd.c2_14_12 = ds.c2_14_12
    dd.c2_14_13 = ds.c2_14_13
    dd.c2_14_14 = ds.c2_14_14
    dd.c2_14_15 = ds.c2_14_15
    dd.c2_14_16 = ds.c2_14_16
    dd.c2_14_17 = ds.c2_14_17
    dd.c2_14_18 = ds.c2_14_18
    dd.c2_14_19 = ds.c2_14_19
    dd.c2_14_20 = ds.c2_14_20
    dd.c2_14_21 = ds.c2_14_21
    dd.c2_14_22 = ds.c2_14_22
    dd.c2_14_23 = ds.c2_14_23
    dd.c2_14_24 = ds.c2_14_24
    dd.c2_14_25 = ds.c2_14_25
    dd.c2_14_26 = ds.c2_14_26
    dd.c2_14_27 = ds.c2_14_27
    dd.c2_14_28 = ds.c2_14_28
    dd.c2_14_29 = ds.c2_14_29
    dd.c2_14_30 = ds.c2_14_30
    dd.c2_14_31 = ds.c2_14_31
    dd.c2_14_32 = ds.c2_14_32
    dd.c2_14_33 = ds.c2_14_33
    dd.c2_14_34 = ds.c2_14_34
    dd.c2_14_35 = ds.c2_14_35
    dd.c2_14_36 = ds.c2_14_36
    dd.c2_14_37 = ds.c2_14_37
    dd.c2_14_38 = ds.c2_14_38
    dd.c2_14_39 = ds.c2_14_39
    dd.c2_14_40 = ds.c2_14_40
    dd.c2_14_41 = ds.c2_14_41
    dd.c2_14_42 = ds.c2_14_42
    dd.c2_14_43 = ds.c2_14_43
    dd.c2_14_44 = ds.c2_14_44
    dd.c2_14_45 = ds.c2_14_45
    dd.c2_15 = ds.c2_15
    dd.c2_16 = ds.c2_16
    dd.c2_17 = ds.c2_17
    dd.c2_18 = ds.c2_18
    dd.c2_19 = ds.c2_19
    dd.c2_20 = ds.c2_20
    dd.c2_21 = ds.c2_21
    dd.c2_22 = ds.c2_22
    dd.c2_23 = ds.c2_23
    dd.c2_24 = ds.c2_24
    dd.c2_25 = ds.c2_25
    dd.c2_26 = ds.c2_26
    dd.c2_27 = ds.c2_27
    dd.c2_28 = ds.c2_28
    dd.c3_1  = ds.c3_1
    dd.c3_2  = ds.c3_2
    dd.c3_3  = ds.c3_3
    dd.c3_4  = ds.c3_4
    dd.c3_5  = ds.c3_5
    dd.c3_6  = ds.c3_6
    dd.c3_7  = ds.c3_7
    dd.c3_8  = ds.c3_8
    dd.c3_9  = ds.c3_9
    dd.c3_10 = ds.c3_10
    dd.c3_11 = ds.c3_11
    dd.c3_12 = ds.c3_12
    dd.c3_13 = ds.c3_13
    dd.c3_14 = ds.c3_14
    dd.c3_15 = ds.c3_15
    dd.c3_16 = ds.c3_16
    dd.c3_17 = ds.c3_17
    dd.c3_18 = ds.c3_18
    dd.c3_19 = ds.c3_19
    dd.c3_20 = ds.c3_20
    dd.c3_21 = ds.c3_21
    dd.c3_22 = ds.c3_22
    dd.c3_23 = ds.c3_23
    dd.c3_24 = ds.c3_24
    dd.c3_25 = ds.c3_25
    dd.c3_26 = ds.c3_26
    dd.c3_27 = ds.c3_27
    dd.c3_28 = ds.c3_28
    dd.c3_29 = ds.c3_29
    dd.c3_30 = ds.c3_30
    dd.c3_31 = ds.c3_31
    dd.c3_32 = ds.c3_32
    dd.c3_33 = ds.c3_33
    dd.c3_34 = ds.c3_34
    dd.c3_35 = ds.c3_35
    dd.c3_36 = ds.c3_36
    dd.c3_37 = ds.c3_37
    dd.c3_38 = ds.c3_38
    dd.c4_1  = ds.c4_1
    dd.c4_2  = ds.c4_2
    dd.c4_3  = ds.c4_3
    dd.c4_4  = ds.c4_4
    dd.c4_5  = ds.c4_5
    dd.c4_6  = ds.c4_6
    dd.c4_7  = ds.c4_7
    dd.c4_8  = ds.c4_8
    dd.c4_9  = ds.c4_9
    dd.c4_10 = ds.c4_10
    dd.c4_11 = ds.c4_11
    dd.c4_12 = ds.c4_12
    dd.c4_13 = ds.c4_13
    dd.c4_14 = ds.c4_14
    dd.c4_15 = ds.c4_15
     

def set_fields_form2(request, doc):
    ''' Заполнение полей модели данными формы . 
        Для каждой формы
    '''
    doc.c2_1 = request.POST['c2_1'] 
    doc.c2_2 = request.POST['c2_2'] 
    doc.c2_3 = request.POST['c2_3'] 
    doc.c2_3_1 = request.POST['c2_3_1'] 
    doc.c2_3_2 = request.POST['c2_3_2'] 
    doc.c2_3_3 = request.POST['c2_3_3'] 
    doc.c2_4 = request.POST['c2_4'] 
    doc.c2_4_1 = request.POST['c2_4_1'] 
    doc.c2_4_2 = request.POST['c2_4_2'] 
    doc.c2_4_3 = request.POST['c2_4_3'] 
    doc.c2_5 = request.POST['c2_5'] 
    doc.c2_5_1 = request.POST['c2_5_1'] 
    doc.c2_5_2 = request.POST['c2_5_2'] 
    doc.c2_5_3 = request.POST['c2_5_3'] 
    doc.c2_5_4 = request.POST['c2_5_4'] 
    doc.c2_5_5 = request.POST['c2_5_5'] 
    doc.c2_5_6 = request.POST['c2_5_6'] 
    doc.c2_5_7 = request.POST['c2_5_7'] 
    doc.c2_5_8 = request.POST['c2_5_8'] 
    doc.c2_5_9 = request.POST['c2_5_9'] 
    doc.c2_5_10 = request.POST['c2_5_10'] 
    doc.c2_5_11 = request.POST['c2_5_11'] 
    doc.c2_5_12 = request.POST['c2_5_12'] 
    doc.c2_5_13 = request.POST['c2_5_13'] 
    doc.c2_5_14 = request.POST['c2_5_14'] 
    doc.c2_5_15 = request.POST['c2_5_15'] 
    doc.c2_5_16 = request.POST['c2_5_16'] 
    doc.c2_5_17 = request.POST['c2_5_17'] 
    doc.c2_5_18 = request.POST['c2_5_18'] 
    doc.c2_5_19 = request.POST['c2_5_19'] 
    doc.c2_5_20 = request.POST['c2_5_20'] 
    doc.c2_5_21 = request.POST['c2_5_21'] 
    doc.c2_5_22 = request.POST['c2_5_22'] 
    doc.c2_5_23 = request.POST['c2_5_23'] 
    doc.c2_5_24 = request.POST['c2_5_24'] 
    doc.c2_5_25 = request.POST['c2_5_25'] 
    doc.c2_5_26 = request.POST['c2_5_26'] 
    doc.c2_5_27 = request.POST['c2_5_27'] 
    doc.c2_5_28 = request.POST['c2_5_28'] 
    doc.c2_5_29 = request.POST['c2_5_29'] 
    doc.c2_5_30 = request.POST['c2_5_30'] 
    doc.c2_5_31 = request.POST['c2_5_31'] 
    doc.c2_5_32 = request.POST['c2_5_32'] 
    doc.c2_5_33 = request.POST['c2_5_33'] 
    doc.c2_5_34 = request.POST['c2_5_34'] 
    doc.c2_5_35 = request.POST['c2_5_35'] 
    doc.c2_5_36 = request.POST['c2_5_36'] 
    doc.c2_5_37 = request.POST['c2_5_37'] 
    doc.c2_5_38 = request.POST['c2_5_38'] 
    doc.c2_5_39 = request.POST['c2_5_39'] 
    doc.c2_5_40 = request.POST['c2_5_40'] 
    doc.c2_5_41 = request.POST['c2_5_41'] 
    doc.c2_6 = request.POST['c2_6'] 
    doc.c2_7 = request.POST['c2_7'] 
    doc.c2_8 = request.POST['c2_8'] 
    doc.c2_9 = request.POST['c2_9'] 
    doc.c2_10 = request.POST['c2_10'] 
    doc.c2_11 = request.POST['c2_11'] 
    doc.c2_12 = request.POST['c2_12'] 
    doc.c2_13 = request.POST['c2_13'] 
    doc.c2_13_1 = request.POST['c2_13_1'] 
    doc.c2_13_2 = request.POST['c2_13_2'] 
    doc.c2_13_3 = request.POST['c2_13_3'] 
    doc.c2_13_4 = request.POST['c2_13_4'] 
    doc.c2_13_5 = request.POST['c2_13_5'] 
    doc.c2_13_6 = request.POST['c2_13_6'] 
    doc.c2_13_7 = request.POST['c2_13_7'] 
    doc.c2_13_8 = request.POST['c2_13_8'] 
    doc.c2_13_9 = request.POST['c2_13_9'] 
    doc.c2_13_10 = request.POST['c2_13_10'] 
    doc.c2_13_11 = request.POST['c2_13_11'] 
    doc.c2_13_12 = request.POST['c2_13_12'] 
    doc.c2_13_13 = request.POST['c2_13_13'] 
    doc.c2_13_14 = request.POST['c2_13_14'] 
    doc.c2_13_15 = request.POST['c2_13_15'] 
    doc.c2_13_16 = request.POST['c2_13_16'] 
    doc.c2_13_17 = request.POST['c2_13_17'] 
    doc.c2_13_18 = request.POST['c2_13_18'] 
    doc.c2_13_19 = request.POST['c2_13_19'] 
    doc.c2_13_20 = request.POST['c2_13_20'] 
    doc.c2_13_21 = request.POST['c2_13_21'] 
    doc.c2_13_22 = request.POST['c2_13_22'] 
    doc.c2_13_23 = request.POST['c2_13_23'] 
    doc.c2_13_24 = request.POST['c2_13_24'] 
    doc.c2_13_25 = request.POST['c2_13_25'] 
    doc.c2_13_26 = request.POST['c2_13_26'] 
    doc.c2_13_27 = request.POST['c2_13_27'] 
    doc.c2_13_28 = request.POST['c2_13_28'] 
    doc.c2_13_29 = request.POST['c2_13_29'] 
    doc.c2_13_30 = request.POST['c2_13_30'] 
    doc.c2_13_31 = request.POST['c2_13_31'] 
    doc.c2_13_32 = request.POST['c2_13_32'] 
    doc.c2_13_33 = request.POST['c2_13_33'] 
    doc.c2_13_34 = request.POST['c2_13_34'] 
    doc.c2_13_35 = request.POST['c2_13_35'] 
    doc.c2_13_36 = request.POST['c2_13_36'] 
    doc.c2_13_37 = request.POST['c2_13_37'] 
    doc.c2_13_38 = request.POST['c2_13_38'] 
    doc.c2_13_39 = request.POST['c2_13_39'] 
    doc.c2_13_40 = request.POST['c2_13_40'] 
    doc.c2_13_41 = request.POST['c2_13_41'] 
    doc.c2_13_42 = request.POST['c2_13_42'] 
    doc.c2_13_43 = request.POST['c2_13_43'] 
    doc.c2_13_44 = request.POST['c2_13_44'] 
    doc.c2_13_45 = request.POST['c2_13_45'] 
    doc.c2_13_46 = request.POST['c2_13_46'] 
    doc.c2_13_47 = request.POST['c2_13_47'] 
    doc.c2_13_48 = request.POST['c2_13_48'] 
    doc.c2_13_49 = request.POST['c2_13_49'] 
    doc.c2_13_50 = request.POST['c2_13_50'] 
    doc.c2_13_51 = request.POST['c2_13_51'] 
    doc.c2_13_52 = request.POST['c2_13_52'] 
    doc.c2_13_53 = request.POST['c2_13_53'] 
    doc.c2_13_54 = request.POST['c2_13_54'] 
    doc.c2_13_55 = request.POST['c2_13_55'] 
    doc.c2_13_56 = request.POST['c2_13_56'] 
    doc.c2_13_57 = request.POST['c2_13_57'] 
    doc.c2_13_58 = request.POST['c2_13_58'] 
    doc.c2_13_59 = request.POST['c2_13_59'] 
    doc.c2_13_60 = request.POST['c2_13_60'] 
    doc.c2_13_61 = request.POST['c2_13_61'] 
    doc.c2_13_62 = request.POST['c2_13_62'] 
    doc.c2_13_63 = request.POST['c2_13_63'] 
    doc.c2_13_64 = request.POST['c2_13_64'] 
    doc.c2_13_65 = request.POST['c2_13_65'] 
    doc.c2_13_66 = request.POST['c2_13_66'] 
    doc.c2_13_67 = request.POST['c2_13_67'] 
    doc.c2_13_68 = request.POST['c2_13_68'] 
    doc.c2_13_69 = request.POST['c2_13_69'] 
    doc.c2_13_70 = request.POST['c2_13_70'] 
    doc.c2_13_71 = request.POST['c2_13_71'] 
    doc.c2_13_72 = request.POST['c2_13_72'] 
    doc.c2_13_73 = request.POST['c2_13_73'] 
    doc.c2_13_74 = request.POST['c2_13_74'] 
    doc.c2_13_75 = request.POST['c2_13_75'] 
    doc.c2_13_76 = request.POST['c2_13_76'] 
    doc.c2_13_77 = request.POST['c2_13_77'] 
    doc.c2_13_78 = request.POST['c2_13_78'] 
    doc.c2_13_79 = request.POST['c2_13_79'] 
    doc.c2_13_80 = request.POST['c2_13_80'] 
    doc.c2_13_81 = request.POST['c2_13_81'] 
    doc.c2_13_82 = request.POST['c2_13_82'] 
    doc.c2_13_83 = request.POST['c2_13_83'] 
    doc.c2_13_84 = request.POST['c2_13_84'] 
    doc.c2_13_85 = request.POST['c2_13_85'] 
    doc.c2_13_86 = request.POST['c2_13_86'] 
    doc.c2_13_87 = request.POST['c2_13_87'] 
    doc.c2_13_88 = request.POST['c2_13_88'] 
    doc.c2_13_89 = request.POST['c2_13_89'] 
    doc.c2_13_90 = request.POST['c2_13_90'] 
    doc.c2_13_91 = request.POST['c2_13_91'] 
    doc.c2_13_92 = request.POST['c2_13_92'] 
    doc.c2_13_93 = request.POST['c2_13_93'] 
    doc.c2_13_94 = request.POST['c2_13_94'] 
    doc.c2_13_95 = request.POST['c2_13_95'] 
    doc.c2_13_96 = request.POST['c2_13_96'] 
    doc.c2_13_97 = request.POST['c2_13_97'] 
    doc.c2_13_98 = request.POST['c2_13_98'] 
    doc.c2_13_99 = request.POST['c2_13_99'] 
    doc.c2_13_101 = request.POST['c2_13_101'] 
    doc.c2_13_102 = request.POST['c2_13_102'] 
    doc.c2_13_103 = request.POST['c2_13_103'] 
    doc.c2_13_104 = request.POST['c2_13_104'] 
    doc.c2_13_105 = request.POST['c2_13_105'] 
    doc.c2_13_106 = request.POST['c2_13_106'] 
    doc.c2_13_107 = request.POST['c2_13_107'] 
    doc.c2_13_108 = request.POST['c2_13_108'] 
    doc.c2_13_109 = request.POST['c2_13_109'] 
    doc.c2_13_110 = request.POST['c2_13_110'] 
    doc.c2_13_111 = request.POST['c2_13_111'] 
    doc.c2_13_112 = request.POST['c2_13_112'] 
    doc.c2_13_113 = request.POST['c2_13_113'] 
    doc.c2_13_114 = request.POST['c2_13_114'] 
    doc.c2_13_115 = request.POST['c2_13_115'] 
    doc.c2_13_116 = request.POST['c2_13_116'] 
    doc.c2_13_117 = request.POST['c2_13_117'] 
    doc.c2_13_118 = request.POST['c2_13_118'] 
    doc.c2_13_119 = request.POST['c2_13_119'] 
    doc.c2_13_120 = request.POST['c2_13_120'] 
    doc.c2_13_121 = request.POST['c2_13_121'] 
    doc.c2_13_122 = request.POST['c2_13_122'] 
    doc.c2_13_123 = request.POST['c2_13_123'] 
    doc.c2_13_124 = request.POST['c2_13_124'] 
    doc.c2_14 = request.POST['c2_14'] 
    doc.c2_14_1 = request.POST['c2_14_1'] 
    doc.c2_14_2 = request.POST['c2_14_2'] 
    doc.c2_14_3 = request.POST['c2_14_3'] 
    doc.c2_14_4 = request.POST['c2_14_4'] 
    doc.c2_14_5 = request.POST['c2_14_5'] 
    doc.c2_14_6 = request.POST['c2_14_6'] 
    doc.c2_14_7 = request.POST['c2_14_7'] 
    doc.c2_14_8 = request.POST['c2_14_8'] 
    doc.c2_14_9 = request.POST['c2_14_9'] 
    doc.c2_14_10 = request.POST['c2_14_10'] 
    doc.c2_14_11 = request.POST['c2_14_11'] 
    doc.c2_14_12 = request.POST['c2_14_12'] 
    doc.c2_14_14 = request.POST['c2_14_14'] 
    doc.c2_14_14 = request.POST['c2_14_14'] 
    doc.c2_14_15 = request.POST['c2_14_15'] 
    doc.c2_14_16 = request.POST['c2_14_16'] 
    doc.c2_14_17 = request.POST['c2_14_17'] 
    doc.c2_14_18 = request.POST['c2_14_18'] 
    doc.c2_14_19 = request.POST['c2_14_19'] 
    doc.c2_14_20 = request.POST['c2_14_20'] 
    doc.c2_14_21 = request.POST['c2_14_21'] 
    doc.c2_14_22 = request.POST['c2_14_22'] 
    doc.c2_14_23 = request.POST['c2_14_23'] 
    doc.c2_14_24 = request.POST['c2_14_24'] 
    doc.c2_14_25 = request.POST['c2_14_25'] 
    doc.c2_14_26 = request.POST['c2_14_26'] 
    doc.c2_14_27 = request.POST['c2_14_27'] 
    doc.c2_14_28 = request.POST['c2_14_28'] 
    doc.c2_14_29 = request.POST['c2_14_29'] 
    doc.c2_14_30 = request.POST['c2_14_30'] 
    doc.c2_14_31 = request.POST['c2_14_31'] 
    doc.c2_14_32 = request.POST['c2_14_32'] 
    doc.c2_14_33 = request.POST['c2_14_33'] 
    doc.c2_14_34 = request.POST['c2_14_34'] 
    doc.c2_14_35 = request.POST['c2_14_35'] 
    doc.c2_14_36 = request.POST['c2_14_36'] 
    doc.c2_14_37 = request.POST['c2_14_37'] 
    doc.c2_14_38 = request.POST['c2_14_38'] 
    doc.c2_14_39 = request.POST['c2_14_39'] 
    doc.c2_14_40 = request.POST['c2_14_40'] 
    doc.c2_14_41 = request.POST['c2_14_41'] 
    doc.c2_14_42 = request.POST['c2_14_42'] 
    doc.c2_14_43 = request.POST['c2_14_43'] 
    doc.c2_14_44 = request.POST['c2_14_44'] 
    doc.c2_14_45 = request.POST['c2_14_45'] 
    doc.c2_15 = request.POST['c2_15'] 
    doc.c2_16 = request.POST['c2_16'] 
    doc.c2_17 = request.POST['c2_17'] 
    doc.c2_18 = request.POST['c2_18'] 
    doc.c2_19 = request.POST['c2_19'] 
    doc.c2_20 = request.POST['c2_20'] 
    doc.c2_21 = request.POST['c2_21'] 
    doc.c2_22 = request.POST['c2_22'] 
    doc.c2_23 = request.POST['c2_23'] 
    doc.c2_24 = request.POST['c2_24'] 
    doc.c2_25 = request.POST['c2_25'] 
    doc.c2_26 = request.POST['c2_26'] 
    doc.c2_27 = request.POST['c2_27'] 
    doc.c2_28 = request.POST['c2_28'] 

    doc.c3_1 = request.POST['c3_1'] 
    doc.c3_2 = request.POST['c3_2'] 
    doc.c3_3 = request.POST['c3_3'] 
    doc.c3_4 = request.POST['c3_4'] 
    doc.c3_5 = request.POST['c3_5'] 
    doc.c3_6 = request.POST['c3_6'] 
    doc.c3_7 = request.POST['c3_7'] 
    doc.c3_8 = request.POST['c3_8'] 
    doc.c3_9 = request.POST['c3_9'] 
    doc.c3_10 = request.POST['c3_10'] 
    doc.c3_11 = request.POST['c3_11'] 
    doc.c3_12 = request.POST['c3_12'] 
    doc.c3_13 = request.POST['c3_13'] 
    doc.c3_14 = request.POST['c3_14'] 
    doc.c3_15 = request.POST['c3_15'] 
    doc.c3_16 = request.POST['c3_16'] 
    doc.c3_17 = request.POST['c3_17'] 
    doc.c3_18 = request.POST['c3_18'] 
    doc.c3_19 = request.POST['c3_19'] 
    doc.c3_20 = request.POST['c3_20'] 
    doc.c3_21 = request.POST['c3_21'] 
    doc.c3_22 = request.POST['c3_22'] 
    doc.c3_23 = request.POST['c3_23'] 
    doc.c3_24 = request.POST['c3_24'] 
    doc.c3_25 = request.POST['c3_25'] 
    doc.c3_26 = request.POST['c3_26'] 
    doc.c3_27 = request.POST['c3_27'] 
    doc.c3_28 = request.POST['c3_28'] 
    doc.c3_29 = request.POST['c3_29'] 
    doc.c3_30 = request.POST['c3_30'] 
    doc.c3_31 = request.POST['c3_31'] 
    doc.c3_32 = request.POST['c3_32'] 
    doc.c3_33 = request.POST['c3_33'] 
    doc.c3_34 = request.POST['c3_34'] 
    doc.c3_35 = request.POST['c3_35'] 
    doc.c3_36 = request.POST['c3_36'] 
    doc.c3_37 = request.POST['c3_37'] 
    doc.c3_38 = request.POST['c3_38'] 
    doc.c4_1 = request.POST['c4_1'] 
    doc.c4_2 = request.POST['c4_2'] 
    doc.c4_3 = request.POST['c4_3'] 
    doc.c4_4 = request.POST['c4_4'] 
    doc.c4_5 = request.POST['c4_5'] 
    doc.c4_6 = request.POST['c4_6'] 
    doc.c4_7 = request.POST['c4_7'] 
    doc.c4_8 = request.POST['c4_8'] 
    doc.c4_9 = request.POST['c4_9'] 
    doc.c4_10 = request.POST['c4_10'] 
    doc.c4_11 = request.POST['c4_11'] 
    doc.c4_12 = request.POST['c4_12'] 
    doc.c4_13 = request.POST['c4_13'] 
    doc.c4_14 = request.POST['c4_14'] 
    doc.c4_15 = request.POST['c4_15'] 
    


def is_valid_form2(doc, doc_prev):
    ''' Проверка заполнения формы на корректность 
        Специфично для каждой формы
    '''
    '''
    if int(doc.c1_1) < int(doc.c1_2) + int(doc.c1_3) + int(doc.c1_4) + int(doc.c1_5):
        ret = [False,'Итого по строке 1 меньше суммы по столбцам'] 
        return ret
    elif int(doc.c4_1) < int(doc.c4_2) + int(doc.c4_3) + int(doc.c4_4) + int(doc.c4_5) + int(doc.c4_6) + int(doc.c4_7) + int(doc.c4_8):
        ret = [False,'Итого по строке 3 меньше суммы по столбцам'] 
        return ret
    elif int(doc.c4_1) < int(doc.c4_2) + int(doc.c4_3) + int(doc.c4_4) + int(doc.c4_5) + int(doc.c4_6) + int(doc.c4_7) + int(doc.c4_8):
        ret = [False,'Итого по строке 4 меньше суммы по столбцам'] 
        return ret
    elif doc_prev and int(doc.c1_2) < int(doc_prev.c1_2):
        ret = [False,'Значение в строке 1 в предыдущщий период больше нынешнего'] 
        return ret
    else:
        ret = [True,'OK']
        return ret
    '''     
    ret = [True,'OK']
    return ret

def calc_sum_form2(doc):
    ''' Возвращает Суммы данных отчетов
    '''
    aq = doc.aggregate(Sum('c2_1'),Sum('c2_2'),Sum('c2_3'),Sum('c2_3_1'),Sum('c2_3_2'), Sum('c2_3_3'), \
                       Sum('c2_4'),Sum('c2_4_1'),Sum('c2_4_2'),Sum('c2_4_3'), \
         Sum('c2_5'), Sum('c2_5_1'),Sum('c2_5_2'),Sum('c2_5_3'),Sum('c2_5_4'),Sum('c2_5_5'),Sum('c2_5_6'),Sum('c2_5_7'),Sum('c2_5_8'),Sum('c2_5_9'), \
         Sum('c2_5_10'),Sum('c2_5_11'),Sum('c2_5_12'),Sum('c2_5_13'),Sum('c2_5_14'),Sum('c2_5_15'),Sum('c2_5_16'),Sum('c2_5_17'),Sum('c2_5_18'),Sum('c2_5_19'), \
         Sum('c2_5_20'),Sum('c2_5_21'),Sum('c2_5_22'),Sum('c2_5_23'),Sum('c2_5_24'),Sum('c2_5_25'),Sum('c2_5_26'),Sum('c2_5_27'),Sum('c2_5_28'),Sum('c2_5_29'), \
         Sum('c2_5_30'),Sum('c2_5_31'),Sum('c2_5_32'),Sum('c2_5_33'),Sum('c2_5_34'),Sum('c2_5_35'),Sum('c2_5_36'),Sum('c2_5_37'),Sum('c2_5_38'),Sum('c2_5_39'), \
         Sum('c2_5_40'),Sum('c2_5_41'), \
         Sum('c2_6'), Sum('c2_7'),Sum('c2_9'),Sum('c2_10'),Sum('c2_11'),Sum('c2_12'), \
         Sum('c2_13'), Sum('c2_13_1'),Sum('c2_13_2'),Sum('c2_13_3'),Sum('c2_13_4'),Sum('c2_13_5'),Sum('c2_13_6'),Sum('c2_13_7'),Sum('c2_13_8'),Sum('c2_13_9'), \
         Sum('c2_13_10'), Sum('c2_13_11'),Sum('c2_13_12'),Sum('c2_13_13'),Sum('c2_13_14'),Sum('c2_13_15'),Sum('c2_13_16'),Sum('c2_13_17'),Sum('c2_13_18'),Sum('c2_13_19'), \
         Sum('c2_13_20'), Sum('c2_13_21'),Sum('c2_13_22'),Sum('c2_13_23'),Sum('c2_13_24'),Sum('c2_13_25'),Sum('c2_13_26'),Sum('c2_13_27'),Sum('c2_13_28'),Sum('c2_13_29'), \
         Sum('c2_13_30'), Sum('c2_13_31'),Sum('c2_13_32'),Sum('c2_13_33'),Sum('c2_13_34'),Sum('c2_13_35'),Sum('c2_13_36'),Sum('c2_13_37'),Sum('c2_13_38'),Sum('c2_13_39'), \
         Sum('c2_13_40'), Sum('c2_13_41'),Sum('c2_13_42'),Sum('c2_13_43'),Sum('c2_13_44'),Sum('c2_13_45'),Sum('c2_13_46'),Sum('c2_13_47'),Sum('c2_13_48'),Sum('c2_13_49'), \
         Sum('c2_13_50'), Sum('c2_13_51'),Sum('c2_13_52'),Sum('c2_13_53'),Sum('c2_13_54'),Sum('c2_13_55'),Sum('c2_13_56'),Sum('c2_13_57'),Sum('c2_13_58'),Sum('c2_13_59'), \
         Sum('c2_13_60'), Sum('c2_13_61'),Sum('c2_13_62'),Sum('c2_13_63'),Sum('c2_13_64'),Sum('c2_13_65'),Sum('c2_13_66'),Sum('c2_13_67'),Sum('c2_13_68'),Sum('c2_13_69'), \
         Sum('c2_13_70'), Sum('c2_13_71'),Sum('c2_13_72'),Sum('c2_13_73'),Sum('c2_13_74'),Sum('c2_13_75'),Sum('c2_13_76'),Sum('c2_13_77'),Sum('c2_13_78'),Sum('c2_13_79'), \
         Sum('c2_13_80'), Sum('c2_13_81'),Sum('c2_13_82'),Sum('c2_13_83'),Sum('c2_13_84'),Sum('c2_13_85'),Sum('c2_13_86'),Sum('c2_13_87'),Sum('c2_13_88'),Sum('c2_13_89'), \
         Sum('c2_13_90'), Sum('c2_13_91'),Sum('c2_13_92'),Sum('c2_13_93'),Sum('c2_13_94'),Sum('c2_13_95'),Sum('c2_13_96'),Sum('c2_13_97'),Sum('c2_13_98'),Sum('c2_13_99'), \
         Sum('c2_13_100'), Sum('c2_13_101'),Sum('c2_13_102'),Sum('c2_13_103'),Sum('c2_13_104'),Sum('c2_13_105'),Sum('c2_13_106'),Sum('c2_13_107'),Sum('c2_13_108'),Sum('c2_13_109'), \
         Sum('c2_13_110'), Sum('c2_13_111'),Sum('c2_13_112'),Sum('c2_13_113'),Sum('c2_13_114'),Sum('c2_13_115'),Sum('c2_13_116'),Sum('c2_13_117'),Sum('c2_13_118'),Sum('c2_13_119'), \
         Sum('c2_13_120'), Sum('c2_13_121'),Sum('c2_13_122'),Sum('c2_13_123'),Sum('c2_13_124'), \
         Sum('c2_14'), Sum('c2_14_1'),Sum('c2_14_2'),Sum('c2_14_3'),Sum('c2_14_4'),Sum('c2_14_5'),Sum('c2_14_6'),Sum('c2_14_7'),Sum('c2_14_8'),Sum('c2_14_9'), \
         Sum('c2_14_10'), Sum('c2_14_11'),Sum('c2_14_12'),Sum('c2_14_13'),Sum('c2_14_14'),Sum('c2_14_15'),Sum('c2_14_16'),Sum('c2_14_17'),Sum('c2_14_18'),Sum('c2_14_19'), \
         Sum('c2_14_20'), Sum('c2_14_21'),Sum('c2_14_22'),Sum('c2_14_23'),Sum('c2_14_24'),Sum('c2_14_25'),Sum('c2_14_26'),Sum('c2_14_27'),Sum('c2_14_28'),Sum('c2_14_29'), \
         Sum('c2_14_30'), Sum('c2_14_31'),Sum('c2_14_32'),Sum('c2_14_33'),Sum('c2_14_34'),Sum('c2_14_35'),Sum('c2_14_36'),Sum('c2_14_37'),Sum('c2_14_38'),Sum('c2_14_39'), \
         Sum('c2_14_40'), Sum('c2_14_41'),Sum('c2_14_42'),Sum('c2_14_43'),Sum('c2_14_44'),Sum('c2_14_45'), \
         Sum('c2_15'),Sum('c2_16'),Sum('c2_18'),Sum('c2_19'),Sum('c2_20'),Sum('c2_21'),Sum('c2_22'),Sum('c2_23'), \
         Sum('c2_24'),Sum('c2_25'),Sum('c2_26'),Sum('c2_27'),Sum('c2_28'), \
         Sum('c3_1'),Sum('c3_2'),Sum('c3_3'),Sum('c3_4'),Sum('c3_5'),Sum('c3_6'),Sum('c3_7'),Sum('c3_8'),Sum('c3_9'), \
         Sum('c3_10'),Sum('c3_11'),Sum('c3_12'),Sum('c3_13'),Sum('c3_14'),Sum('c3_15'),Sum('c3_16'),Sum('c3_17'),Sum('c3_18'),Sum('c3_19'), \
         Sum('c3_20'),Sum('c3_21'),Sum('c3_22'),Sum('c3_23'),Sum('c3_24'),Sum('c3_25'),Sum('c3_26'),Sum('c3_27'),Sum('c3_28'),Sum('c3_29'), \
         Sum('c3_30'),Sum('c3_31'),Sum('c3_32'),Sum('c3_33'),Sum('c3_34'),Sum('c3_35'),Sum('c3_36'),Sum('c3_37'),Sum('c3_38'),\
         Sum('c4_1'),Sum('c4_2'),Sum('c4_3'),Sum('c4_4'),Sum('c4_5'),Sum('c4_6'),Sum('c4_7'),Sum('c4_8'),Sum('c4_9'), \
         Sum('c4_10'),Sum('c4_11'),Sum('c4_12'),Sum('c4_13'),Sum('c4_14'),Sum('c4_15') \
                      )
    
    s = [["Нозологии, рецептов",0],
         ["Федеральные:льготополучатели",0],
        ]
   
    s[0][1] = aq['c1_1__sum']
    s[0][2] = aq['c1_2__sum']
    s[0][3] = aq['c1_3__sum']
    s[0][4] = aq['c1_4__sum']
    s[0][5] = aq['c1_13__sum']

    s[1][6] = aq['c2_6__sum']
    s[1][7] = aq['c2_7__sum']
    s[1][8] = aq['c2_8__sum']
 
    s[2][1] = aq['c4_1__sum']
    s[2][2] = aq['c4_2__sum']
    s[2][3] = aq['c4_3__sum']
    s[2][4] = aq['c4_4__sum']
    s[2][5] = aq['c4_13__sum']
    s[2][6] = aq['c4_6__sum']
    s[2][7] = aq['c4_7__sum']
    s[2][8] = aq['c4_8__sum']
 
    s[3][1] = aq['c4_1__sum']
    s[3][2] = aq['c4_2__sum']
    s[3][3] = aq['c4_3__sum']
    s[3][4] = aq['c4_4__sum']
    s[3][5] = aq['c4_5__sum']
    s[3][6] = aq['c4_6__sum']
    s[3][7] = aq['c4_7__sum']
    s[3][8] = aq['c4_8__sum']
     
 
    return s

def exp_to_excel_form2(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form2(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    name_file = get_name("/medicament/Form/Form1.xlsx")

    wb = openpyxl.load_workbook(name_file)
    sheet = wb.active
    sheet['B2'] = speriod
    sheet['A1'] = sregion
    if mode==0:
        sheet['A20'] = "Статистика по отчету"  
        sheet['A21'] = "Организаций предоставляющих, Всего"
        sheet['B21'] = stat.rec_all
        sheet['A22'] = "Отобрано в отчет, Всего"
        sheet['B22'] = stat.rec_fltr
        sheet['A23'] = "Завершено"
        sheet['B23'] = stat.rec_complete
        sheet['A24'] = "Согласование"
        sheet['B24'] = stat.rec_soglas
        sheet['A25'] = "Корректировка"
        sheet['B25'] = stat.rec_correct
        sheet['A26'] = "Редактирование"
        sheet['B26'] = stat.rec_edit

    sheet['A28'] = "Выведено в системе Мед+ " + str(datetime.now()) 
    sheet['A28'].font = Font(size=5)

    
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


 #   name_file =  get_name("\\medicament\\Form\\rep" + str(int(random()*100000000)) + ".xlsx") 
    name_file =  get_name("/medicament/Form/rep" + str(int(random()*100000000)) + ".xlsx") 
    wb.save(name_file)
    
    return name_file


    

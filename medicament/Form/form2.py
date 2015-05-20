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
    doc.c2_13_100 = request.POST['c2_13_100'] 
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
    doc.c2_14_13 = request.POST['c2_14_13'] 
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

    doc.p3_1 = request.POST['p3_1'] 
    doc.p3_2 = request.POST['p3_2'] 
    doc.p3_3 = request.POST['p3_3'] 
    doc.p3_4 = request.POST['p3_4'] 
    doc.p3_5 = request.POST['p3_5'] 
    doc.p3_6 = request.POST['p3_6'] 
    doc.p3_7 = request.POST['p3_7'] 
    doc.p3_8 = request.POST['p3_8'] 
    doc.p3_9 = request.POST['p3_9'] 
    doc.p3_10 = request.POST['p3_10'] 
    doc.p3_11 = request.POST['p3_11'] 
    doc.p3_12 = request.POST['p3_12'] 
    doc.p3_13 = request.POST['p3_13'] 
    doc.p3_14 = request.POST['p3_14'] 
    doc.p3_15 = request.POST['p3_15'] 
    doc.p3_16 = request.POST['p3_16'] 
    doc.p3_17 = request.POST['p3_17'] 
    doc.p3_18 = request.POST['p3_18'] 
    doc.p3_19 = request.POST['p3_19'] 
    doc.p3_20 = request.POST['p3_20'] 
    doc.p3_21 = request.POST['p3_21'] 
    doc.p3_22 = request.POST['p3_22'] 
    doc.p3_23 = request.POST['p3_23'] 
    doc.p3_24 = request.POST['p3_24'] 
    doc.p3_25 = request.POST['p3_25'] 
    doc.p3_26 = request.POST['p3_26'] 
    doc.p3_27 = request.POST['p3_27'] 
    doc.p3_28 = request.POST['p3_28'] 
    doc.p3_29 = request.POST['p3_29'] 
    doc.p3_30 = request.POST['p3_30'] 
    doc.p3_31 = request.POST['p3_31'] 
    doc.p3_32 = request.POST['p3_32'] 
    doc.p3_33 = request.POST['p3_33'] 
    doc.p3_34 = request.POST['p3_34'] 
    doc.p3_35 = request.POST['p3_35'] 
    doc.p3_36 = request.POST['p3_36'] 
    doc.p3_37 = request.POST['p3_37'] 
    doc.p3_38 = request.POST['p3_38'] 
    


def is_valid_form2(doc, doc_prev):
    ''' Проверка заполнения формы на корректность 
    '''
    if int(doc.c2_3) != int(doc.c2_3_1) + int(doc.c2_3_2) + int(doc.c2_3_3):
        ret = [False,'Итого по строке 2.3 не равно сумме 2.3.1 - 2.3.3'] 
        return ret
    if int(doc.c2_4) != int(doc.c2_4_1) + int(doc.c2_4_2) + int(doc.c2_4_3):
        ret = [False,'Итого по строке 2.4 не равно сумме 2.4.1 - 2.4.3'] 
        return ret
    if int(doc.c2_13) != int(doc.c2_13_1) + int(doc.c2_13_2) + int(doc.c2_13_3) + int(doc.c2_13_4) + \
                         int(doc.c2_13_5) + int(doc.c2_13_6) + int(doc.c2_13_7) + int(doc.c2_13_8) + int(doc.c2_13_9) + \
                         int(doc.c2_13_10) + int(doc.c2_13_11) + int(doc.c2_13_12) + int(doc.c2_13_13) + int(doc.c2_13_14) + \
                         int(doc.c2_13_15) + int(doc.c2_13_16) + int(doc.c2_13_17) + int(doc.c2_13_18) + int(doc.c2_13_19) + \
                         int(doc.c2_13_20) + int(doc.c2_13_21) + int(doc.c2_13_22) + int(doc.c2_13_23) + int(doc.c2_13_24) + \
                         int(doc.c2_13_25) + int(doc.c2_13_26) + int(doc.c2_13_27) + int(doc.c2_13_28) + int(doc.c2_13_29) + \
                         int(doc.c2_13_30) + int(doc.c2_13_31) + int(doc.c2_13_32) + int(doc.c2_13_33) + int(doc.c2_13_34) + \
                        int(doc.c2_13_35) + int(doc.c2_13_36) + int(doc.c2_13_37) + int(doc.c2_13_38) + int(doc.c2_13_39) + \
                        int(doc.c2_13_40) + int(doc.c2_13_41) + int(doc.c2_13_42) + int(doc.c2_13_43) + int(doc.c2_13_44) + \
                        int(doc.c2_13_45) + int(doc.c2_13_46) + int(doc.c2_13_47) + int(doc.c2_13_48) + int(doc.c2_13_49) + \
                        int(doc.c2_13_50) + int(doc.c2_13_51) + int(doc.c2_13_52) + int(doc.c2_13_53) + int(doc.c2_13_54) + \
                        int(doc.c2_13_55) + int(doc.c2_13_56) + int(doc.c2_13_57) + int(doc.c2_13_58) + int(doc.c2_13_59) + \
                        int(doc.c2_13_60) + int(doc.c2_13_61) + int(doc.c2_13_62) + int(doc.c2_13_63) + int(doc.c2_13_64) + \
                        int(doc.c2_13_65) + int(doc.c2_13_66) + int(doc.c2_13_67) + int(doc.c2_13_68) + int(doc.c2_13_69) + \
                        int(doc.c2_13_70) + int(doc.c2_13_71) + int(doc.c2_13_72) + int(doc.c2_13_73) + int(doc.c2_13_74) + \
                        int(doc.c2_13_75) + int(doc.c2_13_76) + int(doc.c2_13_77) + int(doc.c2_13_78) + int(doc.c2_13_79) + \
                        int(doc.c2_13_80) + int(doc.c2_13_81) + int(doc.c2_13_82) + int(doc.c2_13_83) + int(doc.c2_13_84) + \
                        int(doc.c2_13_85) + int(doc.c2_13_86) + int(doc.c2_13_87) + int(doc.c2_13_88) + int(doc.c2_13_89) + \
                        int(doc.c2_13_90) + int(doc.c2_13_91) + int(doc.c2_13_92) + int(doc.c2_13_93) + int(doc.c2_13_94) + \
                        int(doc.c2_13_95) + int(doc.c2_13_96) + int(doc.c2_13_97) + int(doc.c2_13_98) + int(doc.c2_13_99) + \
                        int(doc.c2_13_100) + int(doc.c2_13_101) + int(doc.c2_13_102) + int(doc.c2_13_103) + int(doc.c2_13_104) + \
                        int(doc.c2_13_105) + int(doc.c2_13_106) + int(doc.c2_13_107) + int(doc.c2_13_108) + int(doc.c2_13_109) + \
                        int(doc.c2_13_110) + int(doc.c2_13_111) + int(doc.c2_13_112) + int(doc.c2_13_113) + int(doc.c2_13_114) + \
                        int(doc.c2_13_115) + int(doc.c2_13_116) + int(doc.c2_13_117) + int(doc.c2_13_118) + int(doc.c2_13_119) + \
                        int(doc.c2_13_120) + int(doc.c2_13_121) + int(doc.c2_13_122) + int(doc.c2_13_123) + int(doc.c2_13_124) :
        ret = [False,'Итого по строке 2.13 не равно сумме 2.13.1 - 2.13.124'] 
        return ret
    if int(doc.c2_14) != int(doc.c2_14_1) + int(doc.c2_14_2) + int(doc.c2_14_3) + int(doc.c2_14_4) + \
                         int(doc.c2_14_5) + int(doc.c2_14_6) + int(doc.c2_14_7) + int(doc.c2_14_8) + int(doc.c2_14_9) + \
                         int(doc.c2_14_10) + int(doc.c2_14_11) + int(doc.c2_14_12) + int(doc.c2_14_13) + int(doc.c2_14_14) + \
                         int(doc.c2_14_15) + int(doc.c2_14_16) + int(doc.c2_14_17) + int(doc.c2_14_18) + int(doc.c2_14_19) + \
                         int(doc.c2_14_20) + int(doc.c2_14_21) + int(doc.c2_14_22) + int(doc.c2_14_23) + int(doc.c2_14_24) + \
                         int(doc.c2_14_25) + int(doc.c2_14_26) + int(doc.c2_14_27) + int(doc.c2_14_28) + int(doc.c2_14_29) + \
                         int(doc.c2_14_30) + int(doc.c2_14_31) + int(doc.c2_14_32) + int(doc.c2_14_33) + int(doc.c2_14_34) + \
                        int(doc.c2_14_35) + int(doc.c2_14_36) + int(doc.c2_14_37) + int(doc.c2_14_38) + int(doc.c2_14_39) + \
                        int(doc.c2_14_40) + int(doc.c2_14_41) + int(doc.c2_14_42) + int(doc.c2_14_43) + int(doc.c2_14_44) + \
                        int(doc.c2_14_45):
        ret = [False,'Итого по строке 2.14 не равно сумме 2.14.1 - 2.14.45'] 
        return ret
    ret = [True,'OK']
    return ret

def calc_sum_form2(doc):
    ''' Возвращает Суммы данных отчетов
    '''
#    assert False
    aq0= doc.aggregate(Sum('c2_1'),Sum('c2_2'),Sum('c2_3'),Sum('c2_3_1'),Sum('c2_3_2'), Sum('c2_3_3'), \
                       Sum('c2_4'),Sum('c2_4_1'),Sum('c2_4_2'),Sum('c2_4_3'), \
         Sum('c2_5'), Sum('c2_5_1'),Sum('c2_5_2'),Sum('c2_5_3'),Sum('c2_5_4'),Sum('c2_5_5'),Sum('c2_5_6'),Sum('c2_5_7'),Sum('c2_5_8'),Sum('c2_5_9'), \
         Sum('c2_5_10'),Sum('c2_5_11'),Sum('c2_5_12'),Sum('c2_5_13'),Sum('c2_5_14'),Sum('c2_5_15'),Sum('c2_5_16'),Sum('c2_5_17'),Sum('c2_5_18'),Sum('c2_5_19'), \
         Sum('c2_5_20'),Sum('c2_5_21'),Sum('c2_5_22'),Sum('c2_5_23'),Sum('c2_5_24'),Sum('c2_5_25'),Sum('c2_5_26'),Sum('c2_5_27'),Sum('c2_5_28'),Sum('c2_5_29'), \
         Sum('c2_5_30'),Sum('c2_5_31'),Sum('c2_5_32'),Sum('c2_5_33'),Sum('c2_5_34'),Sum('c2_5_35'),Sum('c2_5_36'),Sum('c2_5_37'),Sum('c2_5_38'),Sum('c2_5_39'), \
         Sum('c2_5_40'),Sum('c2_5_41'), \
         Sum('c2_6'), Sum('c2_7'), Sum('c2_8'),Sum('c2_9'),Sum('c2_10'),Sum('c2_11'),Sum('c2_12'), \
         Sum('c2_13'), Sum('c2_13_1'),Sum('c2_13_2'),Sum('c2_13_3'),Sum('c2_13_4'),Sum('c2_13_5'),Sum('c2_13_6'),Sum('c2_13_7'),Sum('c2_13_8'),Sum('c2_13_9'), \
         Sum('c2_13_10'), Sum('c2_13_11'),Sum('c2_13_12'),Sum('c2_13_13'),Sum('c2_13_14'),Sum('c2_13_15'),Sum('c2_13_16'),Sum('c2_13_17'),Sum('c2_13_18'),Sum('c2_13_19'), \
         Sum('c2_13_20'), Sum('c2_13_21'),Sum('c2_13_22'),Sum('c2_13_23'),Sum('c2_13_24'),Sum('c2_13_25'),Sum('c2_13_26'),Sum('c2_13_27'),Sum('c2_13_28'),Sum('c2_13_29'), \
         Sum('c2_13_30'), Sum('c2_13_31'),Sum('c2_13_32'),Sum('c2_13_33'),Sum('c2_13_34'),Sum('c2_13_35'),Sum('c2_13_36'),Sum('c2_13_37'),Sum('c2_13_38'),Sum('c2_13_39'), \
         Sum('c2_13_40'), Sum('c2_13_41'),Sum('c2_13_42'),Sum('c2_13_43'),Sum('c2_13_44'),Sum('c2_13_45'),Sum('c2_13_46'),Sum('c2_13_47'),Sum('c2_13_48'),Sum('c2_13_49'), \
         Sum('c2_13_50'), Sum('c2_13_51'),Sum('c2_13_52'),Sum('c2_13_53'),Sum('c2_13_54'),Sum('c2_13_55'),Sum('c2_13_56'),Sum('c2_13_57'),Sum('c2_13_58'),Sum('c2_13_59'), \
         Sum('c2_13_60'), Sum('c2_13_61'),Sum('c2_13_62'),Sum('c2_13_63'),Sum('c2_13_64'),Sum('c2_13_65'),Sum('c2_13_66'),Sum('c2_13_67'),Sum('c2_13_68'),Sum('c2_13_69'), \
         Sum('c2_13_70'), Sum('c2_13_71'),Sum('c2_13_72'),Sum('c2_13_73'),Sum('c2_13_74'),Sum('c2_13_75'),Sum('c2_13_76'),Sum('c2_13_77'),Sum('c2_13_78'),Sum('c2_13_79'), \
         Sum('c2_13_80'), Sum('c2_13_81'),Sum('c2_13_82'),Sum('c2_13_83'),Sum('c2_13_84'),Sum('c2_13_85'),Sum('c2_13_86'),Sum('c2_13_87'),                Sum('c2_13_89'), \
         Sum('c2_13_90'), Sum('c2_13_91'),Sum('c2_13_92'),Sum('c2_13_93'),Sum('c2_13_94'),Sum('c2_13_95'),Sum('c2_13_96'),Sum('c2_13_97'),Sum('c2_13_98'),Sum('c2_13_99'), \
         Sum('c2_13_100'), Sum('c2_13_101'),Sum('c2_13_102'),Sum('c2_13_103'),Sum('c2_13_104'),Sum('c2_13_105'),Sum('c2_13_106'),Sum('c2_13_107'),Sum('c2_13_108'),Sum('c2_13_109'), \
         Sum('c2_13_110'), Sum('c2_13_111'),Sum('c2_13_112'),Sum('c2_13_113'),Sum('c2_13_114'),Sum('c2_13_115'),Sum('c2_13_116'),Sum('c2_13_117'),Sum('c2_13_118'),Sum('c2_13_119'), \
         Sum('c2_13_120'), Sum('c2_13_121'),Sum('c2_13_122'),Sum('c2_13_123'),Sum('c2_13_124'), \
         )
    aq1= doc.aggregate( Sum('c2_14'), Sum('c2_14_1'),Sum('c2_14_2'),Sum('c2_14_3'),Sum('c2_14_4'),Sum('c2_14_5'),Sum('c2_14_6'),Sum('c2_14_7'),Sum('c2_14_8'),Sum('c2_14_9'), \
         Sum('c2_14_10'), Sum('c2_14_11'),Sum('c2_14_12'),Sum('c2_14_13'),Sum('c2_14_14'),Sum('c2_14_15'),Sum('c2_14_16'),Sum('c2_14_17'),Sum('c2_14_18'),Sum('c2_14_19'), \
         Sum('c2_14_20'), Sum('c2_14_21'),Sum('c2_14_22'),Sum('c2_14_23'),Sum('c2_14_24'),Sum('c2_14_25'),Sum('c2_14_26'),Sum('c2_14_27'),Sum('c2_14_28'),Sum('c2_14_29'), \
         Sum('c2_14_30'), Sum('c2_14_31'),Sum('c2_14_32'),Sum('c2_14_33'),Sum('c2_14_34'),Sum('c2_14_35'),Sum('c2_14_36'),Sum('c2_14_37'),Sum('c2_14_38'),Sum('c2_14_39'), \
         Sum('c2_14_40'), Sum('c2_14_41'),Sum('c2_14_42'),Sum('c2_14_43'),Sum('c2_14_44'),Sum('c2_14_45'), \
         Sum('c2_15'),Sum('c2_16'),Sum('c2_17'),Sum('c2_18'),Sum('c2_19'),Sum('c2_20'),Sum('c2_21'),Sum('c2_22'),Sum('c2_23'), \
         Sum('c2_24'),Sum('c2_25'),Sum('c2_26'),Sum('c2_27'),Sum('c2_28'), \
         Sum('c3_1'),Sum('c3_2'),Sum('c3_3'),Sum('c3_4'),Sum('c3_5'),Sum('c3_6'),Sum('c3_7'),Sum('c3_8'),Sum('c3_9'), \
         Sum('c3_10'),Sum('c3_11'),Sum('c3_12'),Sum('c3_13'),Sum('c3_14'),Sum('c3_15'),Sum('c3_16'),Sum('c3_17'),Sum('c3_18'),Sum('c3_19'), \
         Sum('c3_20'),Sum('c3_21'),Sum('c3_22'),Sum('c3_23'),Sum('c3_24'),Sum('c3_25'),Sum('c3_26'),Sum('c3_27'),Sum('c3_28'),Sum('c3_29'), \
         Sum('c3_30'),Sum('c3_31'),Sum('c3_32'),Sum('c3_33'),Sum('c3_34'),Sum('c3_35'),Sum('c3_36'),Sum('c3_37'),Sum('c3_38'),\
         Sum('c4_1'),Sum('c4_2'),Sum('c4_3'),Sum('c4_4'),Sum('c4_5'),Sum('c4_6'),Sum('c4_7'),Sum('c4_8'),Sum('c4_9'), \
         Sum('c4_10'),Sum('c4_11'),Sum('c4_12'),Sum('c4_13'),Sum('c4_14'),Sum('c4_15') \
                      )
    
    s = [["2.1. Число врачей (без аспирантов, интернов и ординаторов), работающих в медицинских организациях субъекта Российской Федерации ", aq0['c2_1__sum']],
         ["2.2. Число среднего медицинского персонала, работающего в медицинских организациях субъекта Российской Федерации",aq0['c2_2__sum']],
         ["2.3. Число участковых врачей (без аспирантов, интернов и ординаторов), оказывающих медицинскую помощь сельскому населению (выбрать из справочника), всего",aq0['c2_3__sum']],
         ["2.3.1 Участковый врач терапевт",aq0['c2_3_1__sum']],
         ["2.3.2 Участковый врач педиатр",aq0['c2_3_2__sum']],
         ["2.3.3 Врач общей практики",aq0['c2_3_3__sum']],
         ["2.4. Число среднего медицинского персонала, оказывающего медицинскую помощь сельскому населению (выбрать из справочника), всего",aq0['c2_4__sum']],
         ["2.4.1 Участковая медицинская сестра врача терапевта",aq0['c2_4_1__sum']],
         ["2.4.2 Участковая медицинская сестра врача педиатра",aq0['c2_4_2__sum']],
         ["2.4.3 Участковая медицинская сестра врача общей практики",aq0['c2_4_3__sum']],
         ["2.5. Число врачей клинических специальностей (выбрать из списка), всего",aq0['c2_5__sum']],
         ["2.5.1 акушеры-гинекологи",aq0['c2_5_1__sum']],
         ["2.5.2 аллергологи-иммунологи",aq0['c2_5_2__sum']],
         ["2.5.3 гастроэнтерологи",aq0['c2_5_3__sum']],
         ["2.5.4 гематологи",aq0['c2_5_4__sum']],
         ["2.5.5 гериатры",aq0['c2_5_5__sum']],
         ["2.5.6 дерматовенерологи",aq0['c2_5_6__sum']],
         ["2.5.7 диабетологи",aq0['c2_5_7__sum']],
         ["2.5.8 инфекционисты",aq0['c2_5_8__sum']],
         ["2.5.9 кардиологи",aq0['c2_5_9__sum']],
         ["2.5.10 кардиологи детские",aq0['c2_5_10__sum']],
         ["2.5.11 колопроктологи",aq0['c2_5_11__sum']],
         ["2.5.12 неврологи",aq0['c2_5_12__sum']],
         ["2.5.13 нейрохирурги",aq0['c2_5_13__sum']],
         ["2.5.14 неонатологи",aq0['c2_5_14__sum']],
         ["2.5.15 нефрологи",aq0['c2_5_15__sum']],
         ["2.5.16 общей практики (семейные)",aq0['c2_5_16__sum']],
         ["2.5.17 онкологи",aq0['c2_5_17__sum']],
         ["2.5.18 онкологи детские",aq0['c2_5_18__sum']],
         ["2.5.19 оториноларингологи",aq0['c2_5_19__sum']],
         ["2.5.20 офтальмологи",aq0['c2_5_20__sum']],
         ["2.5.21 педиатры",aq0['c2_5_21__sum']],
         ["2.5.22 профпатологи",aq0['c2_5_22__sum']],
         ["2.5.23 no рентгенэндоваскулярным диагностике и лечению",aq0['c2_5_23__sum']],
         ["2.5.24 психиатры",aq0['c2_5_24__sum']],
         ["2.5.25 психиатры-наркологи",aq0['c2_5_25__sum']],        
         ["2.5.26 пульмонологи",aq0['c2_5_26__sum']],
         ["2.5.27 ревматологи",aq0['c2_5_27__sum']],
         ["2.5.28 скорой медицинской помощи",aq0['c2_5_28__sum']],
         ["2.5.29 терапевты",aq0['c2_5_29__sum']],
         ["2.5.30 травматология и ортопеды",aq0['c2_5_30__sum']],
         ["2.5.31 урологи",aq0['c2_5_31__sum']],
         ["2.5.32 урологи-андрологи детские",aq0['c2_5_32__sum']],
         ["2.5.33 фтизиатры",aq0['c2_5_33__sum']],
         ["2.5.34 хирурги",aq0['c2_5_34__sum']],
         ["2.5.35 хирурги детские",aq0['c2_5_35__sum']],
         ["2.5.36 хирурги пластические",aq0['c2_5_36__sum']],
         ["2.5.37 хирурги сердечно-сосудистые",aq0['c2_5_37__sum']],
         ["2.5.38 хирурги торакальные",aq0['c2_5_38__sum']],
         ["2.5.39 хирурги челюстно-лицевые",aq0['c2_5_39__sum']],
         ["2.5.40 эндокринологи",aq0['c2_5_40__sum']],
         ["2.5.41 эндокринологи детские",aq0['c2_5_41__sum']],         
         ["2.6. Число среднего медицинского персонала, работающих с  врачами клинических специальностей",aq0['c2_6__sum']],
         ["2.7. Число врачей, работающих в медицинских организациях, оказывающих медицинскую помощь в амбулаторных условиях",aq0['c2_7__sum']],
         ["2.8. Число занятых  врачебных должностей, оказывающих медицинскую помощь в амбулаторных условиях",aq0['c2_8__sum']],
         ["2.9. Число среднего медицинского персонала, работающих в медицинских организациях, оказывающих медицинскую помощь в амбулаторных условиях",aq0['c2_9__sum']],
         ["2.10. Число занятых  должностей  среднего медицинского персонала, оказывающих медицинскую помощь в амбулаторных условиях",aq0['c2_10__sum']],
         ["2.11. Число штатных должностей врачей, оказывающих медицинскую  помощь в амбулаторных условиях",aq0['c2_11__sum']],
         ["2.12. Число штатных должностей среднего медицинского персонала, оказывающих медицинскую помощь  в амбулаторных условиях",aq0['c2_12__sum']],
         ["2.13. Число  врачей дефицитных для субъекта Российской Федерации должностей на конец отчетного периода (выбрать из справочника), всего",aq0['c2_13__sum']],
         ["2.13.1 акушеры – гинекологи",aq0['c2_13_1__sum']],
         ["2.13.2 - их них акушеры – гинекологи цехового врачебного участка",aq0['c2_13_2__sum']],
         ["2.13.3 аллергологи – иммунологи",aq0['c2_13_3__sum']],
         ["2.13.4 анестезиологи – реаниматологи",aq0['c2_13_4__sum']],
         ["2.13.5 бактериологи",aq0['c2_13_5__sum']],
         ["2.13.6 вирусологи",aq0['c2_13_6__sum']],
         ["2.13.7 врачи здравпунктов",aq0['c2_13_7__sum']],
         ["2.13.8 гастроэнтерологи",aq0['c2_13_8__sum']],         
         ["2.13.9 гематологи",aq0['c2_13_9__sum']],
         ["2.13.10 генетики",aq0['c2_13_10__sum']],
         ["2.13.11 гериатры",aq0['c2_13_11__sum']],
         ["2.13.12 дезинфектологи",aq0['c2_13_12__sum']],
         ["2.13.13 дерматовенерологи",aq0['c2_13_13__sum']],
         ["2.13.14 диабетологи",aq0['c2_13_14__sum']],
         ["2.13.15 диетологи",aq0['c2_13_15__sum']],
         ["2.13.16 инфекционисты",aq0['c2_13_16__sum']],
         ["2.13.17 кардиологи",aq0['c2_13_17__sum']],
         ["2.13.18 кардиологи детские",aq0['c2_13_18__sum']],
         ["2.13.19 клинической лабораторной диагностики",aq0['c2_13_19__sum']],
         ["2.13.20 клинические микологи",aq0['c2_13_20__sum']],
         ["2.13.21 колопроктологи",aq0['c2_13_21__sum']],
         ["2.13.22 косметологи",aq0['c2_13_22__sum']],
         ["2.13.23 лаборанты",aq0['c2_13_23__sum']],
         ["2.13.24 лабораторные генетики",aq0['c2_13_24__sum']],       
         ["2.13.25 лабораторные микологи",aq0['c2_13_25__sum']],
         ["2.13.26 мануальной терапии",aq0['c2_13_26__sum']],
         ["2.13.27 методисты",aq0['c2_13_27__sum']],
         ["2.13.28 неврологи",aq0['c2_13_28__sum']],
         ["2.13.29 нейрохирурги",aq0['c2_13_29__sum']],
         ["2.13.30 неонатолог",aq0['c2_13_30__sum']],
         ["2.13.31 нефрологи",aq0['c2_13_31__sum']],
         ["2.13.32 общей практики (семейные)",aq0['c2_13_32__sum']],
         ["2.13.33 онкологи",aq0['c2_13_33__sum']],
         ["2.13.34 онкологи детские",aq0['c2_13_34__sum']],
         ["2.13.35 ортодонты",aq0['c2_13_35__sum']],
         ["2.13.36 остеопаты",aq0['c2_13_36__sum']],
         ["2.13.37 оториноларингологи",aq0['c2_13_37__sum']],
         ["2.13.38 офтальмологи",aq0['c2_13_38__sum']],
         ["2.13.39 офтальмологи-протезисты",aq0['c2_13_39__sum']],
         ["2.13.40 паразитологи",aq0['c2_13_40__sum']],        
         ["2.13.41 патологоанатомы",aq0['c2_13_41__sum']],
         ["2.13.42 педиатры – всего",aq0['c2_13_42__sum']],
         ["2.13.43 - из них: педиатры участковые (включая педиатров участковых приписных участков)",aq0['c2_13_43__sum']],
         ["2.13.44 - педиатры городские (районные)",aq0['c2_13_44__sum']],
         ["2.13.45 по авиационной и космической медицине",aq0['c2_13_45__sum']],
         ["2.13.46 по водолазной медицине",aq0['c2_13_46__sum']],
         ["2.13.47 по гигиене детей и подростков",aq0['c2_13_47__sum']],
         ["2.13.48 по гигиене питания",aq0['c2_13_48__sum']],
         ["2.13.49 по гигиене труда",aq0['c2_13_49__sum']],
         ["2.13.50 по гигиеническому воспитанию",aq0['c2_13_50__sum']],
         ["2.13.51 по коммунальной гигиене",aq0['c2_13_51__sum']],
         ["2.13.52 по лечебной физкультуре",aq0['c2_13_52__sum']],
         ["2.13.53 по медико-социальной экспертизе",aq0['c2_13_53__sum']],
         ["2.13.54 по медицинской профилактике",aq0['c2_13_54__sum']],
         ["2.13.55 по медицинской реабилитации",aq0['c2_13_55__sum']],
         ["2.13.56 по общей гигиене",aq0['c2_13_56__sum']],        
         ["2.13.57 по паллиативной медицинской помощи",aq0['c2_13_57__sum']],
         ["2.13.58 по радиационной гигиене",aq0['c2_13_58__sum']],
         ["2.13.59 по рентгенэдоваскулярным диагностике и лечению",aq0['c2_13_59__sum']],
         ["2.13.60 по санитарно-гигиеническим лабораторным исследованиям",aq0['c2_13_60__sum']],
         ["2.13.61 по спортивной медицине",aq0['c2_13_61__sum']],
         ["2.13.62 приемного отделения",aq0['c2_13_62__sum']],
         ["2.13.63 профпатологи",aq0['c2_13_63__sum']],
         ["2.13.64 психиатры",aq0['c2_13_64__sum']],
         ["2.13.65 - из них: участковые",aq0['c2_13_65__sum']],
         ["2.13.66 - психиатры детские",aq0['c2_13_66__sum']],
         ["2.13.67 - из них психиатры детские участковые",aq0['c2_13_67__sum']],
         ["2.13.68 - психиатры подростковые",aq0['c2_13_68__sum']],
         ["2.13.69 - из них психиатры подростковые участковые",aq0['c2_13_69__sum']],
         ["2.13.70 - психиатры-наркологи",aq0['c2_13_70__sum']],
         ["2.13.71 - из них психиатры-наркологи участковые",aq0['c2_13_71__sum']],
         ["2.13.72 психотерапевты",aq0['c2_13_72__sum']],
         ["2.13.73 пульмонологи",aq0['c2_13_73__sum']],        
         ["2.13.74 радиологи",aq0['c2_13_74__sum']],
         ["2.13.75 радиотерапевты",aq0['c2_13_75__sum']],
         ["2.13.76 ревматологи",aq0['c2_13_76__sum']],
         ["2.13.77 рентгенологи",aq0['c2_13_77__sum']],
         ["2.13.78 рефлексотерапевты",aq0['c2_13_78__sum']],
         ["2.13.79 сексологи",aq0['c2_13_79__sum']],
         ["2.13.80 стажеры",aq0['c2_13_80__sum']],
         ["2.13.81 статистики",aq0['c2_13_81__sum']],
         ["2.13.82 стоматологи",aq0['c2_13_82__sum']],
         ["2.13.83 стоматологи детские",aq0['c2_13_83__sum']],
         ["2.13.84 стоматологи-ортопеды",aq0['c2_13_84__sum']],
         ["2.13.85 стоматологи-терапевты",aq0['c2_13_85__sum']],
         ["2.13.86 стоматологи-хирурги",aq0['c2_13_86__sum']],
         ["2.13.87 судебно-психиатрические эксперты",aq0['c2_13_87__sum']],
         ["2.13.89 судовые врачи",aq0['c2_13_89__sum']],
         ["2.13.90 сурдологи-оториноларингологи",aq0['c2_13_90__sum']],
         ["2.13.91 сурдологи-протезисты",aq0['c2_13_91__sum']],
         ["2.13.92 терапевты - всего",aq0['c2_13_92__sum']],
         ["2.13.93 - из них: терапевты участковые",aq0['c2_13_93__sum']],
         ["2.13.94 - терапевты участковые цеховых врачебных участков",aq0['c2_13_94__sum']],
         ["2.13.95 - терапевты амбулаторий",aq0['c2_13_95__sum']],
         ["2.13.96 - терапевты подростковые",aq0['c2_13_96__sum']],
         ["2.13.97 токсикологи",aq0['c2_13_97__sum']],
         ["2.13.98 травматологи - ортопеды",aq0['c2_13_98__sum']],
         ["2.13.99 трансфузиологи",aq0['c2_13_99__sum']],         
         ["2.13.100 ультразвуковой диагностики",aq0['c2_13_100__sum']],
         ["2.13.101 урологи",aq0['c2_13_101__sum']],
         ["2.13.102 урологи-андрологи детские",aq0['c2_13_102__sum']],
         ["2.13.103 фармакологи клинические",aq0['c2_13_103__sum']],
         ["2.13.104 физиотерапевты",aq0['c2_13_104__sum']],
         ["2.13.105 фтизиатры",aq0['c2_13_105__sum']],
         ["2.13.106 - из них: фтизиатры участковые",aq0['c2_13_106__sum']],
         ["2.13.107 функциональной диагностики",aq0['c2_13_107__sum']],
         ["2.13.108 хирурги",aq0['c2_13_108__sum']],         
         ["2.13.109 хирурги детские",aq0['c2_13_109__sum']],
         ["2.13.110 хирурги пластические",aq0['c2_13_110__sum']],
         ["2.13.111 хирурги сердечно-сосудистые",aq0['c2_13_111__sum']],
         ["2.13.112 хирурги торакальные",aq0['c2_13_112__sum']],
         ["2.13.113 хирурги челюстно-лицевые",aq0['c2_13_113__sum']],
         ["2.13.114 эндокринологи",aq0['c2_13_114__sum']],
         ["2.13.115 эндокринологи детские",aq0['c2_13_115__sum']],
         ["2.13.116 эндоскописты",aq0['c2_13_116__sum']],
         ["2.13.117 эпидемиологи",aq0['c2_13_117__sum']],         
         ["2.13.118 прочие",aq0['c2_13_118__sum']],
         ["2.13.119 Специалисты с высшим немедицинским образованием – всего:",aq0['c2_13_119__sum']],
         ["2.13.120 - из них специалисты: биологи",aq0['c2_13_120__sum']],
         ["2.13.121 - психологи медицинские",aq0['c2_13_121__sum']],
         ["2.13.122 - инструкторы-методисты по лечебной физкультуре",aq0['c2_13_122__sum']],
         ["2.13.123 - судебные эксперты",aq0['c2_13_123__sum']],
         ["2.13.124 - химики-эксперты",aq0['c2_13_124__sum']],
         ["2.14.Число среднего медицинского персонала дефицитных для субъекта Российской Федерации должностей на конец отчетного периода (выбрать из справочника), всего",aq1['c2_14__sum']],
         ["2.14.1 акушерки",aq1['c2_14_1__sum']],         
         ["2.14.2 гигиенисты стоматологические",aq1['c2_14_2__sum']],
         ["2.14.3 заведующие",aq1['c2_14_3__sum']],
         ["2.14.4 - из них: заведущие фельдшерско-акушерским пунктом",aq1['c2_14_4__sum']],
         ["2.14.5 зубные врачи",aq1['c2_14_5__sum']],
         ["2.14.6 зубные техники",aq1['c2_14_6__sum']],
         ["2.14.7 инструкторы-дезинфекторы",aq1['c2_14_7__sum']],
         ["2.14.8 инструкторы по гигиеническому воспитанию",aq1['c2_14_8__sum']],
         ["2.14.9 инструкторы по лечебной физкультуре",aq1['c2_14_9__sum']],
         ["2.14.10 инструкторы по трудовой терапии",aq1['c2_14_10__sum']],         
         ["2.14.11 лаборанты",aq1['c2_14_11__sum']],
         ["2.14.12 медицинские лабораторные техники (фельдшеры-лаборанты)",aq1['c2_14_12__sum']],
         ["2.14.13 медицинские сестры",aq1['c2_14_13__sum']],
         ["2.14.14 - анестезисты",aq1['c2_14_14__sum']],
         ["2.14.15 - врачей общей практики (семейных врачей)",aq1['c2_14_15__sum']],
         ["2.14.16 - диетические",aq1['c2_14_16__sum']],
         ["2.14.17 - медико-социальной помощи",aq1['c2_14_17__sum']],
         ["2.14.18 - медицинская сестра (фельдшер) по приему вызовов скорой медицинской помощи и передаче их выездным бригадам скорой медицинской помощи",aq1['c2_14_18__sum']],
         ["2.14.19 - операционные",aq1['c2_14_19__sum']],         
         ["2.14.20 - палатные (постовые)",aq1['c2_14_20__sum']],
         ["2.14.21 - патронажные",aq1['c2_14_21__sum']],
         ["2.14.22 - перевязочной",aq1['c2_14_22__sum']],
         ["2.14.23 - по косметологии",aq1['c2_14_23__sum']],
         ["2.14.24 - по массажу",aq1['c2_14_24__sum']],
         ["2.14.25 - приемного отделения",aq1['c2_14_25__sum']],
         ["2.14.26 - процедурной",aq1['c2_14_26__sum']],
         ["2.14.27 - по реабилитации",aq1['c2_14_27__sum']],
         ["2.14.28 - старшие",aq1['c2_14_28__sum']],         
         ["2.14.29 - стерилизационной",aq1['c2_14_29__sum']],
         ["2.14.30 - участковые врачей-терапевтов участковых",aq1['c2_14_30__sum']],
         ["2.14.31 - участковые врачей-педиатров участковых",aq1['c2_14_31__sum']],
         ["2.14.32 - по физиотерапии",aq1['c2_14_32__sum']],
         ["2.14.33 - по функциональной диагностике",aq1['c2_14_33__sum']],
         ["2.14.34 медицинские дезинфекторы",aq1['c2_14_34__sum']],
         ["2.14.35 медицинские оптики-оптометристы",aq1['c2_14_35__sum']],
         ["2.14.36 медицинские регистраторы",aq1['c2_14_36__sum']],
         ["2.14.37 медицинские статистики",aq1['c2_14_37__sum']],         
         ["2.14.38 медицинские технологи",aq1['c2_14_38__sum']],
         ["2.14.39 помощники врачей",aq1['c2_14_39__sum']],
         ["2.14.40 рентгенолаборанты",aq1['c2_14_40__sum']],
         ["2.14.41 фельдшеры",aq1['c2_14_41__sum']],         
         ["2.14.42 - из них: фельдшеры скорой медицинской помощи",aq1['c2_14_42__sum']],
         ["2.14.43 - фельдшеры-наркологи",aq1['c2_14_43__sum']],
         ["2.14.44 - фельдшеры-водители скорой медицинской помощи",aq1['c2_14_44__sum']],
         ["2.14.45 прочий средний медицинский персонал",aq1['c2_14_45__sum']],
         ["2.15.Число участковых врачей терапевтов, работающих в медицинских организациях субъекта Российской Федерации",aq1['c2_15__sum']],
         ["2.16.Число участковых врачей педиатров, работающих в медицинских организациях субъекта Российской Федерации",aq1['c2_16__sum']],
         ["2.17.Число врачей общей практики (семейных врачей), работающих в медицинских организациях субъекта Российской Федерации",aq1['c2_17__sum']],
         ["2.18.Число участковых медицинских сестер участкового врача терапевта",aq1['c2_18__sum']],
         ["2.19.Число участковых медицинских сестер участкового врача педиатра",aq1['c2_19__sum']],         
         ["2.20.Число участковых медицинских сестер врача общей практики (семейного врача)",aq1['c2_20__sum']],
         ["2.21.Число штатных должностей участковых врачей терапевтов",aq1['c2_21__sum']],
         ["2.22.Число штатных должностей участковых врачей педиатров",aq1['c2_22__sum']],
         ["2.23.Число штатных должностей врачей общей практики (семейного врача)",aq1['c2_23__sum']],         
         ["2.24.Число штатных должностей участковых медицинских сестер участкового врача терапевта",aq1['c2_24__sum']],
         ["2.25.Число штатных должностей участковых медицинских сестер участкового врача педиатра",aq1['c2_25__sum']],
         ["2.26.Число штатных должностей участковых медицинских сестер врача общей практики (семейного врача)",aq1['c2_26__sum']],
         ["2.27.Число врачей, привлеченных на работу в медицинские организации субъекта Российской Федерации",aq1['c2_27__sum']],
         ["2.28.Число среднего медицинского персонала, привлеченного на работу в медицинские организации субъекта Российской Федерации",aq1['c2_28__sum']],
         ["3.1 Число врачей, получивших жилье из нуждающихся в улучшении жилищных условий, всего, из них",aq1['c3_1__sum']],
         ["3.2 - по социальному найму",aq1['c3_2__sum']],
         ["3.3 - служебное жилье",aq1['c3_3__sum']],
         ["3.4 - предоставление общежития",aq1['c3_4__sum']],         
         ["3.5 Число врачей, приобретших жилье из нуждающихся в улучшении жилищных условий, всего, из них:",aq1['c3_5__sum']],
         ["3.6 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части стоимости приобретаемого (строящегося) жилья",aq1['c3_6__sum']],
         ["3.7 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части платежа по кредитному договору (договору займа)",aq1['c3_7__sum']],
         ["3.8 - на основе льготного кредитования",aq1['c3_8__sum']],         
         ["3.9 Число врачей, нуждающихся в улучшении жилищных условий",aq1['c3_9__sum']],
         ["3.10 Число врачей, обеспеченных жильем, из числа врачей, привлеченных в субъект Российской Федерации",aq1['c3_10__sum']],
         ["3.11 Число врачей, нуждающихся в улучшении жилищных условий из числа врачей, привлеченных в субъект Российской Федерации",aq1['c3_11__sum']],
         ["3.12 Число среднего медицинского персонала, получившего жилье из нуждающихся в улучшении жилищных условий, всего, из них:",aq1['c3_12__sum']],
         ["3.13 - по социальному найму",aq1['c3_13__sum']],
         ["3.14 - служебное жилье",aq1['c3_14__sum']],
         ["3.15 - предоставление места в общежитии",aq1['c3_15__sum']],
         ["3.16 Число среднего медицинского персонала, приобретшего жилье из нуждающихся в улучшении жилищных условий, всего, из них:",aq1['c3_16__sum']],
         ["3.17 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части стоимости приобретаемого (строящегося) жилья",aq1['c3_17__sum']],         
         ["3.18 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части платежа по кредитному договору (договору займа)",aq1['c3_18__sum']],
         ["3.19 - на основе льготного кредитования",aq1['c3_19__sum']],
         ["3.20 Число среднего медицинского персонала, нуждающихся в улучшении жилищных условий",aq1['c3_20__sum']],
         ["3.21 Число среднего медицинского персонала, обеспеченных жильем, из числа средних медицинских работников, привлеченных в субъект Российской Федерации",aq1['c3_21__sum']],         
         ["3.22 Число среднего медицинского персонала, нуждающихся в улучшении жилищных условий из числа средних медицинских работников, привлеченных в субъект Российской Федерации",aq1['c3_22__sum']],
         ["3.23 Число врачей, получивших безвозмездно земельный участок для строительства (покупки) жилья, всего",aq1['c3_23__sum']],
         ["3.24 - в том числе, привлеченных в субъект Российской Федерации",aq1['c3_24__sum']],
         ["3.25 Число среднего медицинского персонала, получивших безвозмездно земельный участок для строительства (покупки) жилья, всего",aq1['c3_25__sum']],
         ["3.26 - в том числе, привлеченных в субъект Российской Федерации",aq1['c3_26__sum']],
         ["3.27 Число врачей, получивших компенсацию расходов за аренду жилого помещения",aq1['c3_27__sum']],
         ["3.28 Число среднего медицинского персонала, получивших компенсацию расходов за аренду жилого помещения",aq1['c3_28__sum']],
         ["3.29 Число врачей, получивших единовременные денежные выплаты при заключении трудового договора («подъмные»), с указанием программ – Земский доктор, иные",aq1['c3_29__sum']],
         ["3.30 Число среднего медицинского персонала, получивших единовременные денежные выплаты при заключении трудового договора («подъмные»), с указанием программ – Земский доктор, иные",aq1['c3_30__sum']],         
         ["3.31 Число врачей, получивших ежемесячные денежные выплаты",aq1['c3_31__sum']],
         ["3.32 Число среднего медицинского персонала, получивших ежемесячные денежные выплаты",aq1['c3_32__sum']],
         ["3.33 Число студентов образовательных учреждений высшего профессионального образования, получивших доплаты к стипендиям",aq1['c3_33__sum']],
         ["3.34 Число студентов образовательных учреждений среднего профессионального образования, получивших доплаты к стипендиям",aq1['c3_34__sum']],         
         ["3.35 Число врачей, получивших компенсацию расходов на оплату жилищно-коммунальных услуг",aq1['c3_35__sum']],
         ["3.36 Число среднего медицинского персонала, получивших компенсацию расходов на оплату жилищно-коммунальных услуг",aq1['c3_36__sum']],
         ["3.37 Число врачей, которые воспользовались внеочередным предоставлением места в дошкольной образовательной организации",aq1['c3_37__sum']],
         ["3.38 Число среднего медицинского персонала, которые воспользовались внеочередным предоставлением места в дошкольной образовательной организации",aq1['c3_38__sum']],
         ["4.1 Число врачей, прошедших обучение по программам дополнительного профессионального образования (повышение квалификации)",aq1['c4_1__sum']],
         ["4.2 Число врачей, прошедших обучение по программам дополнительного профессионального образования (профессиональная переподготовка)",aq1['c4_2__sum']],
         ["4.3 Число врачей, направленных на целевую подготовку в интернатуре",aq1['c4_3__sum']],         
         ["4.4 Число врачей, направленных на целевую подготовку в ординатуре",aq1['c4_4__sum']],
         ["4.5 Число врачей, завершивших обучение в интернатуре, всего",aq1['c4_5__sum']],
         ["4.6 в том числе, завершивших обучение в целевой интернатуре",aq1['c4_6__sum']],
         ["4.7 Число врачей, завершивших обучение в ординатуре, всего",aq1['c4_7__sum']],         
         ["4.8 в том числе, завершивших обучение в целевой ординатуре",aq1['c4_8__sum']],
         ["4.9 Число выпускников, трудоустроившихся в медицинских организациях государственной и муниципальной систем здравоохранения субъекта Российской Федерации после завершения обучения в целевой интернатуре",aq1['c4_9__sum']],
         ["4.10 Число выпускников, трудоустроившихся в медицинских организациях государственной и муниципальной систем здравоохранения субъекта Российской Федерации после завершения обучения в целевой ординатуре",aq1['c4_10__sum']],
         ["4.11 Число среднего медицинского персонала, направленного на целевую подготовку по программам среднего профессионального образования (базовая и углубленная подготовка)",aq1['c4_11__sum']],
         ["4.12 Число специалистов со средним медицинским и фармацевтическим образованием, прошедших обучение по программам дополнительного образования в образовательных учреждениях среднего профессионального и дополнительного профессионального образования",aq1['c4_12__sum']],
         ["4.13 Число бюджетных мест в образовательных учреждениях среднего профессионального образования, подведомственных субъекту Российской Федерации",aq1['c4_13__sum']],
         ["4.14 Число внебюджетных мест в образовательных учреждениях среднего профессионального образования, подведомственных субъекту Российской Федерации",aq1['c4_14__sum']],
         ["4.15 Число среднего медицинского персонала, трудоустроившихся в медицинских организациях государственной и муниципальной систем здравоохранения после завершения целевой подготовки по программам среднего профессионального образования (базовая и углубленная подготовка)",aq1['c4_15__sum']],
         ]

    return s

def calc_valf3_form2(doc):
    ''' Возвращает значения в приложении 3.1 
    '''
    s = [["3.1 Число врачей, получивших жилье из нуждающихся в улучшении жилищных условий, всего, из них", doc[0].p3_1],
         ["3.2 - по социальному найму", doc[0].p3_2],
         ["3.3 - служебное жилье", doc[0].p3_3],
         ["3.4 - предоставление общежития", doc[0].p3_4],         
         ["3.5 Число врачей, приобретших жилье из нуждающихся в улучшении жилищных условий, всего, из них:", doc[0].p3_5],
         ["3.6 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части стоимости приобретаемого (строящегося) жилья", doc[0].p3_6],
         ["3.7 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части платежа по кредитному договору (договору займа)", doc[0].p3_7],
         ["3.8 - на основе льготного кредитования", doc[0].p3_8],         
         ["3.9 Число врачей, нуждающихся в улучшении жилищных условий", doc[0].p3_9],
         ["3.10 Число врачей, обеспеченных жильем, из числа врачей, привлеченных в субъект Российской Федерации", doc[0].p3_10],
         ["3.11 Число врачей, нуждающихся в улучшении жилищных условий из числа врачей, привлеченных в субъект Российской Федерации",doc[0].p3_11],
         ["3.12 Число среднего медицинского персонала, получившего жилье из нуждающихся в улучшении жилищных условий, всего, из них:",doc[0].p3_12],
         ["3.13 - по социальному найму",doc[0].p3_13],
         ["3.14 - служебное жилье",doc[0].p3_14],
         ["3.15 - предоставление места в общежитии",doc[0].p3_15],
         ["3.16 Число среднего медицинского персонала, приобретшего жилье из нуждающихся в улучшении жилищных условий, всего, из них:",doc[0].p3_16],
         ["3.17 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части стоимости приобретаемого (строящегося) жилья",doc[0].p3_17],         
         ["3.18 - с использованием безвозмездной единовременной субсидии (выплаты) на компенсацию части платежа по кредитному договору (договору займа)",doc[0].p3_18],
         ["3.19 - на основе льготного кредитования",doc[0].p3_19],
         ["3.20 Число среднего медицинского персонала, нуждающихся в улучшении жилищных условий",doc[0].p3_20],
         ["3.21 Число среднего медицинского персонала, обеспеченных жильем, из числа средних медицинских работников, привлеченных в субъект Российской Федерации",doc[0].p3_21],         
         ["3.22 Число среднего медицинского персонала, нуждающихся в улучшении жилищных условий из числа средних медицинских работников, привлеченных в субъект Российской Федерации",doc[0].p3_22],
         ["3.23 Число врачей, получивших безвозмездно земельный участок для строительства (покупки) жилья, всего",doc[0].p3_23],
         ["3.24 - в том числе, привлеченных в субъект Российской Федерации",doc[0].p3_24],
         ["3.25 Число среднего медицинского персонала, получивших безвозмездно земельный участок для строительства (покупки) жилья, всего",doc[0].p3_25],
         ["3.26 - в том числе, привлеченных в субъект Российской Федерации",doc[0].p3_26],
         ["3.27 Число врачей, получивших компенсацию расходов за аренду жилого помещения",doc[0].p3_27],
         ["3.28 Число среднего медицинского персонала, получивших компенсацию расходов за аренду жилого помещения",doc[0].p3_28],
         ["3.29 Число врачей, получивших единовременные денежные выплаты при заключении трудового договора («подъмные»), с указанием программ – Земский доктор, иные",doc[0].p3_29],
         ["3.30 Число среднего медицинского персонала, получивших единовременные денежные выплаты при заключении трудового договора («подъмные»), с указанием программ – Земский доктор, иные",doc[0].p3_30],         
         ["3.31 Число врачей, получивших ежемесячные денежные выплаты",doc[0].p3_31],
         ["3.32 Число среднего медицинского персонала, получивших ежемесячные денежные выплаты",doc[0].p3_32],
         ["3.33 Число студентов образовательных учреждений высшего профессионального образования, получивших доплаты к стипендиям",doc[0].p3_33],
         ["3.34 Число студентов образовательных учреждений среднего профессионального образования, получивших доплаты к стипендиям",doc[0].p3_34],         
         ["3.35 Число врачей, получивших компенсацию расходов на оплату жилищно-коммунальных услуг",doc[0].p3_35],
         ["3.36 Число среднего медицинского персонала, получивших компенсацию расходов на оплату жилищно-коммунальных услуг",doc[0].p3_36],
         ["3.37 Число врачей, которые воспользовались внеочередным предоставлением места в дошкольной образовательной организации",doc[0].p3_37],
         ["3.38 Число среднего медицинского персонала, которые воспользовались внеочередным предоставлением места в дошкольной образовательной организации",doc[0].p3_38]
         ]
 
    return s





def exp_to_excel_form2(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form2(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    if mode == 1:
        name_file = get_name("/static/Form/Form2.xlsx")
    else:
        name_file = get_name("/static/Form/Form2_All.xlsx")

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
        res = calc_valf3_form2(doc)
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

def load_from_excel_form2(doc_id, filename):
    d  =  Doc2.objects.get(pk=doc_id)
    name_file = ("C:\\MedPlus\\" + filename)

    wb = openpyxl.load_workbook(name_file)
    sheet = wb.active
    startrow = 7 
    for i in range(0,296):
        c = "C" + str(startrow + i)
        if   i==0:
            d.c2_1 = sheet[c].value
        elif i==1:
            d.c2_2 = sheet[c].value
        elif i==2:
            d.c2_3 = sheet[c].value
        elif i==3:
            d.c2_3_1 = sheet[c].value
        elif i==4:
            d.c2_3_2 = sheet[c].value
        elif i==5:
            d.c2_3_3 = sheet[c].value
        elif i==6:
            d.c2_4 = sheet[c].value
        elif i==7:
            d.c2_4_1 = sheet[c].value
        elif i==8:
            d.c2_4_2 = sheet[c].value
        elif i==9:
            d.c2_4_3 = sheet[c].value
        elif i==10:
            d.c2_5 = sheet[c].value
        elif i==11:
            d.c2_5_1 = sheet[c].value
        elif i==12:
            d.c2_5_2 = sheet[c].value
        elif i==13:
            d.c2_5_3 = sheet[c].value
        elif i==14:
            d.c2_5_4 = sheet[c].value
        elif i==15:
            d.c2_5_5 = sheet[c].value
        elif i==16:
            d.c2_5_6 = sheet[c].value
        elif i==17:
            d.c2_5_7 = sheet[c].value
        elif i==18:
            d.c2_5_8 = sheet[c].value
        elif i==19:
            d.c2_5_9 = sheet[c].value
        elif i==20:
            d.c2_5_10 = sheet[c].value
        elif i==21:
            d.c2_5_11 = sheet[c].value
        elif i==22:
            d.c2_5_12 = sheet[c].value
        elif i==23:
            d.c2_5_13 = sheet[c].value
        elif i==24:
            d.c2_5_14 = sheet[c].value
        elif i==25:
            d.c2_5_15 = sheet[c].value
        elif i==26:
            d.c2_5_16 = sheet[c].value
        elif i==27:
            d.c2_5_17 = sheet[c].value
        elif i==28:
            d.c2_5_18 = sheet[c].value
        elif i==29:
            d.c2_5_19 = sheet[c].value
        elif i==30:
            d.c2_5_20 = sheet[c].value
        elif i==31:
            d.c2_5_21 = sheet[c].value
        elif i==32:
            d.c2_5_22 = sheet[c].value
        elif i==33:
            d.c2_5_23 = sheet[c].value
        elif i==34:
            d.c2_5_24 = sheet[c].value
        elif i==35:
            d.c2_5_25 = sheet[c].value
        elif i==36:
            d.c2_5_26 = sheet[c].value
        elif i==37:
            d.c2_5_27 = sheet[c].value
        elif i==38:
            d.c2_5_28 = sheet[c].value
        elif i==39:
            d.c2_5_29 = sheet[c].value
        elif i==40:
            d.c2_5_30 = sheet[c].value
        elif i==41:
            d.c2_5_31 = sheet[c].value
        elif i==42:
            d.c2_5_32 = sheet[c].value
        elif i==43:
            d.c2_5_33 = sheet[c].value
        elif i==44:
            d.c2_5_34 = sheet[c].value
        elif i==45:
            d.c2_5_35 = sheet[c].value
        elif i==46:
            d.c2_5_36 = sheet[c].value
        elif i==47:
            d.c2_5_37 = sheet[c].value
        elif i==48:
            d.c2_5_38 = sheet[c].value
        elif i==49:
            d.c2_5_39 = sheet[c].value
        elif i==50:
            d.c2_5_40 = sheet[c].value
        elif i==51:
            d.c2_5_41 = sheet[c].value
        elif i==52:
            d.c2_6 = sheet[c].value
        elif i==53:
            d.c2_7 = sheet[c].value
        elif i==54:
            d.c2_8 = sheet[c].value
        elif i==55:
            d.c2_9 = sheet[c].value
        elif i==56:
            d.c2_10 = sheet[c].value
        elif i==57:
            d.c2_11 = sheet[c].value
        elif i==58:
            d.c2_12 = sheet[c].value
        elif i==59:
            d.c2_13 = sheet[c].value
        elif i==60:
            d.c2_13_1 = sheet[c].value
        elif i==61:
            d.c2_13_2 = sheet[c].value
        elif i==62:
            d.c2_13_3 = sheet[c].value
        elif i==63:
            d.c2_13_4 = sheet[c].value
        elif i==64:
            d.c2_13_5 = sheet[c].value
        elif i==65:
            d.c2_13_6 = sheet[c].value
        elif i==66:
            d.c2_13_7 = sheet[c].value
        elif i==67:
            d.c2_13_8 = sheet[c].value
        elif i==68:
            d.c2_13_9 = sheet[c].value
        elif i==69:
            d.c2_13_10 = sheet[c].value
        elif i==70:
            d.c2_13_11 = sheet[c].value
        elif i==71:
            d.c2_13_12 = sheet[c].value
        elif i==72:
            d.c2_13_13 = sheet[c].value
        elif i==73:
            d.c2_13_14 = sheet[c].value
        elif i==74:
            d.c2_13_15 = sheet[c].value
        elif i==75:
            d.c2_13_16 = sheet[c].value
        elif i==76:
            d.c2_13_17 = sheet[c].value
        elif i==77:
            d.c2_13_18 = sheet[c].value
        elif i==78:
            d.c2_13_19 = sheet[c].value
        elif i==79:
            d.c2_13_20 = sheet[c].value
        elif i==80:
            d.c2_13_21 = sheet[c].value
        elif i==81:
            d.c2_13_22 = sheet[c].value
        elif i==82:
            d.c2_13_23 = sheet[c].value  
        elif i==83:
            d.c2_13_24 = sheet[c].value
        elif i==84:
            d.c2_13_25 = sheet[c].value
        elif i==85:
            d.c2_13_26 = sheet[c].value
        elif i==86:
            d.c2_13_27 = sheet[c].value
        elif i==87:
            d.c2_13_28 = sheet[c].value
        elif i==88:
            d.c2_13_29 = sheet[c].value
        elif i==89:
            d.c2_13_30 = sheet[c].value
        elif i==90:
            d.c2_13_31 = sheet[c].value
        elif i==91:
            d.c2_13_32 = sheet[c].value
        elif i==92:
            d.c2_13_33 = sheet[c].value
        elif i==93:
            d.c2_13_34 = sheet[c].value
        elif i==94:
            d.c2_13_35 = sheet[c].value
        elif i==95:
            d.c2_13_36 = sheet[c].value
        elif i==96:
            d.c2_13_37 = sheet[c].value
        elif i==97:
            d.c2_13_38 = sheet[c].value
        elif i==98:
            d.c2_13_39 = sheet[c].value
        elif i==99:
            d.c2_13_40 = sheet[c].value
        elif i==100:
            d.c2_13_41 = sheet[c].value
        elif i==101:
            d.c2_13_42 = sheet[c].value
        elif i==102:
            d.c2_13_43 = sheet[c].value
        elif i==103:
            d.c2_13_44 = sheet[c].value
        elif i==104:
            d.c2_13_45 = sheet[c].value
        elif i==105:
            d.c2_13_46 = sheet[c].value
        elif i==106:
            d.c2_13_47 = sheet[c].value  
        elif i==107:
            d.c2_13_48 = sheet[c].value
        elif i==108:
            d.c2_13_49 = sheet[c].value
        elif i==109:
            d.c2_13_50 = sheet[c].value
        elif i==110:
            d.c2_13_51 = sheet[c].value
        elif i==111:
            d.c2_13_52 = sheet[c].value
        elif i==112:
            d.c2_13_53 = sheet[c].value
        elif i==113:
            d.c2_13_54 = sheet[c].value
        elif i==114:
            d.c2_13_55 = sheet[c].value
        elif i==115:
            d.c2_13_56 = sheet[c].value
        elif i==116:
            d.c2_13_57 = sheet[c].value
        elif i==117:
            d.c2_13_58 = sheet[c].value
        elif i==118:
            d.c2_13_59 = sheet[c].value
        elif i==119:
            d.c2_13_60 = sheet[c].value
        elif i==120:
            d.c2_13_61 = sheet[c].value
        elif i==121:
            d.c2_13_62 = sheet[c].value
        elif i==122:
            d.c2_13_63 = sheet[c].value
        elif i==123:
            d.c2_13_64 = sheet[c].value
        elif i==124:
            d.c2_13_65 = sheet[c].value
        elif i==125:
            d.c2_13_66 = sheet[c].value
        elif i==126:
            d.c2_13_67 = sheet[c].value
        elif i==127:
            d.c2_13_68 = sheet[c].value
        elif i==128:
            d.c2_13_69 = sheet[c].value
        elif i==129:
            d.c2_13_70 = sheet[c].value
        elif i==130:
            d.c2_13_71 = sheet[c].value  
        elif i==131:
            d.c2_13_72 = sheet[c].value
        elif i==132:
            d.c2_13_73 = sheet[c].value
        elif i==133:
            d.c2_13_74 = sheet[c].value
        elif i==134:
            d.c2_13_75 = sheet[c].value
        elif i==135:
            d.c2_13_76 = sheet[c].value
        elif i==136:
            d.c2_13_77 = sheet[c].value
        elif i==137:
            d.c2_13_78 = sheet[c].value
        elif i==138:
            d.c2_13_79 = sheet[c].value
        elif i==139:
            d.c2_13_80 = sheet[c].value
        elif i==140:
            d.c2_13_81 = sheet[c].value
        elif i==141:
            d.c2_13_82 = sheet[c].value
        elif i==142:
            d.c2_13_83 = sheet[c].value
        elif i==143:
            d.c2_13_84 = sheet[c].value
        elif i==144:
            d.c2_13_85 = sheet[c].value
        elif i==145:
            d.c2_13_86 = sheet[c].value
        elif i==146:
            d.c2_13_87 = sheet[c].value
        elif i==147:
            d.c2_13_88 = sheet[c].value
        elif i==147:
            d.c2_13_89 = sheet[c].value
        elif i==148:
            d.c2_13_90 = sheet[c].value
        elif i==149:
            d.c2_13_91 = sheet[c].value
        elif i==150:
            d.c2_13_92 = sheet[c].value
        elif i==151:
            d.c2_13_93 = sheet[c].value
        elif i==152:
            d.c2_13_94 = sheet[c].value
        elif i==153:
            d.c2_13_95 = sheet[c].value  
        elif i==154:
            d.c2_13_96 = sheet[c].value
        elif i==155:
            d.c2_13_97 = sheet[c].value
        elif i==156:
            d.c2_13_98 = sheet[c].value
        elif i==157:
            d.c2_13_99 = sheet[c].value
        elif i==158:
            d.c2_13_100 = sheet[c].value
        elif i==159:
            d.c2_13_101 = sheet[c].value
        elif i==160:
            d.c2_13_102= sheet[c].value
        elif i==161:
            d.c2_13_103 = sheet[c].value
        elif i==162:
            d.c2_13_104 = sheet[c].value
        elif i==163:
            d.c2_13_105 = sheet[c].value
        elif i==164:
            d.c2_13_106 = sheet[c].value
        elif i==165:
            d.c2_13_107 = sheet[c].value
        elif i==166:
            d.c2_13_108 = sheet[c].value
        elif i==167:
            d.c2_13_109 = sheet[c].value
        elif i==168:
            d.c2_13_110 = sheet[c].value
        elif i==169:
            d.c2_13_111 = sheet[c].value
        elif i==170:
            d.c2_13_112 = sheet[c].value
        elif i==171:
            d.c2_13_113 = sheet[c].value
        elif i==172:
            d.c2_13_114 = sheet[c].value
        elif i==173:
            d.c2_13_115 = sheet[c].value
        elif i==174:
            d.c2_13_116 = sheet[c].value
        elif i==175:
            d.c2_13_117 = sheet[c].value
        elif i==176:
            d.c2_13_118 = sheet[c].value
        elif i==177:
            d.c2_13_119 = sheet[c].value  
        elif i==178:
            d.c2_13_120 = sheet[c].value
        elif i==179:
            d.c2_13_121 = sheet[c].value
        elif i==180:
            d.c2_13_122 = sheet[c].value
        elif i==181:
            d.c2_13_123 = sheet[c].value
        elif i==182:
            d.c2_13_124 = sheet[c].value
        elif i==183:
            d.c2_14 = sheet[c].value
        elif i==184:
            d.c2_14_1 = sheet[c].value
        elif i==185:
            d.c2_14_2 = sheet[c].value
        elif i==186:
            d.c2_14_3 = sheet[c].value
        elif i==187:
            d.c2_14_4 = sheet[c].value
        elif i==188:
            d.c2_14_5 = sheet[c].value
        elif i==189:
            d.c2_14_6 = sheet[c].value
        elif i==190:
            d.c2_14_7 = sheet[c].value
        elif i==191:
            d.c2_14_8 = sheet[c].value
        elif i==192:
            d.c2_14_9 = sheet[c].value
        elif i==193:
            d.c2_14_10 = sheet[c].value
        elif i==194:
            d.c2_14_11 = sheet[c].value
        elif i==195:
            d.c2_14_12 = sheet[c].value
        elif i==196:
            d.c2_14_13 = sheet[c].value
        elif i==197:
            d.c2_14_14 = sheet[c].value
        elif i==198:
            d.c2_14_15 = sheet[c].value
        elif i==199:
            d.c2_14_16 = sheet[c].value
        elif i==200:
            d.c2_14_17 = sheet[c].value
        elif i==201:
            d.c2_14_18 = sheet[c].value  
        elif i==202:
            d.c2_14_19 = sheet[c].value
        elif i==203:
            d.c2_14_20 = sheet[c].value
        elif i==204:
            d.c2_14_21 = sheet[c].value
        elif i==205:
            d.c2_14_22 = sheet[c].value
        elif i==206:
            d.c2_14_23 = sheet[c].value
        elif i==207:
            d.c2_14_24 = sheet[c].value
        elif i==208:
            d.c2_14_25 = sheet[c].value
        elif i==209:
            d.c2_14_26 = sheet[c].value
        elif i==210:
            d.c2_14_27 = sheet[c].value
        elif i==211:
            d.c2_14_28 = sheet[c].value
        elif i==212:
            d.c2_14_29 = sheet[c].value
        elif i==213:
            d.c2_14_30 = sheet[c].value
        elif i==214:
            d.c2_14_31 = sheet[c].value
        elif i==215:
            d.c2_14_32 = sheet[c].value
        elif i==216:
            d.c2_14_33 = sheet[c].value
        elif i==217:
            d.c2_14_34 = sheet[c].value
        elif i==218:
            d.c2_14_35 = sheet[c].value
        elif i==219:
            d.c2_14_36 = sheet[c].value
        elif i==220:
            d.c2_14_37 = sheet[c].value
        elif i==221:
            d.c2_14_38 = sheet[c].value
        elif i==222:
            d.c2_14_39 = sheet[c].value
        elif i==223:
            d.c2_14_40 = sheet[c].value
        elif i==224:
            d.c2_14_41 = sheet[c].value
        elif i==225:
            d.c2_14_42 = sheet[c].value  
        elif i==226:
            d.c2_14_43 = sheet[c].value
        elif i==227:
            d.c2_14_44 = sheet[c].value
        elif i==228:
            d.c2_14_45 = sheet[c].value
        elif i==229:
            d.c2_15 = sheet[c].value
        elif i==230:
            d.c2_16 = sheet[c].value
        elif i==231:
            d.c2_17 = sheet[c].value
        elif i==232:
            d.c2_18 = sheet[c].value
        elif i==233:
            d.c2_19 = sheet[c].value
        elif i==234:
            d.c2_20 = sheet[c].value
        elif i==235:
            d.c2_21 = sheet[c].value
        elif i==236:
            d.c2_22 = sheet[c].value
        elif i==237:
            d.c2_23 = sheet[c].value
        elif i==238:
            d.c2_24 = sheet[c].value
        elif i==239:
            d.c2_25 = sheet[c].value
        elif i==240:
            d.c2_26 = sheet[c].value
        elif i==241:
            d.c2_27 = sheet[c].value
        elif i==242:
            d.c2_28 = sheet[c].value
        elif i==243:
            d.c3_1 = sheet[c].value
        elif i==244:
            d.c3_2 = sheet[c].value
        elif i==245:
            d.c3_3 = sheet[c].value
        elif i==246:
            d.c3_4 = sheet[c].value
        elif i==247:
            d.c3_5 = sheet[c].value
        elif i==248:
            d.c3_6 = sheet[c].value
        elif i==249:
            d.c3_7 = sheet[c].value  
        elif i==250:
            d.c3_8 = sheet[c].value
        elif i==251:
            d.c3_9 = sheet[c].value
        elif i==252:
            d.c3_10 = sheet[c].value
        elif i==253:
            d.c3_11 = sheet[c].value
        elif i==254:
            d.c3_12 = sheet[c].value
        elif i==255:
            d.c3_13 = sheet[c].value
        elif i==256:
            d.c3_14 = sheet[c].value
        elif i==257:
            d.c3_15 = sheet[c].value
        elif i==258:
            d.c3_16 = sheet[c].value
        elif i==259:
            d.c3_17 = sheet[c].value
        elif i==260:
            d.c3_18 = sheet[c].value
        elif i==261:
            d.c3_19 = sheet[c].value
        elif i==262:
            d.c3_20 = sheet[c].value
        elif i==263:
            d.c3_21 = sheet[c].value
        elif i==264:
            d.c3_22 = sheet[c].value
        elif i==265:
            d.c3_23 = sheet[c].value
        elif i==266:
            d.c3_24 = sheet[c].value
        elif i==267:
            d.c3_25 = sheet[c].value
        elif i==268:
            d.c3_26 = sheet[c].value
        elif i==269:
            d.c3_27 = sheet[c].value
        elif i==270:
            d.c3_28 = sheet[c].value
        elif i==271:
            d.c3_29 = sheet[c].value
        elif i==272:
            d.c3_30 = sheet[c].value
        elif i==273:
            d.c3_31 = sheet[c].value  
        elif i==274:
            d.c3_32 = sheet[c].value
        elif i==275:
            d.c3_33 = sheet[c].value
        elif i==276:
            d.c3_34 = sheet[c].value
        elif i==277:
            d.c3_35 = sheet[c].value
        elif i==278:
            d.c3_36 = sheet[c].value
        elif i==279:
            d.c3_37 = sheet[c].value
        elif i==280:
            d.c3_38 = sheet[c].value
        elif i==281:
            d.c4_1 = sheet[c].value
        elif i==282:
            d.c4_2 = sheet[c].value
        elif i==283:
            d.c4_3 = sheet[c].value
        elif i==284:
            d.c4_4 = sheet[c].value
        elif i==285:
            d.c4_5 = sheet[c].value
        elif i==286:
            d.c4_6 = sheet[c].value
        elif i==287:
            d.c4_7 = sheet[c].value
        elif i==288:
            d.c4_8 = sheet[c].value
        elif i==289:
            d.c4_9 = sheet[c].value
        elif i==290:
            d.c4_10 = sheet[c].value
        elif i==291:
            d.c4_11 = sheet[c].value
        elif i==292:
            d.c4_12 = sheet[c].value
        elif i==293:
            d.c4_13 = sheet[c].value
        elif i==294:
            d.c4_14 = sheet[c].value
        elif i==295:
            d.c4_15 = sheet[c].value

    startrow = 307 
    for i in range(0,38):
        c = "C" + str(startrow + i)
    for i in range(0,38):
        c = "C" + str(startrow + i)
        if   i==0:
            d.p3_1 = sheet[c].value
        if   i==1:
            d.p3_2 = sheet[c].value
        if   i==2:
            d.p3_3 = sheet[c].value
        if   i==3:
            d.p3_4 = sheet[c].value
        if   i==4:
            d.p3_5 = sheet[c].value
        if   i==5:
            d.p3_6 = sheet[c].value
        if   i==6:
            d.p3_7 = sheet[c].value
        if   i==7:
            d.p3_8 = sheet[c].value
        if   i==8:
            d.p3_9 = sheet[c].value
        if   i==9:
            d.p3_10 = sheet[c].value
        if   i==10:
            d.p3_11 = sheet[c].value
        if   i==11:
            d.p3_12 = sheet[c].value
        if   i==12:
            d.p3_13 = sheet[c].value
        if   i==13:
            d.p3_14 = sheet[c].value
        if   i==14:
            d.p3_15 = sheet[c].value
        if   i==15:
            d.p3_16 = sheet[c].value
        if   i==16:
            d.p3_17 = sheet[c].value
        if   i==17:
            d.p3_18 = sheet[c].value
        if   i==18:
            d.p3_19 = sheet[c].value
        if   i==19:
            d.p3_20 = sheet[c].value
        if   i==20:
            d.p3_21 = sheet[c].value
        if   i==21:
            d.p3_22 = sheet[c].value
        if   i==22:
            d.p3_23 = sheet[c].value
        if   i==23:
            d.p3_24 = sheet[c].value
        if   i==24:
            d.p3_25 = sheet[c].value
        if   i==25:
            d.p3_26 = sheet[c].value
        if   i==26:
            d.p3_27 = sheet[c].value
        if   i==27:
            d.p3_28 = sheet[c].value
        if   i==28:
            d.p3_29 = sheet[c].value
        if   i==29:
            d.p3_30 = sheet[c].value
        if   i==30:
            d.p3_31 = sheet[c].value
        if   i==31:
            d.p3_32 = sheet[c].value
        if   i==32:
            d.p3_33 = sheet[c].value
        if   i==33:
            d.p3_34 = sheet[c].value
        if   i==34:
            d.p3_35 = sheet[c].value
        if   i==35:
            d.p3_36 = sheet[c].value
        if   i==36:
            d.p3_37 = sheet[c].value
        if   i==37:
            d.p3_38 = sheet[c].value        
    d.save()    
    return

    

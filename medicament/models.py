# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

def get_file_path(self, file):
#    return ("pdf/datasheet/%s/%s/%s" % (file[0], file[1], file))
    return ("C:\\" + file)

# Create your models here.
class Doc_type(models.Model):
    ''' Тип документа свода
    '''
    name =  models.CharField('Наименование',max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Period(models.Model):
    name =  models.CharField('Наименование',max_length=100)
    dateb =  models.DateField()
    datee =  models.DateField()
    prev = models.ForeignKey('self', null=True, blank=True)      # ссылка на документ предудущего периода с которым сверяемся
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class Region(models.Model):
    ''' Регионы
    '''
    name = models.CharField('Регион',max_length=32)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)

class Hosp(models.Model):
    name =  models.CharField('Наименование Краткое',max_length=64)
    name_full =  models.CharField('Наименование Полное',max_length=255)
    region = models.ForeignKey(Region, null=True, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Doc_Hosp(models.Model):
    ''' назначение Документов для заполнения больницам
    '''
    hosp = models.ForeignKey(Hosp)
    doc_type =  models.ForeignKey(Doc_type)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.hosp) + "-" + str(self.doc_type )

class Role(models.Model):
    ''' Назначение ролей пользователей
    '''
    user = models.ForeignKey(User)
    hosp = models.ForeignKey(Hosp)
    tel = models.CharField('Телефон',max_length=20)
    EDIT = 'Р'
    CONTROL = 'К'
    
    STATE_IN_RIGHT = (
        (EDIT, 'Редактирование'),
        (CONTROL, 'Контроль'),
    )
    role = models.CharField('Роль',max_length=1,
                                      choices=STATE_IN_RIGHT,
                                      default=EDIT)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.hosp) + ':' + str(self.user)



class Document(models.Model):
    period = models.ForeignKey(Period)
    hosp = models.ForeignKey(Hosp)
    EDIT = 'E'
    WAITCONTROL = 'W'
    NEEDCHANGE = 'C'
    COMPELETE = 'F'
    
    STATE_IN_DOC = (
        (EDIT, 'Редактирование'),
        (WAITCONTROL, 'Согласование'),
        (NEEDCHANGE, 'Корректировка'),
        (COMPELETE, 'Завершено'),
    )
    status = models.CharField('Статус',max_length=1,
                                      choices=STATE_IN_DOC,
                                      default=EDIT)

    datef = models.DateField(auto_now_add=False)
    date_mod= models.DateTimeField(auto_now_add=True)
# !!! поле null=true делает поле sql базы null возможным, blank=true разрешает работать формам - т.е админке!!!!!
# иначе не получится оставить поле не заполненным - а это бывает иногда необходимо!!!!      
#    doc_prev = models.ForeignKey('self', null=True, blank=True)    # ссылка на документ предудущего периода с которым сверяемся
#   отбой, излишне достаточно иметь предудущий период
    def __str__(self):              # __unicode__ on P2
        return str(self.period) + ':' + str(self.hosp)

class Doc1(Document):
    c1_1 = models.IntegerField('Кол1-1', default=0)
    c1_2 = models.IntegerField('Кол1-2',  default=0)
    c1_3 = models.IntegerField('Кол1-3',  default=0)
    c1_4 = models.IntegerField('Кол1-4',  default=0)
    c1_5 = models.IntegerField('Кол1-5',  default=0)

    c2_6 = models.IntegerField('Кол2-6', default=0)
    c2_7 = models.IntegerField('Кол2-7',  default=0)
    c2_8 = models.IntegerField('Кол2-8',  default=0)
    
    c3_1 = models.IntegerField('КолПр3-1', default=0)
    c3_2 = models.IntegerField('КолПр3-2', default=0)
    c3_3 = models.IntegerField('КолПр3-3', default=0)
    c3_4 = models.IntegerField('КолПр3-4', default=0)
    c3_5 = models.IntegerField('КолПр3-5',  default=0)
    c3_6 = models.IntegerField('КолПр3-6',  default=0)
    c3_7 = models.IntegerField('КолПр3-7',  default=0)
    c3_8 = models.IntegerField('КолПр3-8',  default=0)
    
    c4_1 = models.IntegerField('Кол4-1', default=0)
    c4_2 = models.IntegerField('Кол4-2',  default=0)
    c4_3 = models.IntegerField('Кол4-3',  default=0)
    c4_4 = models.IntegerField('Кол4-4',  default=0)
    c4_5 = models.IntegerField('Кол4-5',  default=0)
    c4_6 = models.IntegerField('Кол4-6',  default=0)
    c4_7 = models.IntegerField('Кол4-7',  default=0)
    c4_8 = models.IntegerField('Кол4-8',  default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.period) + ':' + str(self.hosp)

class Doc2(Document):
# порядок именования полей сX_Y_Z   X-таблица номер Y-номер строки Z-номер подстроки
    c2_1   = models.IntegerField('Кол2_1', default=0)
    c2_2   = models.IntegerField('Кол2_2', default=0)
    c2_3   = models.IntegerField('Кол2_3', default=0)
    c2_3_1 = models.IntegerField('Кол2_3_1', default=0)
    c2_3_2 = models.IntegerField('Кол2_3_2', default=0)
    c2_3_3 = models.IntegerField('Кол2_3_3', default=0)
    c2_4   = models.IntegerField('Кол2_4', default=0)
    c2_4_1 = models.IntegerField('Кол2_4_1', default=0)
    c2_4_2 = models.IntegerField('Кол2_4_2', default=0)
    c2_4_3 = models.IntegerField('Кол2_4_3', default=0)
    c2_5   = models.IntegerField('Кол2_5', default=0)
    c2_5_1   = models.IntegerField('Кол2_5_1', default=0)
    c2_5_2   = models.IntegerField('Кол2_5_2', default=0)
    c2_5_3   = models.IntegerField('Кол2_5_3', default=0)
    c2_5_4   = models.IntegerField('Кол2_5_4', default=0)
    c2_5_5   = models.IntegerField('Кол2_5_5', default=0)
    c2_5_6   = models.IntegerField('Кол2_5_6', default=0)
    c2_5_7   = models.IntegerField('Кол2_5_7', default=0)
    c2_5_8   = models.IntegerField('Кол2_5_8', default=0)
    c2_5_9   = models.IntegerField('Кол2_5_9', default=0)
    c2_5_10   = models.IntegerField('Кол2_5_10', default=0)
    c2_5_11   = models.IntegerField('Кол2_5_11', default=0)
    c2_5_12   = models.IntegerField('Кол2_5_12', default=0)
    c2_5_13   = models.IntegerField('Кол2_5_13', default=0)
    c2_5_14   = models.IntegerField('Кол2_5_14', default=0)
    c2_5_15   = models.IntegerField('Кол2_5_15', default=0)
    c2_5_16   = models.IntegerField('Кол2_5_16', default=0)
    c2_5_17   = models.IntegerField('Кол2_5_17', default=0)
    c2_5_18   = models.IntegerField('Кол2_5_18', default=0)
    c2_5_19   = models.IntegerField('Кол2_5_19', default=0)
    c2_5_20   = models.IntegerField('Кол2_5_20', default=0)
    c2_5_21   = models.IntegerField('Кол2_5_21', default=0)
    c2_5_22   = models.IntegerField('Кол2_5_22', default=0)
    c2_5_23   = models.IntegerField('Кол2_5_23', default=0)
    c2_5_24   = models.IntegerField('Кол2_5_24', default=0)
    c2_5_25   = models.IntegerField('Кол2_5_25', default=0)
    c2_5_26   = models.IntegerField('Кол2_5_26', default=0)
    c2_5_27   = models.IntegerField('Кол2_5_27', default=0)
    c2_5_28   = models.IntegerField('Кол2_5_28', default=0)
    c2_5_29   = models.IntegerField('Кол2_5_29', default=0)
    c2_5_30   = models.IntegerField('Кол2_5_30', default=0)
    c2_5_31   = models.IntegerField('Кол2_5_31', default=0)
    c2_5_32   = models.IntegerField('Кол2_5_32', default=0)
    c2_5_33   = models.IntegerField('Кол2_5_33', default=0)
    c2_5_34   = models.IntegerField('Кол2_5_34', default=0)
    c2_5_35   = models.IntegerField('Кол2_5_35', default=0)
    c2_5_36   = models.IntegerField('Кол2_5_36', default=0)
    c2_5_37   = models.IntegerField('Кол2_5_37', default=0)
    c2_5_38   = models.IntegerField('Кол2_5_38', default=0)
    c2_5_39   = models.IntegerField('Кол2_5_39', default=0)
    c2_5_40   = models.IntegerField('Кол2_5_40', default=0)
    c2_5_41   = models.IntegerField('Кол2_5_41', default=0)
    c2_6      = models.IntegerField('Кол2_6', default=0)
    c2_7      = models.IntegerField('Кол2_7', default=0)
    c2_8      = models.IntegerField('Кол2_8', default=0)
    c2_9      = models.IntegerField('Кол2_9', default=0)
    c2_10     = models.IntegerField('Кол2_10', default=0)
    c2_11     = models.IntegerField('Кол2_11', default=0)
    c2_12     = models.IntegerField('Кол2_12', default=0)
    c2_13     = models.IntegerField('Кол2_13', default=0)
    c2_13_1   = models.IntegerField('Кол2_13_1', default=0)
    c2_13_2   = models.IntegerField('Кол2_13_2', default=0)
    c2_13_3   = models.IntegerField('Кол2_13_3', default=0)
    c2_13_4   = models.IntegerField('Кол2_13_4', default=0)
    c2_13_5   = models.IntegerField('Кол2_13_5', default=0)
    c2_13_6   = models.IntegerField('Кол2_13_6', default=0)
    c2_13_7   = models.IntegerField('Кол2_13_7', default=0)
    c2_13_8   = models.IntegerField('Кол2_13_8', default=0)
    c2_13_9   = models.IntegerField('Кол2_13_9', default=0)
    c2_13_10  = models.IntegerField('Кол2_13_10', default=0)
    c2_13_11  = models.IntegerField('Кол2_13_11', default=0)
    c2_13_12  = models.IntegerField('Кол2_13_12', default=0)
    c2_13_13  = models.IntegerField('Кол2_13_13', default=0)
    c2_13_14  = models.IntegerField('Кол2_13_14', default=0)
    c2_13_15  = models.IntegerField('Кол2_13_15', default=0)
    c2_13_16  = models.IntegerField('Кол2_13_16', default=0)
    c2_13_17  = models.IntegerField('Кол2_13_17', default=0)
    c2_13_18  = models.IntegerField('Кол2_13_18', default=0)
    c2_13_19  = models.IntegerField('Кол2_13_19', default=0)
    c2_13_20  = models.IntegerField('Кол2_13_20', default=0)
    c2_13_21  = models.IntegerField('Кол2_13_21', default=0)
    c2_13_22  = models.IntegerField('Кол2_13_22', default=0)
    c2_13_23  = models.IntegerField('Кол2_13_23', default=0)
    c2_13_24  = models.IntegerField('Кол2_13_24', default=0)
    c2_13_25  = models.IntegerField('Кол2_13_25', default=0)
    c2_13_26  = models.IntegerField('Кол2_13_26', default=0)
    c2_13_27  = models.IntegerField('Кол2_13_27', default=0)
    c2_13_28  = models.IntegerField('Кол2_13_28', default=0)
    c2_13_29  = models.IntegerField('Кол2_13_29', default=0)
    c2_13_30  = models.IntegerField('Кол2_13_30', default=0)
    c2_13_31  = models.IntegerField('Кол2_13_31', default=0)
    c2_13_32  = models.IntegerField('Кол2_13_32', default=0)
    c2_13_33  = models.IntegerField('Кол2_13_33', default=0)
    c2_13_34  = models.IntegerField('Кол2_13_34', default=0)
    c2_13_35  = models.IntegerField('Кол2_13_35', default=0)
    c2_13_36  = models.IntegerField('Кол2_13_36', default=0)
    c2_13_37  = models.IntegerField('Кол2_13_37', default=0)
    c2_13_38  = models.IntegerField('Кол2_13_38', default=0)
    c2_13_39  = models.IntegerField('Кол2_13_39', default=0)
    c2_13_40  = models.IntegerField('Кол2_13_40', default=0)
    c2_13_41  = models.IntegerField('Кол2_13_41', default=0)
    c2_13_42  = models.IntegerField('Кол2_13_42', default=0)
    c2_13_43  = models.IntegerField('Кол2_13_43', default=0)
    c2_13_44  = models.IntegerField('Кол2_13_44', default=0)
    c2_13_45  = models.IntegerField('Кол2_13_45', default=0)
    c2_13_46  = models.IntegerField('Кол2_13_46', default=0)
    c2_13_47  = models.IntegerField('Кол2_13_47', default=0)
    c2_13_48  = models.IntegerField('Кол2_13_48', default=0)
    c2_13_49  = models.IntegerField('Кол2_13_49', default=0)
    c2_13_50  = models.IntegerField('Кол2_13_50', default=0)
    c2_13_51  = models.IntegerField('Кол2_13_51', default=0)
    c2_13_52  = models.IntegerField('Кол2_13_52', default=0)
    c2_13_53  = models.IntegerField('Кол2_13_53', default=0)
    c2_13_54  = models.IntegerField('Кол2_13_54', default=0)
    c2_13_55  = models.IntegerField('Кол2_13_55', default=0)
    c2_13_56  = models.IntegerField('Кол2_13_56', default=0)
    c2_13_57  = models.IntegerField('Кол2_13_57', default=0)
    c2_13_58  = models.IntegerField('Кол2_13_58', default=0)
    c2_13_59  = models.IntegerField('Кол2_13_59', default=0)
    c2_13_60  = models.IntegerField('Кол2_13_60', default=0)
    c2_13_61  = models.IntegerField('Кол2_13_61', default=0)
    c2_13_62  = models.IntegerField('Кол2_13_62', default=0)
    c2_13_63  = models.IntegerField('Кол2_13_63', default=0)
    c2_13_64  = models.IntegerField('Кол2_13_64', default=0)
    c2_13_65  = models.IntegerField('Кол2_13_65', default=0)
    c2_13_66  = models.IntegerField('Кол2_13_66', default=0)
    c2_13_67  = models.IntegerField('Кол2_13_67', default=0)
    c2_13_68  = models.IntegerField('Кол2_13_68', default=0)
    c2_13_69  = models.IntegerField('Кол2_13_69', default=0)
    c2_13_70  = models.IntegerField('Кол2_13_70', default=0)
    c2_13_71  = models.IntegerField('Кол2_13_71', default=0)
    c2_13_72  = models.IntegerField('Кол2_13_72', default=0)
    c2_13_73  = models.IntegerField('Кол2_13_73', default=0)
    c2_13_74  = models.IntegerField('Кол2_13_74', default=0)
    c2_13_75  = models.IntegerField('Кол2_13_75', default=0)
    c2_13_76  = models.IntegerField('Кол2_13_76', default=0)
    c2_13_77  = models.IntegerField('Кол2_13_77', default=0)
    c2_13_78  = models.IntegerField('Кол2_13_78', default=0)
    c2_13_79  = models.IntegerField('Кол2_13_79', default=0)
    c2_13_80  = models.IntegerField('Кол2_13_80', default=0)
    c2_13_81  = models.IntegerField('Кол2_13_81', default=0)
    c2_13_82  = models.IntegerField('Кол2_13_82', default=0)
    c2_13_83  = models.IntegerField('Кол2_13_83', default=0)
    c2_13_84  = models.IntegerField('Кол2_13_84', default=0)
    c2_13_85  = models.IntegerField('Кол2_13_85', default=0)
    c2_13_86  = models.IntegerField('Кол2_13_86', default=0)
    c2_13_87  = models.IntegerField('Кол2_13_87', default=0)
    c2_13_88  = models.IntegerField('Кол2_13_88', default=0)
    c2_13_89  = models.IntegerField('Кол2_13_89', default=0)
    c2_13_90  = models.IntegerField('Кол2_13_90', default=0)
    c2_13_91  = models.IntegerField('Кол2_13_91', default=0)
    c2_13_92  = models.IntegerField('Кол2_13_92', default=0)
    c2_13_93  = models.IntegerField('Кол2_13_93', default=0)
    c2_13_94  = models.IntegerField('Кол2_13_94', default=0)
    c2_13_95  = models.IntegerField('Кол2_13_95', default=0)
    c2_13_96  = models.IntegerField('Кол2_13_96', default=0)
    c2_13_97  = models.IntegerField('Кол2_13_97', default=0)
    c2_13_98  = models.IntegerField('Кол2_13_98', default=0)
    c2_13_99  = models.IntegerField('Кол2_13_99', default=0)
    c2_13_100 = models.IntegerField('Кол2_13_100', default=0)
    c2_13_101 = models.IntegerField('Кол2_13_101', default=0)
    c2_13_102 = models.IntegerField('Кол2_13_102', default=0)
    c2_13_103 = models.IntegerField('Кол2_13_103', default=0)
    c2_13_104 = models.IntegerField('Кол2_13_104', default=0)
    c2_13_105 = models.IntegerField('Кол2_13_105', default=0)
    c2_13_106 = models.IntegerField('Кол2_13_106', default=0)
    c2_13_107 = models.IntegerField('Кол2_13_107', default=0)
    c2_13_108 = models.IntegerField('Кол2_13_108', default=0)
    c2_13_109 = models.IntegerField('Кол2_13_109', default=0)
    c2_13_110 = models.IntegerField('Кол2_13_110', default=0)
    c2_13_111 = models.IntegerField('Кол2_13_111', default=0)
    c2_13_112 = models.IntegerField('Кол2_13_112', default=0)
    c2_13_113 = models.IntegerField('Кол2_13_113', default=0)
    c2_13_114 = models.IntegerField('Кол2_13_114', default=0)
    c2_13_115 = models.IntegerField('Кол2_13_115', default=0)
    c2_13_116 = models.IntegerField('Кол2_13_116', default=0)
    c2_13_117 = models.IntegerField('Кол2_13_117', default=0)
    c2_13_118 = models.IntegerField('Кол2_13_118', default=0)
    c2_13_119 = models.IntegerField('Кол2_13_119', default=0)
    c2_13_120 = models.IntegerField('Кол2_13_120', default=0)
    c2_13_121 = models.IntegerField('Кол2_13_121', default=0)
    c2_13_122 = models.IntegerField('Кол2_13_122', default=0)
    c2_13_123 = models.IntegerField('Кол2_13_123', default=0)
    c2_13_124 = models.IntegerField('Кол2_13_124', default=0)

    c2_14 = models.IntegerField('Кол2_14', default=0)
    c2_14_1   = models.IntegerField('Кол2_14_1', default=0)
    c2_14_2   = models.IntegerField('Кол2_14_2', default=0)
    c2_14_3   = models.IntegerField('Кол2_14_3', default=0)
    c2_14_4   = models.IntegerField('Кол2_14_4', default=0)
    c2_14_5   = models.IntegerField('Кол2_14_5', default=0)
    c2_14_6   = models.IntegerField('Кол2_14_6', default=0)
    c2_14_7   = models.IntegerField('Кол2_14_7', default=0)
    c2_14_8   = models.IntegerField('Кол2_14_8', default=0)
    c2_14_9   = models.IntegerField('Кол2_14_9', default=0)
    c2_14_10  = models.IntegerField('Кол2_14_10', default=0)
    c2_14_11  = models.IntegerField('Кол2_14_11', default=0)
    c2_14_12  = models.IntegerField('Кол2_14_12', default=0)
    c2_14_13  = models.IntegerField('Кол2_14_13', default=0)
    c2_14_14  = models.IntegerField('Кол2_14_14', default=0)
    c2_14_14  = models.IntegerField('Кол2_14_14', default=0)
    c2_14_15  = models.IntegerField('Кол2_14_15', default=0)
    c2_14_16  = models.IntegerField('Кол2_14_16', default=0)
    c2_14_17  = models.IntegerField('Кол2_14_17', default=0)
    c2_14_18  = models.IntegerField('Кол2_14_18', default=0)
    c2_14_19  = models.IntegerField('Кол2_14_19', default=0)
    c2_14_20  = models.IntegerField('Кол2_14_20', default=0)
    c2_14_21  = models.IntegerField('Кол2_14_21', default=0)
    c2_14_22  = models.IntegerField('Кол2_14_22', default=0)
    c2_14_23  = models.IntegerField('Кол2_14_23', default=0)
    c2_14_24  = models.IntegerField('Кол2_14_24', default=0)
    c2_14_25  = models.IntegerField('Кол2_14_25', default=0)
    c2_14_26  = models.IntegerField('Кол2_14_26', default=0)
    c2_14_27  = models.IntegerField('Кол2_14_27', default=0)
    c2_14_28  = models.IntegerField('Кол2_14_28', default=0)
    c2_14_29  = models.IntegerField('Кол2_14_29', default=0)
    c2_14_30  = models.IntegerField('Кол2_14_30', default=0)
    c2_14_31  = models.IntegerField('Кол2_14_31', default=0)
    c2_14_32  = models.IntegerField('Кол2_14_32', default=0)
    c2_14_33  = models.IntegerField('Кол2_14_33', default=0)
    c2_14_34  = models.IntegerField('Кол2_14_34', default=0)
    c2_14_35  = models.IntegerField('Кол2_14_35', default=0)
    c2_14_36  = models.IntegerField('Кол2_14_36', default=0)
    c2_14_37  = models.IntegerField('Кол2_14_37', default=0)
    c2_14_38  = models.IntegerField('Кол2_14_38', default=0)
    c2_14_39  = models.IntegerField('Кол2_14_39', default=0)
    c2_14_40  = models.IntegerField('Кол2_14_40', default=0)
    c2_14_41  = models.IntegerField('Кол2_14_41', default=0)
    c2_14_42  = models.IntegerField('Кол2_14_42', default=0)
    c2_14_43  = models.IntegerField('Кол2_14_43', default=0)
    c2_14_44  = models.IntegerField('Кол2_14_44', default=0)
    c2_14_45  = models.IntegerField('Кол2_14_45', default=0)
    c2_15     = models.IntegerField('Кол2_15', default=0)
    c2_16     = models.IntegerField('Кол2_16', default=0)
    c2_17     = models.IntegerField('Кол2_17', default=0)
    c2_18     = models.IntegerField('Кол2_18', default=0)
    c2_19     = models.IntegerField('Кол2_19', default=0)
    c2_20     = models.IntegerField('Кол2_20', default=0)
    c2_21     = models.IntegerField('Кол2_21', default=0)
    c2_22     = models.IntegerField('Кол2_22', default=0)
    c2_23     = models.IntegerField('Кол2_23', default=0)
    c2_24     = models.IntegerField('Кол2_24', default=0)
    c2_25     = models.IntegerField('Кол2_25', default=0)
    c2_26     = models.IntegerField('Кол2_26', default=0)
    c2_27     = models.IntegerField('Кол2_27', default=0)
    c2_28     = models.IntegerField('Кол2_28', default=0)
    
    c3_1      = models.IntegerField('Кол3_1', default=0)
    c3_2      = models.IntegerField('Кол3_2', default=0)
    c3_3      = models.IntegerField('Кол3_3', default=0)
    c3_4      = models.IntegerField('Кол3_4', default=0)
    c3_5      = models.IntegerField('Кол3_5', default=0)
    c3_6      = models.IntegerField('Кол3_6', default=0)
    c3_7      = models.IntegerField('Кол3_7', default=0)
    c3_8      = models.IntegerField('Кол3_8', default=0)
    c3_9      = models.IntegerField('Кол3_9', default=0)
    c3_10     = models.IntegerField('Кол3_10', default=0)
    c3_11     = models.IntegerField('Кол3_11', default=0)
    c3_12     = models.IntegerField('Кол3_12', default=0)
    c3_13     = models.IntegerField('Кол3_13', default=0)
    c3_14     = models.IntegerField('Кол3_14', default=0)
    c3_15     = models.IntegerField('Кол3_15', default=0)
    c3_16     = models.IntegerField('Кол3_16', default=0)
    c3_17     = models.IntegerField('Кол3_17', default=0)
    c3_18     = models.IntegerField('Кол3_18', default=0)
    c3_19     = models.IntegerField('Кол3_19', default=0)
    c3_20     = models.IntegerField('Кол3_20', default=0)
    c3_21     = models.IntegerField('Кол3_21', default=0)
    c3_22     = models.IntegerField('Кол3_22', default=0)
    c3_23     = models.IntegerField('Кол3_23', default=0)
    c3_24     = models.IntegerField('Кол3_24', default=0)
    c3_25     = models.IntegerField('Кол3_25', default=0)
    c3_26     = models.IntegerField('Кол3_26', default=0)
    c3_27     = models.IntegerField('Кол3_27', default=0)
    c3_28     = models.IntegerField('Кол3_28', default=0)
    c3_29     = models.IntegerField('Кол3_29', default=0)
    c3_30     = models.IntegerField('Кол3_30', default=0)
    c3_31     = models.IntegerField('Кол3_31', default=0)
    c3_32     = models.IntegerField('Кол3_32', default=0)
    c3_33     = models.IntegerField('Кол3_33', default=0)
    c3_34     = models.IntegerField('Кол3_34', default=0)
    c3_35     = models.IntegerField('Кол3_35', default=0)
    c3_36     = models.IntegerField('Кол3_36', default=0)
    c3_37     = models.IntegerField('Кол3_37', default=0)
    c3_38     = models.IntegerField('Кол3_38', default=0)

    c4_1      = models.IntegerField('Кол4_1', default=0)
    c4_2      = models.IntegerField('Кол4_2', default=0)
    c4_3      = models.IntegerField('Кол4_3', default=0)
    c4_4      = models.IntegerField('Кол4_4', default=0)
    c4_5      = models.IntegerField('Кол4_5', default=0)
    c4_6      = models.IntegerField('Кол4_6', default=0)
    c4_7      = models.IntegerField('Кол4_7', default=0)
    c4_8      = models.IntegerField('Кол4_8', default=0)
    c4_9      = models.IntegerField('Кол4_9', default=0)
    c4_10     = models.IntegerField('Кол4_10', default=0)
    c4_11     = models.IntegerField('Кол4_11', default=0)
    c4_12     = models.IntegerField('Кол4_12', default=0)
    c4_13     = models.IntegerField('Кол4_13', default=0)
    c4_14     = models.IntegerField('Кол4_14', default=0)
    c4_15     = models.IntegerField('Кол4_15', default=0)

    p3_1      = models.CharField('КолПр3_1', max_length=80, null=True, blank=True)
    p3_2      = models.CharField('КолПр3_2', max_length=80, null=True, blank=True)
    p3_3      = models.CharField('КолПр3_3', max_length=80, null=True, blank=True)
    p3_4      = models.CharField('КолПр3_4', max_length=80, null=True, blank=True)
    p3_5      = models.CharField('КолПр3_5', max_length=80, null=True, blank=True)
    p3_6      = models.CharField('КолПр3_6', max_length=80, null=True, blank=True)
    p3_7      = models.CharField('КолПр3_7', max_length=80, null=True, blank=True)
    p3_8      = models.CharField('КолПр3_8', max_length=80, null=True, blank=True)
    p3_9      = models.CharField('КолПр3_9', max_length=80, null=True, blank=True)
    p3_10     = models.CharField('КолПр3_10', max_length=80, null=True, blank=True)
    p3_11     = models.CharField('КолПр3_11', max_length=80, null=True, blank=True)
    p3_12     = models.CharField('КолПр3_12', max_length=80, null=True, blank=True)
    p3_13     = models.CharField('КолПр3_13', max_length=80, null=True, blank=True)
    p3_14     = models.CharField('КолПр3_14', max_length=80, null=True, blank=True)
    p3_15     = models.CharField('КолПр3_15', max_length=80, null=True, blank=True)
    p3_16     = models.CharField('КолПр3_16', max_length=80, null=True, blank=True)
    p3_17     = models.CharField('КолПр3_17', max_length=80, null=True, blank=True)
    p3_18     = models.CharField('КолПр3_18', max_length=80, null=True, blank=True)
    p3_19     = models.CharField('КолПр3_19', max_length=80, null=True, blank=True)
    p3_20     = models.CharField('КолПр3_20', max_length=80, null=True, blank=True)
    p3_21     = models.CharField('КолПр3_21', max_length=80, null=True, blank=True)
    p3_22     = models.CharField('КолПр3_22', max_length=80, null=True, blank=True)
    p3_23     = models.CharField('КолПр3_23', max_length=80, null=True, blank=True)
    p3_24     = models.CharField('КолПр3_24', max_length=80, null=True, blank=True)
    p3_25     = models.CharField('КолПр3_25', max_length=80, null=True, blank=True)
    p3_26     = models.CharField('КолПр3_26', max_length=80, null=True, blank=True)
    p3_27     = models.CharField('КолПр3_27', max_length=80, null=True, blank=True)
    p3_28     = models.CharField('КолПр3_28', max_length=80, null=True, blank=True)
    p3_29     = models.CharField('КолПр3_29', max_length=80, null=True, blank=True)
    p3_30     = models.CharField('КолПр3_30', max_length=80, null=True, blank=True)
    p3_31     = models.CharField('КолПр3_31', max_length=80, null=True, blank=True)
    p3_32     = models.CharField('КолПр3_32', max_length=80, null=True, blank=True)
    p3_33     = models.CharField('КолПр3_33', max_length=80, null=True, blank=True)
    p3_34     = models.CharField('КолПр3_34', max_length=80, null=True, blank=True)
    p3_35     = models.CharField('КолПр3_35', max_length=80, null=True, blank=True)
    p3_36     = models.CharField('КолПр3_36', max_length=80, null=True, blank=True)
    p3_37     = models.CharField('КолПр3_37', max_length=80, null=True, blank=True)
    p3_38     = models.CharField('КолПр3_38', max_length=80, null=True, blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.period) + ':' + str(self.hosp)

class Doc3(Document):
# тест 
# порядок именования полей сX_Y_Z   X-таблица номер Y-номер строки Z-номер подстроки
    c1_1_1 = models.IntegerField('Кол1_1_1', default=0)
    c1_1_2 = models.IntegerField('Кол1_1_2', default=0)
    c1_2   = models.IntegerField('Кол1_2', default=0)
    c2_1   = models.IntegerField('Кол2_1', default=0)
    c2_2   = models.IntegerField('Кол2_2', default=0)
    c3_1 = models.IntegerField('Кол3_1', default=0)
    c3_2_1 = models.IntegerField('Кол3_2_1', default=0)
    c3_2_2 = models.IntegerField('Кол3_2_2', default=0)
    c4_1 = models.IntegerField('Кол4_1', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.period) + ':' + str(self.hosp)


class Comment(models.Model):
    document  = models.ForeignKey(Document)
    text = models.TextField('Текст комментария')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    EMPTY = 'E'
    ON_CONTROL = 'O'
    CONTROL_YES = 'Y'
    CONTROL_NO = 'N'

    ACTION_COMMENT = (
        (EMPTY, ''),
        (ON_CONTROL, 'На согласование'),
        (CONTROL_YES, 'Согласовано'),
        (CONTROL_NO, 'Не согласовано'),
    )
    action = models.CharField('Действие',max_length=1,
                                      choices= ACTION_COMMENT,
                                      default=EMPTY)



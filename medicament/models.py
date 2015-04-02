# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

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
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    

class Hosp(models.Model):
    name =  models.CharField('Наименование',max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Doc_Hosp(models.Model):
    ''' назначение Документов для заполнения больницам
    '''
    hosp = models.ForeignKey(Hosp)
    doc_type =  models.ForeignKey(Doc_type)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.hosp) + "-" + str(self.doc_type )


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
    
    c3_1 = models.IntegerField('Кол3-1', default=0)
    c3_2 = models.IntegerField('Кол3-2', default=0)
    c3_3 = models.IntegerField('Кол3-3', default=0)
    c3_4 = models.IntegerField('Кол3-4', default=0)
    c3_5 = models.IntegerField('Кол3-5',  default=0)
    c3_6 = models.IntegerField('Кол3-6',  default=0)
    c3_7 = models.IntegerField('Кол3-7',  default=0)
    c3_8 = models.IntegerField('Кол3-8',  default=0)
    
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
    c1_1 = models.IntegerField('Кол1-1', default=0)
    c1_2 = models.IntegerField('Кол1-2',  default=0)
    c1_3 = models.IntegerField('Кол1-3',  default=0)
    c1_4 = models.IntegerField('Кол1-4',  default=0)
    c1_5 = models.IntegerField('Кол1-5',  default=0)
    c1_6 = models.IntegerField('Кол1-6',  default=0)
    c1_7 = models.IntegerField('Кол1-7',  default=0)
    c1_8 = models.IntegerField('Кол1-8',  default=0)

    c2_1 = models.IntegerField('Кол2-1', default=0)
    c2_2 = models.IntegerField('Кол2-2',  default=0)
    c2_3 = models.IntegerField('Кол2-3',  default=0)
    c2_4 = models.IntegerField('Кол2-4',  default=0)
    c2_5 = models.IntegerField('Кол2-5',  default=0)
    
    c3_1 = models.IntegerField('Кол3-1', default=0)
    c3_5 = models.IntegerField('Кол3-5',  default=0)
    c3_6 = models.IntegerField('Кол3-6',  default=0)
    c3_7 = models.IntegerField('Кол3-7',  default=0)
    c3_8 = models.IntegerField('Кол3-8',  default=0)
    
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


class Comment(models.Model):
    document  = models.ForeignKey(Document, default=0)
    text = models.TextField('Текст комментария')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=0)
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


class Role(models.Model):
    user = models.ForeignKey(User,default=0)
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



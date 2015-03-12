# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Period(models.Model):
    name =  models.CharField('Наименование',max_length=100)
    dateb =  models.DateField()
    datee =  models.DateField()
    def __str__(self):              # __unicode__ on Python 2
        return self.name + ' (' + str(self.dateb) + ' - ' + str(self.datee) + ')'
    

class Hosp(models.Model):
    name =  models.CharField('Наименование',max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Document(models.Model):
    period = models.ForeignKey(Period)
    hosp = models.ForeignKey(Hosp)
    EDIT = 'Р'
    WAITCONTROL = 'О'
    NEEDCHANGE = 'И'
    COMPELETE = 'Ф'
    
    STATE_IN_DOC = (
        (EDIT, 'Редактирование'),
        (WAITCONTROL, 'Ожидание утвержд'),
        (NEEDCHANGE, 'Не утверждено'),
        (COMPELETE, 'Завершено'),
    )
    status = models.CharField('Статус',max_length=1,
                                      choices=STATE_IN_DOC,
                                      default=EDIT)

    title  = models.CharField('Заголовок',max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title

   
class Comment(models.Model):
    document  = models.ForeignKey(Document, default=0)
    text = models.TextField('Текст комментария')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=0)

class Role(models.Model):
    user = models.ForeignKey(User,default=0)
    hosp = models.ForeignKey(Hosp)
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

class Row(models.Model):
    name = models.CharField('Наименование',max_length=100) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)

class TabDocument(models.Model):
    document  = models.ForeignKey(Document, default=0)
    row = models.ForeignKey(Row,default=0)
    col1 = models.IntegerField('Кол1', default=0)
    col2 = models.IntegerField('Кол2',  default=0)
    col3 = models.IntegerField('Кол3',  default=0)
    col4 = models.IntegerField('Кол4',  default=0)
    col5 = models.IntegerField('Кол5',  default=0)
    col6 = models.IntegerField('Кол6',  default=0)
    col7 = models.IntegerField('Кол7',  default=0)
    col8 = models.IntegerField('Кол8',  default=0)


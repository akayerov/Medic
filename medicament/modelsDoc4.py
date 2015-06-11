# -*- coding: utf-8 -*-
from django.db import models
from medicament.models import Document, Rows
# Doc4 Изменения в хранении информации - как товар в накладной
class Doc4(Document):
# тест 
# порядок именования полей сX_Y_Z   X-таблица номер Y-номер строки Z-номер подстроки
    KodMO = models.IntegerField('Код МО', default=0)  # Сведения
    c7002 = models.IntegerField('Кол 7002', default=0)  # Итоги

    def __str__(self):              # __unicode__ on Python 2
        return str(self.period) + ':' + str(self.hosp)

class Doc4Tab1000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c3 = models.IntegerField('Таб1000Кол3', default=0) 
    c4 = models.IntegerField('Таб1000Кол4', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab2000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c3 = models.IntegerField('Таб2000Кол3', default=0) 
    c4 = models.IntegerField('Таб2000Кол4', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab3000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c3 = models.IntegerField('Таб3000Кол3', default=0) 
    c4 = models.IntegerField('Таб3000Кол4', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab4000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c4 = models.IntegerField('Таб4000Кол4', default=0) 
    c5 = models.IntegerField('Таб4000Кол5', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab5000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c4 = models.IntegerField('Таб5000Кол4', default=0) 
    c5 = models.IntegerField('Таб5000Кол5', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab5001(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c4 = models.IntegerField('Таб5001Кол4', default=0) 
    c5 = models.IntegerField('Таб5001Кол5', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab6000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c4 = models.IntegerField('Таб6000Кол4', default=0) 
    c5 = models.IntegerField('Таб6000Кол5', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc4Tab7000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc4)  
    row = models.ForeignKey(Rows)
    c4 = models.IntegerField('Таб7000Кол4', default=0) 
    c5 = models.IntegerField('Таб7000Кол5', default=0) 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

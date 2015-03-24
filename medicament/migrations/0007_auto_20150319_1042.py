# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0006_auto_20150318_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='action',
            field=models.CharField(choices=[('E', ''), ('O', 'На согласование'), ('Y', 'Согласовано'), ('N', 'Не согласовано')], default='E', max_length=1, verbose_name='Действие'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('E', 'Редактирование'), ('W', 'Согласование'), ('C', 'Корректировка'), ('F', 'Завершено')], default='E', max_length=1, verbose_name='Статус'),
            preserve_default=True,
        ),
    ]

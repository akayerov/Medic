# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0008_auto_20150610_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='rows',
            name='table',
            field=models.CharField(default='', verbose_name='Таблица', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rows',
            name='name1',
            field=models.CharField(null=True, max_length=20, verbose_name='Доп.Наименов', blank=True),
            preserve_default=True,
        ),
    ]

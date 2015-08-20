# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0009_auto_20150610_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc4',
            name='c7002',
            field=models.IntegerField(verbose_name='Кол 7002', default=0),
            preserve_default=True,
        ),
    ]

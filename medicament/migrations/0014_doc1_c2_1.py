# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0013_auto_20150401_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc1',
            name='c2_1',
            field=models.IntegerField(default=0, verbose_name='Кол2-1'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0012_auto_20150611_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='rows',
            name='nom',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Номер'),
            preserve_default=True,
        ),
    ]

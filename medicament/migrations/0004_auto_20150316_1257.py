# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0003_auto_20150313_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='datef',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]

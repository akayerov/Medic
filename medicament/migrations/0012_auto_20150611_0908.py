# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0011_auto_20150611_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc4',
            name='c7000',
        ),
        migrations.RemoveField(
            model_name='doc4',
            name='c7001',
        ),
    ]

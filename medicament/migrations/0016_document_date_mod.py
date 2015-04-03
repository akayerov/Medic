# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0015_remove_doc1_c2_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date_mod',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 3, 5, 28, 26, 516595, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

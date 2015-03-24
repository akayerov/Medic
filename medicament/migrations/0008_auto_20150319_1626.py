# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0007_auto_20150319_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabdocument',
            name='document',
        ),
        migrations.RemoveField(
            model_name='tabdocument',
            name='row',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
        migrations.DeleteModel(
            name='TabDocument',
        ),
    ]

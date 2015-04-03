# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0014_doc1_c2_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc1',
            name='c2_1',
        ),
    ]

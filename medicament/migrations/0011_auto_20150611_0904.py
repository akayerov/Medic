# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0010_doc4_c7002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc4',
            old_name='с7000',
            new_name='c7000',
        ),
        migrations.RenameField(
            model_name='doc4',
            old_name='с7001',
            new_name='c7001',
        ),
    ]

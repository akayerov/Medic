# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0010_auto_20150326_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc1',
            fields=[
                ('document_ptr', models.OneToOneField(serialize=False, to='medicament.Document', auto_created=True, primary_key=True, parent_link=True)),
                ('c1_1', models.IntegerField(default=0, verbose_name='Кол1-1')),
                ('c1_2', models.IntegerField(default=0, verbose_name='Кол1-2')),
                ('c1_3', models.IntegerField(default=0, verbose_name='Кол1-3')),
                ('c1_4', models.IntegerField(default=0, verbose_name='Кол1-4')),
                ('c1_5', models.IntegerField(default=0, verbose_name='Кол1-5')),
                ('c1_6', models.IntegerField(default=0, verbose_name='Кол1-6')),
                ('c1_7', models.IntegerField(default=0, verbose_name='Кол1-7')),
                ('c1_8', models.IntegerField(default=0, verbose_name='Кол1-8')),
                ('c2_1', models.IntegerField(default=0, verbose_name='Кол2-1')),
                ('c2_2', models.IntegerField(default=0, verbose_name='Кол2-2')),
                ('c2_3', models.IntegerField(default=0, verbose_name='Кол2-3')),
                ('c2_4', models.IntegerField(default=0, verbose_name='Кол2-4')),
                ('c2_5', models.IntegerField(default=0, verbose_name='Кол2-5')),
                ('c3_1', models.IntegerField(default=0, verbose_name='Кол3-1')),
                ('c3_5', models.IntegerField(default=0, verbose_name='Кол3-5')),
                ('c3_6', models.IntegerField(default=0, verbose_name='Кол3-6')),
                ('c3_7', models.IntegerField(default=0, verbose_name='Кол3-7')),
                ('c3_8', models.IntegerField(default=0, verbose_name='Кол3-8')),
                ('c4_1', models.IntegerField(default=0, verbose_name='Кол4-1')),
                ('c4_2', models.IntegerField(default=0, verbose_name='Кол4-2')),
                ('c4_3', models.IntegerField(default=0, verbose_name='Кол4-3')),
                ('c4_4', models.IntegerField(default=0, verbose_name='Кол4-4')),
                ('c4_5', models.IntegerField(default=0, verbose_name='Кол4-5')),
                ('c4_6', models.IntegerField(default=0, verbose_name='Кол4-6')),
                ('c4_7', models.IntegerField(default=0, verbose_name='Кол4-7')),
                ('c4_8', models.IntegerField(default=0, verbose_name='Кол4-8')),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
    ]

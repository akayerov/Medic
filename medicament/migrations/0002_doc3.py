# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc3',
            fields=[
                ('document_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, serialize=False, to='medicament.Document')),
                ('c1_1_1', models.IntegerField(verbose_name='Кол1_1_1', default=0)),
                ('c1_1_2', models.IntegerField(verbose_name='Кол1_1_2', default=0)),
                ('c1_2', models.IntegerField(verbose_name='Кол1_2', default=0)),
                ('c2_1', models.IntegerField(verbose_name='Кол2_1', default=0)),
                ('c2_2', models.IntegerField(verbose_name='Кол2_2', default=0)),
                ('c3_1', models.IntegerField(verbose_name='Кол3_1', default=0)),
                ('c3_2_1', models.IntegerField(verbose_name='Кол3_2_1', default=0)),
                ('c3_2_2', models.IntegerField(verbose_name='Кол3_2_2', default=0)),
                ('c4_1', models.FloatField(verbose_name='Кол4_1', default=0)),
                ('c4_2', models.CharField(blank=True, verbose_name='КолПр3_38', null=True, max_length=80)),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
    ]

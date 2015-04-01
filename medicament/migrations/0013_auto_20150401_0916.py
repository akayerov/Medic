# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0012_doc2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc1',
            name='c1_6',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c1_7',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c1_8',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c2_1',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c2_2',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c2_3',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c2_4',
        ),
        migrations.RemoveField(
            model_name='doc1',
            name='c2_5',
        ),
        migrations.AddField(
            model_name='doc1',
            name='c2_6',
            field=models.IntegerField(default=0, verbose_name='Кол2-6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc1',
            name='c2_7',
            field=models.IntegerField(default=0, verbose_name='Кол2-7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc1',
            name='c2_8',
            field=models.IntegerField(default=0, verbose_name='Кол2-8'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc1',
            name='c3_2',
            field=models.IntegerField(default=0, verbose_name='Кол3-2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc1',
            name='c3_3',
            field=models.IntegerField(default=0, verbose_name='Кол3-3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc1',
            name='c3_4',
            field=models.IntegerField(default=0, verbose_name='Кол3-4'),
            preserve_default=True,
        ),
    ]

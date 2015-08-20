# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0003_auto_20150608_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc4',
            name='с1',
        ),
        migrations.AddField(
            model_name='doc4',
            name='KodMO',
            field=models.IntegerField(verbose_name='Код МО', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc4',
            name='с7000',
            field=models.IntegerField(verbose_name='Кол 7000', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc4',
            name='с7001',
            field=models.IntegerField(verbose_name='Кол 7001', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_10',
            field=models.FloatField(verbose_name='Кол2_10', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_11',
            field=models.FloatField(verbose_name='Кол2_11', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_12',
            field=models.FloatField(verbose_name='Кол2_12', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_21',
            field=models.FloatField(verbose_name='Кол2_21', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_22',
            field=models.FloatField(verbose_name='Кол2_22', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_23',
            field=models.FloatField(verbose_name='Кол2_23', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_24',
            field=models.FloatField(verbose_name='Кол2_24', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_25',
            field=models.FloatField(verbose_name='Кол2_25', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_26',
            field=models.FloatField(verbose_name='Кол2_26', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_8',
            field=models.FloatField(verbose_name='Кол2_8', default=0),
            preserve_default=True,
        ),
    ]

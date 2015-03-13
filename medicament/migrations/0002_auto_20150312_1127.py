# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col1',
            field=models.IntegerField(default=0, verbose_name='Кол1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col2',
            field=models.IntegerField(default=0, verbose_name='Кол2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col3',
            field=models.IntegerField(default=0, verbose_name='Кол3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col4',
            field=models.IntegerField(default=0, verbose_name='Кол4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col5',
            field=models.IntegerField(default=0, verbose_name='Кол5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col6',
            field=models.IntegerField(default=0, verbose_name='Кол6'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col7',
            field=models.IntegerField(default=0, verbose_name='Кол7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tabdocument',
            name='col8',
            field=models.IntegerField(default=0, verbose_name='Кол8'),
            preserve_default=True,
        ),
    ]

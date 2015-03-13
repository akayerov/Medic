# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0002_auto_20150312_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_Hosp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('doc_type', models.ForeignKey(to='medicament.Doc_type')),
                ('hosp', models.ForeignKey(to='medicament.Hosp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='document',
            name='date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.AddField(
            model_name='document',
            name='datef',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 5, 48, 967029, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='tel',
            field=models.CharField(verbose_name='Телефон', max_length=20, default=' '),
            preserve_default=False,
        ),
    ]

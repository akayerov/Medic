# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0002_doc3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc4',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, serialize=False, to='medicament.Document', auto_created=True, primary_key=True)),
                ('с1', models.IntegerField(default=0, verbose_name='Кол1')),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
        migrations.CreateModel(
            name='Doc4Tab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val', models.FloatField(default=0, verbose_name='Значение')),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
                ('typepar', models.CharField(verbose_name='Тип значения', max_length=1)),
                ('type', models.ForeignKey(to='medicament.Doc_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='doc4tab',
            name='par',
            field=models.ForeignKey(to='medicament.Parameter'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0005_remove_parameter_typepar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('type', models.ForeignKey(to='medicament.Doc_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='type',
        ),
        migrations.AlterField(
            model_name='doc4tab',
            name='par',
            field=models.ForeignKey(to='medicament.Rows'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Parameter',
        ),
    ]

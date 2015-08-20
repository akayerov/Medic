# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0006_auto_20150610_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc4Tab1000',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('c3', models.IntegerField(default=0, verbose_name='Таб1000Кол3')),
                ('c4', models.IntegerField(default=0, verbose_name='Таб1000Кол4')),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='doc4tab',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='doc4tab',
            name='par',
        ),
        migrations.DeleteModel(
            name='Doc4Tab',
        ),
    ]

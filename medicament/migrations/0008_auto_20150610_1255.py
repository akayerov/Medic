# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0007_auto_20150610_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc4Tab2000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c3', models.IntegerField(verbose_name='Таб2000Кол3', default=0)),
                ('c4', models.IntegerField(verbose_name='Таб2000Кол4', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab3000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c3', models.IntegerField(verbose_name='Таб3000Кол3', default=0)),
                ('c4', models.IntegerField(verbose_name='Таб3000Кол4', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab4000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c4', models.IntegerField(verbose_name='Таб4000Кол4', default=0)),
                ('c5', models.IntegerField(verbose_name='Таб4000Кол5', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab5000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c4', models.IntegerField(verbose_name='Таб5000Кол4', default=0)),
                ('c5', models.IntegerField(verbose_name='Таб5000Кол5', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab5001',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c4', models.IntegerField(verbose_name='Таб5001Кол4', default=0)),
                ('c5', models.IntegerField(verbose_name='Таб5001Кол5', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab6000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c4', models.IntegerField(verbose_name='Таб6000Кол4', default=0)),
                ('c5', models.IntegerField(verbose_name='Таб6000Кол5', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc4Tab7000',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c4', models.IntegerField(verbose_name='Таб7000Кол4', default=0)),
                ('c5', models.IntegerField(verbose_name='Таб7000Кол5', default=0)),
                ('doc', models.ForeignKey(to='medicament.Doc4')),
                ('row', models.ForeignKey(to='medicament.Rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rows',
            name='name1',
            field=models.CharField(verbose_name='Доп.Наименов', max_length=20, default=''),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=1, default='E', verbose_name='Действие', choices=[('E', ''), ('O', 'На согласование'), ('Y', 'Согласовано'), ('N', 'Не согласовано')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc_Hosp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=1, default='E', verbose_name='Статус', choices=[('E', 'Редактирование'), ('W', 'Согласование'), ('C', 'Корректировка'), ('F', 'Завершено')])),
                ('datef', models.DateField()),
                ('date_mod', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc2',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, to='medicament.Document', primary_key=True, serialize=False, parent_link=True)),
                ('c1', models.IntegerField(default=0, verbose_name='Кол1')),
                ('c2', models.IntegerField(default=0, verbose_name='Кол2')),
                ('c2_1', models.IntegerField(default=0, verbose_name='Кол2.1')),
                ('c2_2', models.IntegerField(default=0, verbose_name='Кол2.2')),
                ('c2_3', models.IntegerField(default=0, verbose_name='Кол2.3')),
                ('c3', models.FloatField(default=0, verbose_name='Кол3')),
                ('c3_0', models.IntegerField(default=0, verbose_name='Кол3.0')),
                ('c3_1', models.FloatField(default=0, verbose_name='Кол3.1')),
                ('c3_1_1', models.IntegerField(default=0, verbose_name='Кол3.1.1')),
                ('c3_1_2', models.IntegerField(default=0, verbose_name='Кол3.1.2')),
                ('c3_2', models.FloatField(default=0, verbose_name='Кол3.2')),
                ('c3_2_1', models.IntegerField(default=0, verbose_name='Кол3.2.1')),
                ('c3_2_2', models.IntegerField(default=0, verbose_name='Кол3.2.2')),
                ('c4', models.FloatField(default=0, verbose_name='Кол4')),
                ('c4_1', models.IntegerField(default=0, verbose_name='Кол4.1')),
                ('c5', models.IntegerField(default=0, verbose_name='Кол5')),
                ('c6', models.IntegerField(default=0, verbose_name='Кол6')),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
        migrations.CreateModel(
            name='Doc1',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, to='medicament.Document', primary_key=True, serialize=False, parent_link=True)),
                ('c1_1', models.IntegerField(default=0, verbose_name='Кол1-1')),
                ('c1_2', models.IntegerField(default=0, verbose_name='Кол1-2')),
                ('c1_3', models.IntegerField(default=0, verbose_name='Кол1-3')),
                ('c1_4', models.IntegerField(default=0, verbose_name='Кол1-4')),
                ('c1_5', models.IntegerField(default=0, verbose_name='Кол1-5')),
                ('c2_6', models.IntegerField(default=0, verbose_name='Кол2-6')),
                ('c2_7', models.IntegerField(default=0, verbose_name='Кол2-7')),
                ('c2_8', models.IntegerField(default=0, verbose_name='Кол2-8')),
                ('c3_1', models.IntegerField(default=0, verbose_name='Кол3-1')),
                ('c3_2', models.IntegerField(default=0, verbose_name='Кол3-2')),
                ('c3_3', models.IntegerField(default=0, verbose_name='Кол3-3')),
                ('c3_4', models.IntegerField(default=0, verbose_name='Кол3-4')),
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
        migrations.CreateModel(
            name='Hosp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Наименование Краткое')),
                ('name_full', models.CharField(max_length=255, verbose_name='Наименование Полное')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('dateb', models.DateField()),
                ('datee', models.DateField()),
                ('prev', models.ForeignKey(blank=True, null=True, to='medicament.Period')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='Регион')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tel', models.CharField(max_length=20, verbose_name='Телефон')),
                ('role', models.CharField(max_length=1, default='Р', verbose_name='Роль', choices=[('Р', 'Редактирование'), ('К', 'Контроль')])),
                ('hosp', models.ForeignKey(to='medicament.Hosp')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hosp',
            name='region',
            field=models.ForeignKey(blank=True, null=True, to='medicament.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='hosp',
            field=models.ForeignKey(to='medicament.Hosp'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='period',
            field=models.ForeignKey(to='medicament.Period'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc_hosp',
            name='doc_type',
            field=models.ForeignKey(to='medicament.Doc_type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc_hosp',
            name='hosp',
            field=models.ForeignKey(to='medicament.Hosp'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(to='medicament.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

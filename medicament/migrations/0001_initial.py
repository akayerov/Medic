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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(verbose_name='Действие', choices=[('E', ''), ('O', 'На согласование'), ('Y', 'Согласовано'), ('N', 'Не согласовано')], max_length=1, default='E')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc_Hosp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.CharField(verbose_name='Статус', choices=[('E', 'Редактирование'), ('W', 'Согласование'), ('C', 'Корректировка'), ('F', 'Завершено')], max_length=1, default='E')),
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
                ('document_ptr', models.OneToOneField(parent_link=True, to='medicament.Document', auto_created=True, primary_key=True, serialize=False)),
                ('c1', models.IntegerField(verbose_name='Кол1', default=0)),
                ('c2', models.IntegerField(verbose_name='Кол2', default=0)),
                ('c2_1', models.IntegerField(verbose_name='Кол2.1', default=0)),
                ('c2_2', models.IntegerField(verbose_name='Кол2.2', default=0)),
                ('c2_3', models.IntegerField(verbose_name='Кол2.3', default=0)),
                ('c3', models.FloatField(verbose_name='Кол3', default=0)),
                ('c3_0', models.IntegerField(verbose_name='Кол3.0', default=0)),
                ('c3_1', models.FloatField(verbose_name='Кол3.1', default=0)),
                ('c3_1_1', models.IntegerField(verbose_name='Кол3.1.1', default=0)),
                ('c3_1_2', models.IntegerField(verbose_name='Кол3.1.2', default=0)),
                ('c3_2', models.FloatField(verbose_name='Кол3.2', default=0)),
                ('c3_2_1', models.IntegerField(verbose_name='Кол3.2.1', default=0)),
                ('c3_2_2', models.IntegerField(verbose_name='Кол3.2.2', default=0)),
                ('c4', models.FloatField(verbose_name='Кол4', default=0)),
                ('c4_1', models.IntegerField(verbose_name='Кол4.1', default=0)),
                ('c5', models.IntegerField(verbose_name='Кол5', default=0)),
                ('c6', models.IntegerField(verbose_name='Кол6', default=0)),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
        migrations.CreateModel(
            name='Doc1',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, to='medicament.Document', auto_created=True, primary_key=True, serialize=False)),
                ('c1_1', models.IntegerField(verbose_name='Кол1-1', default=0)),
                ('c1_2', models.IntegerField(verbose_name='Кол1-2', default=0)),
                ('c1_3', models.IntegerField(verbose_name='Кол1-3', default=0)),
                ('c1_4', models.IntegerField(verbose_name='Кол1-4', default=0)),
                ('c1_5', models.IntegerField(verbose_name='Кол1-5', default=0)),
                ('c2_6', models.IntegerField(verbose_name='Кол2-6', default=0)),
                ('c2_7', models.IntegerField(verbose_name='Кол2-7', default=0)),
                ('c2_8', models.IntegerField(verbose_name='Кол2-8', default=0)),
                ('c3_1', models.IntegerField(verbose_name='Кол3-1', default=0)),
                ('c3_2', models.IntegerField(verbose_name='Кол3-2', default=0)),
                ('c3_3', models.IntegerField(verbose_name='Кол3-3', default=0)),
                ('c3_4', models.IntegerField(verbose_name='Кол3-4', default=0)),
                ('c3_5', models.IntegerField(verbose_name='Кол3-5', default=0)),
                ('c3_6', models.IntegerField(verbose_name='Кол3-6', default=0)),
                ('c3_7', models.IntegerField(verbose_name='Кол3-7', default=0)),
                ('c3_8', models.IntegerField(verbose_name='Кол3-8', default=0)),
                ('c4_1', models.IntegerField(verbose_name='Кол4-1', default=0)),
                ('c4_2', models.IntegerField(verbose_name='Кол4-2', default=0)),
                ('c4_3', models.IntegerField(verbose_name='Кол4-3', default=0)),
                ('c4_4', models.IntegerField(verbose_name='Кол4-4', default=0)),
                ('c4_5', models.IntegerField(verbose_name='Кол4-5', default=0)),
                ('c4_6', models.IntegerField(verbose_name='Кол4-6', default=0)),
                ('c4_7', models.IntegerField(verbose_name='Кол4-7', default=0)),
                ('c4_8', models.IntegerField(verbose_name='Кол4-8', default=0)),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
        migrations.CreateModel(
            name='Hosp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
                ('dateb', models.DateField()),
                ('datee', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tel', models.CharField(verbose_name='Телефон', max_length=20)),
                ('role', models.CharField(verbose_name='Роль', choices=[('Р', 'Редактирование'), ('К', 'Контроль')], max_length=1, default='Р')),
                ('hosp', models.ForeignKey(to='medicament.Hosp')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
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

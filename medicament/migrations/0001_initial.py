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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default='Р', choices=[('Р', 'Редактирование'), ('О', 'Ожидание утвержд'), ('И', 'Не утверждено'), ('Ф', 'Завершено')], verbose_name='Статус', max_length=1)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hosp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default='Р', choices=[('Р', 'Редактирование'), ('К', 'Контроль')], verbose_name='Роль', max_length=1)),
                ('hosp', models.ForeignKey(to='medicament.Hosp')),
                ('user', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TabDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('col1', models.IntegerField(verbose_name='Кол1')),
                ('col2', models.IntegerField(verbose_name='Кол2')),
                ('col3', models.IntegerField(verbose_name='Кол3')),
                ('col4', models.IntegerField(verbose_name='Кол4')),
                ('col5', models.IntegerField(verbose_name='Кол5')),
                ('col6', models.IntegerField(verbose_name='Кол6')),
                ('col7', models.IntegerField(verbose_name='Кол7')),
                ('col8', models.IntegerField(verbose_name='Кол8')),
                ('document', models.ForeignKey(default=0, to='medicament.Document')),
                ('row', models.ForeignKey(default=0, to='medicament.Row')),
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
            model_name='document',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(default=0, to='medicament.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

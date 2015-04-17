# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('content', models.CharField(max_length=150)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=15)),
                ('fullname', models.CharField(max_length=20, verbose_name=b'full name')),
                ('email', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='author',
            field=models.ForeignKey(to='backend.User'),
        ),
    ]

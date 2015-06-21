# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('uses', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('uses', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

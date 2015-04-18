# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20150417_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('content', models.CharField(max_length=150)),
                ('uses', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ManyToManyField(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('content', models.CharField(max_length=150)),
                ('uses', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='card',
            name='author',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]

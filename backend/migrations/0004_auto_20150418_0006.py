# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_auto_20150418_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='owner',
        ),
        migrations.AddField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

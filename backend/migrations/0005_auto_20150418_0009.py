# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20150418_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]

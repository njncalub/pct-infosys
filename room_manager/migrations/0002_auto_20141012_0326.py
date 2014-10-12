# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='building',
            field=models.CharField(max_length=50, null=True, verbose_name='building', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.IntegerField(max_length=1, null=True, verbose_name='floor', blank=True),
            preserve_default=True,
        ),
    ]

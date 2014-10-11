# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_year_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolyear',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='schoolyear',
            name='end_year',
            field=models.IntegerField(max_length=4, unique=True, null=True, verbose_name='end year', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolyear',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='schoolyear',
            name='start_year',
            field=models.IntegerField(max_length=4, unique=True, null=True, verbose_name='start year', blank=True),
        ),
    ]

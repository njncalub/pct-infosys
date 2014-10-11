# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='date_end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='date_start',
            field=models.DateField(null=True, verbose_name='start date', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0007_auto_20141011_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectinstance',
            name='instance_code',
            field=models.CharField(max_length=15, null=True, verbose_name='instance code', blank=True),
        ),
    ]

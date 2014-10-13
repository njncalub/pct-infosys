# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0002_subjectinstance_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectinstance',
            name='instance_code',
            field=models.CharField(max_length=25, null=True, verbose_name='instance code', blank=True),
        ),
    ]

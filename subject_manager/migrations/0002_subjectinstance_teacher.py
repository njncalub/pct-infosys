# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_profiling', '0001_initial'),
        ('subject_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectinstance',
            name='teacher',
            field=models.ForeignKey(blank=True, to='teacher_profiling.Teacher', null=True),
            preserve_default=True,
        ),
    ]

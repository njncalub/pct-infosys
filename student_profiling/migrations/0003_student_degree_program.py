# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program_manager', '0001_initial'),
        ('student_profiling', '0002_auto_20141011_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='degree_program',
            field=models.ForeignKey(blank=True, to='program_manager.DegreeProgram', null=True),
            preserve_default=True,
        ),
    ]

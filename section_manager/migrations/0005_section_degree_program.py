# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program_manager', '0001_initial'),
        ('section_manager', '0004_auto_20141012_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='degree_program',
            field=models.ForeignKey(blank=True, to='program_manager.DegreeProgram', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('section_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectioninstance',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='sectioninstance',
            unique_together=set([('section', 'school_year')]),
        ),
        migrations.AddField(
            model_name='section',
            name='degree_program',
            field=models.ForeignKey(blank=True, to='program_manager.DegreeProgram', null=True),
            preserve_default=True,
        ),
    ]

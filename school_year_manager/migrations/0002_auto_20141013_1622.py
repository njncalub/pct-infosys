# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_year_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together=set([('semester', 'school_year')]),
        ),
        migrations.AlterUniqueTogether(
            name='schoolyear',
            unique_together=set([('start_year', 'end_year')]),
        ),
    ]

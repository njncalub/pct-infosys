# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0008_auto_20141011_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectinstance',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]

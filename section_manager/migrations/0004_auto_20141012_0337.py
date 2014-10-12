# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('section_manager', '0003_auto_20141012_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioninstance',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]

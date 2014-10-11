# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_year_manager', '0002_auto_20141011_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolyear',
            options={'verbose_name': 'school year'},
        ),
    ]

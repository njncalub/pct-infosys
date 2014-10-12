# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section_manager', '0002_section_year_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='year_level',
            field=models.IntegerField(default=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')], max_length=1, blank=True, null=True, verbose_name='year level'),
        ),
    ]

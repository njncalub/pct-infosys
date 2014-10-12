# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='year_level',
            field=models.IntegerField(default=1, max_length=1, verbose_name='year level', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
    ]

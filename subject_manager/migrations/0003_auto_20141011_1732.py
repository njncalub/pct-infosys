# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0002_auto_20141011_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='days',
            field=models.CharField(default=b'M-F', max_length=3, verbose_name='days', choices=[(b'M-F', b'Mondays-Fridays'), (b'SAT', b'Saturdays'), (b'SUN', b'Sundays')]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='room',
            field=models.ForeignKey(blank=True, to='room_manager.Room', null=True),
        ),
    ]

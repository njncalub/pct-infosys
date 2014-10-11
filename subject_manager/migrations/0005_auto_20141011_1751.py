# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_manager', '0001_initial'),
        ('subject_manager', '0004_subjectinstance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='days',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='room',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='time',
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='date_end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='date_start',
            field=models.DateField(null=True, verbose_name='start date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='days',
            field=models.CharField(default=b'M-F', max_length=3, verbose_name='days', choices=[(b'M-F', b'Mondays-Fridays'), (b'SAT', b'Saturdays'), (b'SUN', b'Sundays')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='room',
            field=models.ForeignKey(blank=True, to='room_manager.Room', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='time',
            field=models.CharField(default=b'0800AM', max_length=6, verbose_name='time', choices=[(b'0800AM', b'08:00AM-12:00PM'), (b'0100PM', b'01:00PM-05:00PM'), (b'0530PM', b'05:30PM-09:30PM')]),
            preserve_default=True,
        ),
    ]

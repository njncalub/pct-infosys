# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=15, verbose_name='code')),
                ('name', models.CharField(max_length=35, verbose_name='name')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('units', models.IntegerField(default=3, max_length=1, verbose_name='units')),
                ('time', models.CharField(default=b'0800AM', max_length=6, verbose_name='time', choices=[(b'0800AM', b'08:00AM-12:00PM'), (b'0100PM', b'01:00PM-05:00PM'), (b'0530PM', b'05:30PM-09:30PM')])),
                ('days', models.CharField(default=b'M-F', max_length=3, verbose_name='days', choices=[(b'M-F', b'M-F'), (b'SAT', b'SAT'), (b'SUN', b'SUN')])),
                ('date_start', models.DateTimeField(null=True, verbose_name='start date', blank=True)),
                ('date_end', models.DateTimeField(null=True, verbose_name='end date', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('room', models.ForeignKey(to='room_manager.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

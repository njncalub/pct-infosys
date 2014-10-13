# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('section_manager', '0001_initial'),
        ('teacher_profiling', '0001_initial'),
        ('room_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_year_manager', '0001_initial'),
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
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_code', models.CharField(max_length=25, null=True, verbose_name='instance code', blank=True)),
                ('time', models.CharField(default=b'0800AM', max_length=6, verbose_name='time', choices=[(b'0800AM', b'08:00AM-12:00PM'), (b'0100PM', b'01:00PM-05:00PM'), (b'0530PM', b'05:30PM-09:30PM')])),
                ('days', models.CharField(default=b'M-F', max_length=3, verbose_name='days', choices=[(b'M-F', b'Mondays-Fridays'), (b'SAT', b'Saturdays'), (b'SUN', b'Sundays')])),
                ('date_start', models.DateField(null=True, verbose_name='start date', blank=True)),
                ('date_end', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('room', models.ForeignKey(blank=True, to='room_manager.Room', null=True)),
                ('section', models.ForeignKey(to='section_manager.SectionInstance')),
                ('semester', models.ForeignKey(to='school_year_manager.Semester')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('subject', models.ForeignKey(to='subject_manager.Subject')),
                ('teacher', models.ForeignKey(blank=True, to='teacher_profiling.Teacher', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

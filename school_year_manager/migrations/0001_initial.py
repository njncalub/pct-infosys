# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_year', models.IntegerField(max_length=4, unique=True, null=True, verbose_name='start year', blank=True)),
                ('end_year', models.IntegerField(max_length=4, unique=True, null=True, verbose_name='end year', blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
            ],
            options={
                'verbose_name': 'school year',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.CharField(max_length=6, verbose_name='semester', choices=[(b'1STSEM', b'1st semester'), (b'2NDSEM', b'2nd semester'), (b'SUMMER', b'Summer')])),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('school_year', models.ForeignKey(to='school_year_manager.SchoolYear')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_year_manager', '0002_auto_20141011_1505'),
        ('subject_manager', '0003_auto_20141011_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('school_year', models.ForeignKey(to='school_year_manager.SchoolYear')),
                ('subject', models.ForeignKey(to='subject_manager.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

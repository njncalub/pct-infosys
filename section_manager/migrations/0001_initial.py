# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('school_year_manager', '0003_auto_20141011_1751'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name='section name')),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('school_year', models.ForeignKey(to='school_year_manager.SchoolYear')),
                ('section', models.ForeignKey(to='section_manager.Section')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

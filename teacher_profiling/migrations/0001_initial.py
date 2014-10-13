# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='last name', blank=True)),
                ('first_name', models.CharField(max_length=200, null=True, verbose_name='first name', blank=True)),
                ('middle_name', models.CharField(max_length=200, null=True, verbose_name='middle name', blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True, verbose_name='sex', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birth_date', models.DateField(null=True, verbose_name='birth date', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

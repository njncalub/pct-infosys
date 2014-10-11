# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=30, verbose_name='room name')),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

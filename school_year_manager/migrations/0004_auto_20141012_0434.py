# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_year_manager', '0003_auto_20141011_1751'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='schoolyear',
            name='modified_at',
            field=models.DateTimeField(null=True, verbose_name='modified at', blank=True),
            preserve_default=True,
        ),
    ]

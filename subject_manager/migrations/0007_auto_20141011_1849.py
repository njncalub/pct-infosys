# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0006_subjectinstance_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectinstance',
            name='description',
        ),
        migrations.AddField(
            model_name='subjectinstance',
            name='instance_code',
            field=models.TextField(null=True, verbose_name='instance code', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('program_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='username')),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='email', blank=True)),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='last name', blank=True)),
                ('first_name', models.CharField(max_length=200, null=True, verbose_name='first name', blank=True)),
                ('middle_name', models.CharField(max_length=200, null=True, verbose_name='middle name', blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True, verbose_name='sex', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birth_date', models.DateField(null=True, verbose_name='birth date', blank=True)),
                ('address', models.TextField(max_length=200, null=True, verbose_name='address', blank=True)),
                ('mobile_number', models.CharField(max_length=200, null=True, verbose_name='mobile number', blank=True)),
                ('landline_number', models.CharField(max_length=200, null=True, verbose_name='landline number', blank=True)),
                ('website_address', models.URLField(null=True, verbose_name='website address', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False)),
                ('modified_at', models.DateTimeField(null=True, verbose_name='modified at', blank=True)),
                ('degree_program', models.ForeignKey(blank=True, to='program_manager.DegreeProgram', null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

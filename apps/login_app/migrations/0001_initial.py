# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('birthday', models.CharField(max_length=15)),
            ],
        ),
    ]

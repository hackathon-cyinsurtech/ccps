# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='value',
            field=models.SmallIntegerField(),
        ),
    ]

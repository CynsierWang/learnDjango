# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_duty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='class_1',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='duty',
            name='class_2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='duty',
            name='class_3',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='duty',
            name='class_4',
            field=models.IntegerField(default=1),
        ),
    ]
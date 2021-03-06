# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-20 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_semester'),
        ('books', '0006_auto_20180120_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdescription',
            name='department',
            field=models.ManyToManyField(to='department.Department'),
        ),
        migrations.AddField(
            model_name='bookdescription',
            name='semester',
            field=models.ManyToManyField(to='department.Semester'),
        ),
        migrations.AddField(
            model_name='bookdescription',
            name='subject',
            field=models.ManyToManyField(to='department.Subject'),
        ),
    ]

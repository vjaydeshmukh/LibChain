# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171001_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, choices=[('COMPUTER SCIENCE AND ENGINEERING', 'COMPUTER SCIENCE AND ENGINEERING'), ('ELECTRONICS AND TELECOMMUNICATIONS', 'ELECTRONICS AND TELECOMMUNICATIONS'), ('ELECTRICAL AND ELCETRONICS ENGINEERING', 'ELECTRICAL AND ELCETRONICS ENGINEERING'), ('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'), ('CIVIL ENGINEERING', 'CIVIL ENGINEERING')], max_length=200, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-20 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20180120_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='hash',
            new_name='issue_hash',
        ),
        migrations.AddField(
            model_name='transaction',
            name='return_hash',
            field=models.CharField(default='0xasdfg12345', max_length=200),
        ),
    ]
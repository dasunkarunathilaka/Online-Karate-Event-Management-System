# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-30 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0005_auto_20180918_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='DistrictName',
            new_name='districtName',
        ),
        migrations.AddField(
            model_name='district',
            name='districtSecretaryName',
            field=models.CharField(default='John Smith', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='telephone',
            field=models.CharField(default='912235933', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='province',
            name='provinceSecretaryName',
            field=models.CharField(default='Steve Carter', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='province',
            name='telephone',
            field=models.CharField(default='+945687123', max_length=12),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-18 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slkf',
            name='memberName',
        ),
    ]
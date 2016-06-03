# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mendel', '0004_auto_20160527_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='architizer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='of_type',
            field=models.CharField(choices=[('S', 'Product Search'), ('R', 'Product Response')], max_length=10),
        ),
    ]
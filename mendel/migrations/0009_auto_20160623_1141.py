# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-23 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mendel', '0008_auto_20160613_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='context',
            old_name='keyword',
            new_name='keyword_given',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='keyword',
            new_name='keyword_given',
        ),
        migrations.AddField(
            model_name='review',
            name='keyword_proposed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='keyword_proposed', to='mendel.Keyword'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('context', 'keyword_proposed', 'category', 'user', 'status')]),
        ),
    ]

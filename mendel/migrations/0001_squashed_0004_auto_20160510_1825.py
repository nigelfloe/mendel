# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'mendel', '0001_initial'), (b'mendel', '0002_auto_20160510_1816'), (b'mendel', '0003_auto_20160510_1817'), (b'mendel', '0004_auto_20160510_1825')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_from', models.IntegerField()),
                ('position_to', models.IntegerField()),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('of_type', models.CharField(choices=[('CSV', 'csv'), ('TXT', 'txt')], max_length=10)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mendel.Category')),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mendel.Content')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mendel.Keyword')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mendel.Document'),
        ),
        migrations.AddField(
            model_name='content',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mendel.Keyword'),
        ),
    ]

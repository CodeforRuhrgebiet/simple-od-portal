# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_ts', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(editable=False, max_length=500, unique=True, verbose_name='Slug')),
                ('file_path', models.FilePathField(path='/home/simonwoerpel/Projects/simple-od-portal/simple_od_portal/datasets/source', recursive=True, verbose_name='File path')),
                ('file_path_relative', models.CharField(editable=False, max_length=500)),
                ('source_name', models.CharField(max_length=500, verbose_name='Source name')),
                ('source_url', models.URLField(blank=True, null=True, verbose_name='Source url')),
                ('published_date', models.DateField(blank=True, null=True, verbose_name='Published date')),
                ('file_content', models.TextField(editable=False, verbose_name='File content')),
                ('tags_raw', models.CharField(blank=True, help_text='Enter comma seperated tags', max_length=256, null=True, verbose_name='Tags')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]

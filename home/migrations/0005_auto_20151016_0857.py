# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('home', '0004_auto_20151016_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEventTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='newsevent',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='home.NewsEventTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='newseventtag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='tagged_items', to='home.NewsEvent'),
        ),
        migrations.AddField(
            model_name='newseventtag',
            name='tag',
            field=models.ForeignKey(related_name='home_newseventtag_items', to='taggit.Tag'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('home', '0003_newsevent_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevent',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='newsevent',
            name='repeat_annually',
            field=models.BooleanField(default=False, help_text='Is this an annual event?'),
        ),
    ]

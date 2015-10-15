# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0002_create_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEvent',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date_start', models.DateField(verbose_name='Start date')),
                ('date_end', models.DateField(help_text='Not required if event is on a single day', null=True, verbose_name='End date', blank=True)),
                ('time_start', models.TimeField(null=True, verbose_name='Start time', blank=True)),
                ('time_end', models.TimeField(null=True, verbose_name='End time', blank=True)),
                ('location', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('repeat_annually', models.BooleanField(default=False, help_text='Is this an annual event? (default: No)')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

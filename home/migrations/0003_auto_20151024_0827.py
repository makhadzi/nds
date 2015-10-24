# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailadmin.taggable
import modelcluster.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0002_create_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
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
                ('province', models.CharField(blank=True, max_length=255, choices=[('easterncape', 'Eastern Cape'), ('freestate', 'Free State'), ('gauteng', 'Gauteng'), ('kwazulunatal', 'Kwazulu Natal'), ('limpopo', 'Limpopo'), ('mpumalanga', 'Mpumalanga'), ('northwest', 'North West'), ('northerncape', 'Northern Cape'), ('westerncape', 'Western Cape')])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', wagtail.wagtailadmin.taggable.TagSearchable),
        ),
        migrations.CreateModel(
            name='NewsEventTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='home.NewsEvent')),
                ('tag', models.ForeignKey(related_name='home_newseventtag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newsevent',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='home.NewsEventTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]

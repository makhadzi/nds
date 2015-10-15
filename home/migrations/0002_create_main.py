# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_main(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    Main = apps.get_model('home.Main')

    # Delete the default homepage
    Page.objects.get(id=2).delete()

    # Create content type for homepage model
    main_content_type, created = ContentType.objects.get_or_create(
        model='main', app_label='home')

    # Create a new homepage
    main = Main.objects.create(
        title="Main",
        slug='home',
        content_type=main_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=main, is_default_site=True)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_main),
    ]

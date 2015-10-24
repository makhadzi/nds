# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151016_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsevent',
            name='repeat_annually',
        ),
    ]

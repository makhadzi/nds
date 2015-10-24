# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_newsevent_repeat_annually'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevent',
            name='province',
            field=models.CharField(blank=True, max_length=255, choices=[('limpopo', 'Limpopo'), ('gauteng', 'Gauteng'), ('mpumalanga', 'Mpumalanga'), ('northwest', 'North West'), ('kwazulunatal', 'Kwazulu Natal'), ('easterncape', 'Eastern Cape'), ('westerncape', 'Western Cape'), ('northerncape', 'Northern Cape'), ('freestate', 'Free State')]),
        ),
    ]

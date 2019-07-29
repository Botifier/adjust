# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import csv

from django.conf import settings
from django.db import migrations

def init_db(apps, schema_editor):
    SampleDataSet = apps.get_model('api', 'SampleDataSet')
    with open(os.path.join(settings.BASE_DIR, 'dataset.csv')) as csvfile:
        for row in csv.DictReader(csvfile):
            SampleDataSet.objects.create(**row)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_db, migrations.RunPython.noop),
    ] if not settings.TESTING else []

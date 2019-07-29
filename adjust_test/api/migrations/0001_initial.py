# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleDataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('channel', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=2)),
                ('os', models.CharField(max_length=32)),
                ('impressions', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('installs', models.IntegerField()),
                ('spend', models.FloatField()),
                ('revenue', models.FloatField()),
            ],
        ),
    ]

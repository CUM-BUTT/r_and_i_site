# Generated by Django 3.2.9 on 2022-01-05 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridt', '0004_auto_20220105_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 15, 59, 57, 714635)),
        ),
        migrations.AlterField(
            model_name='application',
            name='price',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=8),
        ),
    ]

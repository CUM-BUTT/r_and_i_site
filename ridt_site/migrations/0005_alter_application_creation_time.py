# Generated by Django 3.2.9 on 2021-12-30 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridt_site', '0004_auto_20211230_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 30, 13, 40, 24, 757782)),
        ),
    ]

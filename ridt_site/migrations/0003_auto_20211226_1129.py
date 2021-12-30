# Generated by Django 3.2.9 on 2021-12-26 11:29

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ridt_site', '0002_auto_20211226_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AddField(
            model_name='application',
            name='next_payment_date',
            field=models.DateField(default=datetime.date(2021, 12, 26), primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='price',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 11, 28, 6, 551276)),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(decimal_places=2, default=200, max_digits=8),
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together={('currency', 'price')},
        ),
        migrations.RemoveField(
            model_name='price',
            name='next_payment_date',
        ),
    ]

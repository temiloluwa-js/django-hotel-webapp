# Generated by Django 3.2.5 on 2022-01-28 01:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0009_auto_20220119_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_ids',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateField(default=datetime.date(2022, 1, 27)),
        ),
        migrations.AlterField(
            model_name='manager',
            name='date_created',
            field=models.DateField(default=datetime.date(2022, 1, 27)),
        ),
    ]

# Generated by Django 2.2.2 on 2019-10-22 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authanalitics', '0003_aacharacter_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='aazkillmonth',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 12, 12, 14, 47, 248948)),
        ),
        migrations.AlterField(
            model_name='aacharacter',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 12, 12, 14, 47, 247866)),
        ),
    ]
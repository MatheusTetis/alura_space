# Generated by Django 4.1.6 on 2023-02-15 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_favoritos_data_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritos',
            name='data_like',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 11, 44, 34, 593727)),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-15 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_alter_favoritos_data_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritos',
            name='data_like',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 16, 1, 23, 862803)),
        ),
    ]
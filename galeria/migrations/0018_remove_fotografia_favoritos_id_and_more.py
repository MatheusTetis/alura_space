# Generated by Django 4.1.6 on 2023-02-15 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0017_fotografia_favoritos_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='favoritos_id',
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 11, 43, 59, 164351)),
        ),
    ]
# Generated by Django 4.1.6 on 2023-02-15 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0018_remove_fotografia_favoritos_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 11, 44, 34, 592820)),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-15 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_rename_fotografia_id_favoritos_fotografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritos',
            name='data_like',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 11, 47, 38, 368614)),
        ),
    ]

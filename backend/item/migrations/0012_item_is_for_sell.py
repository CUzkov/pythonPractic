# Generated by Django 3.1 on 2020-09-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_auto_20200923_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_for_sell',
            field=models.BooleanField(default=False),
        ),
    ]

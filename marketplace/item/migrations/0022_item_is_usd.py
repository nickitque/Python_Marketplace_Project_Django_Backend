# Generated by Django 4.2.7 on 2024-03-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0021_item_is_rateable'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_usd',
            field=models.BooleanField(default=True),
        ),
    ]
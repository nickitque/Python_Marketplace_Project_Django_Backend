# Generated by Django 4.2.7 on 2023-12-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_alter_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(max_length=300),
        ),
    ]

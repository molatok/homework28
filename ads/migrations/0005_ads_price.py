# Generated by Django 4.1.5 on 2023-01-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0004_alter_categories_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="ads",
            name="price",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

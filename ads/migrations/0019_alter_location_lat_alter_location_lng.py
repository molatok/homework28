# Generated by Django 4.0.1 on 2023-02-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0018_remove_ads_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2023-02-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0015_remove_ads_user_alter_ads_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.location'),
        ),
    ]

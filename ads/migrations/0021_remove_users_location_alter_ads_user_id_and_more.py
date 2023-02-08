# Generated by Django 4.0.1 on 2023-02-08 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_directory', '0001_initial'),
        ('ads', '0020_remove_users_location_users_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='location',
        ),
        migrations.AlterField(
            model_name='ads',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_directory.users'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
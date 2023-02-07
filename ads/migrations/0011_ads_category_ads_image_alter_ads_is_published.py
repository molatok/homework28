# Generated by Django 4.0.1 on 2023-02-05 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_alter_ads_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.categories'),
        ),
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='is_published',
            field=models.CharField(max_length=5),
        ),
    ]
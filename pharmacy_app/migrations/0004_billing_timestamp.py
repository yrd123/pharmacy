# Generated by Django 3.0.7 on 2021-04-24 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0003_auto_20210424_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

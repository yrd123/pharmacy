# Generated by Django 3.0.7 on 2021-05-03 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0004_billing_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='medicines',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='pharmacy_app.Billing')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='pharmacy_app.Medicine')),
            ],
        ),
    ]

# Generated by Django 2.2.24 on 2022-08-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

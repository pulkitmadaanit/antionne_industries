# Generated by Django 3.1.3 on 2020-12-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201209_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslider',
            name='images',
            field=models.ImageField(upload_to='home_slider'),
        ),
    ]

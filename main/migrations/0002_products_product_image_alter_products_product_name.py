# Generated by Django 4.1.6 on 2023-03-11 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default=datetime.datetime(2023, 3, 11, 17, 44, 40, 229753, tzinfo=datetime.timezone.utc), upload_to='product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
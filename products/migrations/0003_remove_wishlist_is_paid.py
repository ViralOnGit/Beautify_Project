# Generated by Django 4.2.4 on 2023-08-25 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_wishlist_wishlistitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='is_paid',
        ),
    ]

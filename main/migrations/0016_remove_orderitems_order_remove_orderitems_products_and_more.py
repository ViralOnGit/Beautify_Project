# Generated by Django 4.1.7 on 2023-03-22 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='products',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
    ]
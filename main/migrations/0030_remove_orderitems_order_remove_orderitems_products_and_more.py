# Generated by Django 4.2.4 on 2023-08-21 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitems_products'),
        ('main', '0029_remove_cartitems_cart_remove_cartitems_products_and_more'),
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
        migrations.RemoveField(
            model_name='products',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
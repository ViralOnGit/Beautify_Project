# Generated by Django 4.2.4 on 2023-08-18 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_remove_userdata_username_alter_products_seller_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='products',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-14 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(choices=[('MAKEUP', 'MakeUp'), ('HAIR', 'HairCare'), ('LIPS', 'LipsCare'), ('EYE', 'EyeShadow'), ('NAIL', 'Nails'), ('FOOT', 'FootCare'), ('FACE', 'FaceProducts')], max_length=30, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('product_image', models.ImageField(default=None, null=True, upload_to='product')),
            ],
        ),
    ]
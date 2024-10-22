# Generated by Django 5.0.3 on 2024-10-20 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0010_alter_products_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('Cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gold.products')),
                ('Cart_image', models.ImageField(upload_to='media/cart')),
                ('Cart_name', models.CharField(max_length=255)),
                ('Cart_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Cart_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='media/products'),
        ),
    ]

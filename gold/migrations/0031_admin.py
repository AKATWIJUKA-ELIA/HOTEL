# Generated by Django 5.0.3 on 2024-11-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0030_remove_products_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
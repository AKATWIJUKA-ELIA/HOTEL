# Generated by Django 5.0.3 on 2024-10-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0013_alter_cart_cart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_image',
            field=models.ImageField(upload_to='cart/'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-11-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0027_alter_cart_cart_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_amount',
            field=models.IntegerField(default=1),
        ),
    ]
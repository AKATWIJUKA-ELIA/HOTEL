# Generated by Django 5.0.3 on 2024-10-30 06:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0021_alter_cart_cart_id_alter_cart_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gold.products'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

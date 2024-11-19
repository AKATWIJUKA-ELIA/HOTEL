# Generated by Django 5.0.3 on 2024-10-23 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0019_alter_cart_cart_amount_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
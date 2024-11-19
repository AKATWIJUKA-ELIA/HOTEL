# Generated by Django 5.0.3 on 2024-11-18 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0032_remove_cart_cart_amount_remove_cart_cart_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='customer_id',
            new_name='order_user',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Total_cost',
            new_name='total_amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Order_date',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
        migrations.AddField(
            model_name='orders',
            name='cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='gold.cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_address',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-10-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0007_alter_customers_managers_alter_customers_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.AutoField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-12-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0037_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='reset_token',
            field=models.CharField(blank=True, null=True, default=None, max_length=255),
        ),
    ]

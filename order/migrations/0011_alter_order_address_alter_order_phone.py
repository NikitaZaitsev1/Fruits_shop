# Generated by Django 4.0.5 on 2022-07-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_rename_processing_order_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]

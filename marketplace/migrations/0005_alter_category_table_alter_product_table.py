# Generated by Django 4.0.5 on 2022-07-11 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
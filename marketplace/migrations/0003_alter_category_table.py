# Generated by Django 4.0.5 on 2022-07-11 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
    ]

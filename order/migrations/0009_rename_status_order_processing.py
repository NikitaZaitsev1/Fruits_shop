# Generated by Django 4.0.5 on 2022-07-21 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='processing',
        ),
    ]
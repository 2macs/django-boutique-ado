# Generated by Django 3.2 on 2023-04-12 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-15 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField('product', 'product', 'name'),
    ]

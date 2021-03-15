# Generated by Django 3.1.7 on 2021-03-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=150, verbose_name='producto')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='descripción')),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/products/', verbose_name='imagen')),
                ('is_top', models.BooleanField(default=True, verbose_name='producto top')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['product'],
            },
        ),
    ]

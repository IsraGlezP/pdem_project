# Generated by Django 3.1.7 on 2021-03-29 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='descripción')),
                ('photo_main', models.ImageField(blank=True, upload_to='categories/', verbose_name='imagen')),
                ('is_published', models.BooleanField(default=True, verbose_name='publicar')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad_disponible',
            field=models.IntegerField(),
        ),
    ]

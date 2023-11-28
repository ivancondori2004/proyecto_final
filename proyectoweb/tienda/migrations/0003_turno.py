# Generated by Django 4.2.5 on 2023-11-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_producto_cantidad_disponible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_turno', models.TimeField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.empleado')),
            ],
        ),
    ]

# Generated by Django 3.1.14 on 2023-12-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0021_auto_20231206_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='tipo_tarifa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.tarifa'),
        ),
    ]
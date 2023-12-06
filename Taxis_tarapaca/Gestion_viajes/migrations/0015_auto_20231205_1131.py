# Generated by Django 3.1.14 on 2023-12-05 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0014_auto_20231205_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='reserva',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.reserva'),
        ),
        migrations.AddField(
            model_name='reclamo',
            name='viaje',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.viaje'),
        ),
    ]
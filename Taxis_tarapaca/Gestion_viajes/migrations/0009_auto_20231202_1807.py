# Generated by Django 3.1.14 on 2023-12-02 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0008_auto_20231202_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='ciudad_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserva_cidestino', to='Gestion_viajes.ciudad'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='comuna_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserva_codestino', to='Gestion_viajes.comuna'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='region_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserva_rdestino', to='Gestion_viajes.region'),
        ),
    ]
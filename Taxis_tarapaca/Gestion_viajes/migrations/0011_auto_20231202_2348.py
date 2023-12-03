# Generated by Django 3.1.14 on 2023-12-03 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0010_ruta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='ciudad',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.ciudad'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='ciudad_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ruta_cidestino', to='Gestion_viajes.ciudad'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='comuna',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.comuna'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='comuna_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ruta_codestino', to='Gestion_viajes.comuna'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.region'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='region_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ruta_rdestino', to='Gestion_viajes.region'),
        ),
    ]

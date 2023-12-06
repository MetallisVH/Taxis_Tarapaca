# Generated by Django 3.1.14 on 2023-12-05 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0015_auto_20231205_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='contacto',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='reclamo',
            name='prefijo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.prefijospais'),
        ),
        migrations.AddField(
            model_name='reclamo',
            name='tipo_contacto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.medioscontacto'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='autor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.usuario'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='reserva',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.reserva'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='tipo_reclamo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.tiposreclamo'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='viaje',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.viaje'),
        ),
    ]
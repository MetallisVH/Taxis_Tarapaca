# Generated by Django 3.1.14 on 2024-01-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_viajes', '0025_auto_20240102_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='reservante',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_viajes.usuario'),
        ),
    ]
from django.db import models

class Geolocalizaciones(models.Model):
    id = models.AutoField(primary_key=True, null=True, blank= True)
    latitud_ubicacion = models.DecimalField(null=True, blank= True)
    longitud_ubicacion = models.DecimalField(null=True, blank= True)
    fecha = models.DateField(null=True, blank= True)
    hora = models.TimeField(null=True, blank= True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
class Viajes(models.Model):
    id = models.AutoField(primary_key=True,null=True, blank= True) # este se usara como FK
    observacion = models.TextField(null=True, blank= True)
    anulado = models.BooleanField(null=True, blank= True)
    motivo_anulado = models.CharField(max_length=255, blank=True, null=True)
    hora_inicio = models.DateTimeField(null=True, blank= True)
    hora_termino = models.DateTimeField(blank=True, null=True)
    tipo_viaje = models.CharField(max_length=50)
    cantidad_pasajeros = models.IntegerField(null=True, blank= True)
    cod_viaje = models.CharField(max_length=20, unique=True)
    fecha = models.DateField(null=True, blank= True)
    latitud_origen = models.DecimalField(null=True, blank= True)
    longitud_origen = models.DecimalField(null=True, blank= True)
    latitud_destino = models.DecimalField(null=True, blank= True)
    longitud_destino = models.DecimalField(null=True, blank= True)
    origen = models.CharField(max_length=255, blank=True, null=True)
    tipo_origen = models.CharField(max_length=255, blank=True, null=True) #este sera un FK
    deleted_at = models.DateTimeField(blank=True, null=True)
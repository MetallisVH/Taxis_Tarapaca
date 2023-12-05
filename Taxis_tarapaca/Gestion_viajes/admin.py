from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Viaje)
admin.site.register(Geolocalizacion)
admin.site.register(TiposCalle)
admin.site.register(PrefijosPais)
admin.site.register(Pais)
admin.site.register(Log)
admin.site.register(Reserva)
admin.site.register(TiposTarifa)
admin.site.register(Tarifa)
admin.site.register(MediosContacto)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Ruta)
admin.site.register(Reclamo)
admin.site.register(TiposReclamo)
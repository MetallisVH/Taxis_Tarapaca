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
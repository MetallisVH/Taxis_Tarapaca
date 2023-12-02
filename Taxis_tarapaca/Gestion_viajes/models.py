from django.db import models

class Pais(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=54,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre

class Region(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=254,blank=True,null=True)
    pais = models.ForeignKey(Pais,on_delete=models.SET_NULL,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    
class Ciudad(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=254,blank=True,null=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=254,blank=True,null=True)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.SET_NULL,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre

class MediosContacto(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=254,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre

class TiposTarifa(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    tipo = models.IntegerField(null=True,blank=True)
    nombre = models.CharField(max_length=54,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)

class Tarifa(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    tipo_tarifa = models.ForeignKey(TiposTarifa,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    monto_tarifa = models.IntegerField(null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)

class Log(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    accion = models.TextField(null=True,blank=True)
    autor = models.CharField(max_length=254,blank=True,null=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)

class PrefijosPais(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    pais = models.ForeignKey(Pais,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    numero_prefijo = models.CharField(max_length=14,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return str(self.pais) +' ('+ str(self.numero_prefijo)+')'
    
class TiposCalle(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=54,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre

class Geolocalizacion(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    latitud_ubicacion = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_ubicacion = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)

class Viaje(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    observacion = models.TextField(null=True, blank=True)
    anulado = models.BooleanField(null=True, blank=True)
    motivo_anulado = models.CharField(max_length=254, blank=True, null=True)
    hora_inicio = models.DateTimeField(null=True, blank=True)
    hora_termino = models.DateTimeField(blank=True, null=True)
    tipo_viaje = models.CharField(max_length=54)
    cantidad_pasajeros = models.IntegerField(null=True, blank=True)
    cod_viaje = models.CharField(max_length=24, unique=True)
    fecha = models.DateField(null=True, blank=True)
    latitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    origen = models.CharField(max_length=254, blank=True, null=True)
    tipo_origen = models.ForeignKey(TiposCalle,on_delete = models.SET_NULL,blank=True,null=True,default=None,related_name='viaje_torigen')
    destino = models.CharField(max_length=254, blank=True, null=True)
    tipo_destino = models.ForeignKey(TiposCalle,on_delete = models.SET_NULL,blank=True,null=True,default=None,related_name='viaje_tdestino')
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=54,null=True,blank=True)
    run = models.IntegerField(null=True,blank=True,unique=True)
    dv = models.CharField(max_length=1,null=True,blank=True)
    apellido_p = models.CharField(max_length=54,null=True,blank=True)
    apellido_m = models.CharField(max_length=54,null=True,blank=True)
    genero = models.CharField(max_length=254,null=True,blank=True)
    nombre_usu = models.CharField(max_length=54,null=True,blank=True,unique=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    edad = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True,unique=True)
    prefijo = models.ForeignKey(PrefijosPais,on_delete=models.SET_NULL,null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    password = models.TextField(null=True,blank=True)
    tipo_calle = models.ForeignKey(TiposCalle,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    direccion = models.CharField(max_length=254,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    
class Reserva(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    fecha_reserva = models.DateTimeField(null=True,blank=True)
    origen = models.CharField(max_length=254,null=True,blank=True)
    numero_origen = models.IntegerField(null=True,blank=True)
    tipo_origen = models.ForeignKey(TiposCalle,on_delete = models.SET_NULL,blank=True,null=True,default=None,related_name='reserva_torigen')
    destino = models.CharField(max_length=54,null=True,blank=True)
    numero_destino = models.IntegerField(null=True,blank=True)
    tipo_destino = models.ForeignKey(TiposCalle,on_delete = models.SET_NULL,blank=True,null=True,default=None,related_name='reserva_tdestino')
    cantidad_pasajeros = models.IntegerField(null=True,blank=True)
    anulado = models.IntegerField(null=True,blank=True)
    observacion = models.TextField(null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    comuna = models.ForeignKey(Comuna,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    region_destino = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True,blank=True,default=None,related_name='reserva_rdestino')
    ciudad_destino = models.ForeignKey(Ciudad,on_delete=models.SET_NULL,null=True,blank=True,default=None,related_name='reserva_cidestino')
    comuna_destino = models.ForeignKey(Comuna,on_delete=models.SET_NULL,null=True,blank=True,default=None,related_name='reserva_codestino')
    tarifa = models.ForeignKey(Tarifa,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    latitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    motivo_anulacion = models.TextField(null=True,blank=True)
    fecha_anulacion = models.DateTimeField(null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)
    estado_reserva = models.IntegerField(null=True,blank=True)
    medio_contacto = models.ForeignKey(MediosContacto,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    prefijo = models.ForeignKey(PrefijosPais,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    contacto = models.CharField(max_length=54,null=True,blank=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
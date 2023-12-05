from django.shortcuts import render, redirect
from .forms import *
from datetime import datetime
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.

def check_ciudades(request):
    
    region_seleccionada = request.GET.get('region',None)
    
    ciudades = Ciudad.objects.filter(deleted_at=None)
    
    ciudades_seleccion = []
    
    for ciudad in ciudades:
        if int(ciudad.region.id) == int(region_seleccionada):
            
            ciudades_seleccion.append(ciudad)
    
    ciudades_json = serialize('json', ciudades_seleccion)
    
    return JsonResponse(ciudades_json, safe=False)

def check_comunas(request):
    
    ciudad_seleccionada = request.GET.get('ciudad',None)
    
    comunas = Comuna.objects.filter(deleted_at=None)
    
    comunas_seleccion = []
    
    for comuna in comunas:
        if int(comuna.ciudad.id) == int(ciudad_seleccionada):
            
            comunas_seleccion.append(comuna)
            
    comunas_json = serialize('json',comunas_seleccion)
    
    return JsonResponse(comunas_json,safe=False)

def check_usuario_login(request):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        
        logged = 1 
        
        return JsonResponse({'logeado':logged})
    
    else:
        
        logged = 0
        
        return JsonResponse({'logeado':logged})
    

def home_login_usuario(request):
    return render(request, 'Gestion_viajes/home_login_usuario.html')

def home_registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            
            nuevo_usu = form.save(commit=False)
            
            genero = request.POST.get('genero',None)
            
            if genero is not None and genero == 'otro':
                
                genero = request.POST.get('otro_genero')
                
            fecha_nacimiento = nuevo_usu.fecha_nacimiento

            fecha_actual = datetime.now().date()

            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            
            nuevo_usu.created_at = fecha_actual
            
            nuevo_usu.edad = edad
            
            nuevo_usu.genero = genero
            
            nuevo_usu.password = make_password(nuevo_usu.password)
            
            nuevo_usu.save()
            
            return render(request,'Gestion_viajes/home_registro_usuario_exito.html')
            
    else:
        form = UsuarioForm()
        
        context = {'form':form}
        
        return render(request,'Gestion_viajes/home_registro_usuario.html',context)       

def home_autenticar_usuario(request):
    if request.method == 'POST':
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        try:
            usuario = Usuario.objects.get(email=username)
        except:
            usuario = None
        
        if usuario is None:
            try:
                usuario = Usuario.objects.get(nombre_usu=username)
            except:
                usuario = None
                
        if usuario is not None and check_password(password,usuario.password):
            
            request.session['user'] = usuario.id
            
            return redirect('http://localhost:8000/es/Usrs/')     
        else:
            
            err_m = 'Credenciales incorrectas intente nuevamente.'
            
            context = {'error':err_m}
            
            return render(request,'Gestion_viajes/home_login_usuario.html',context)
    else:
        
        return redirect('home_login_usuario')
    
def usr_solicitud_reserva(request):
    
    usuario = request.session.get('user',None)
    
    if request.method == 'POST':
        
        form = ReservaUsuarioForm(request.POST)
        
        if form.is_valid() and usuario is not None:
            
            reserva_usuario = form.save(commit=False)
            
            reserva_usuario.estado_reserva = 0
            
            reserva_usuario.created_at = datetime.now()
            
            reserva_usuario.save()
            
            return render(request,'Gestion_viajes/usr_solicitud_reserva_exito.html')
        
        else:
            
            error_m = 'Ocurrio un error en la solicitud, intente nuevamente.'
            
            context = {'error':error_m}
            
            return render(request,'Gestion_viajes/usr_solicitud_reserva.html',context)
            
            
    else:
        
        if usuario is not None:
        
            form = ReservaUsuarioForm()
            
            context = {'form':form}
            
            return render(request,'Gestion_viajes/usr_solicitud_reserva.html',context)
        
        else:
            
            return render(request,'Gestion_viajes/err_frb.html')
        
def usr_busqueda_reserva(request):
    
    usuario = request.session.get('user')
    
    if request.method == 'POST':
        
        form = RutaForm(request.POST)
        
        if form.is_valid() and form is not None:
        
            if usuario is not None:
                
                context = {'form':form}
                
                ruta_vehiculo = form.save(commit=False)
                
                fecha_ruta = ruta_vehiculo.fecha_viaje
                
                region_origen = ruta_vehiculo.region
                
                ciudad_origen = ruta_vehiculo.ciudad
                
                comuna_origen = ruta_vehiculo.comuna
                
                region_destino = ruta_vehiculo.region_destino
                
                ciudad_destino = ruta_vehiculo.ciudad_destino
                
                comuna_destino = ruta_vehiculo.comuna_destino
                
                print(region_origen)
                print(region_destino)
                
                if fecha_ruta is not None:
                    try:
                        rutas_region = Ruta.objects.filter(region=region_origen,region_destino=region_destino,fecha_viaje=fecha_ruta,deleted_at=None)
                    
                        if rutas_region is not None:
                    
                            context = {'form':form,'rutas':rutas_region}
                    except:
                        rutas_region = None
                
                    if ciudad_origen is not None and ciudad_destino is not None:
                    
                        try:
                            rutas_ciudad = Ruta.objects.filter(ciudad=ciudad_origen,ciudad_destino=ciudad_destino,fecha_viaje=fecha_ruta,deleted_at=None)
                        
                            if rutas_ciudad is not None:
                    
                                context = {'form':form,'rutas':rutas_ciudad}
                        except:
                            rutas_ciudad = None
                    
                    if comuna_origen is not None and comuna_destino is not None:
                    
                        try:
                            rutas_comuna = Ruta.objects.filter(comuna=comuna_origen,comuna_destino=comuna_destino,fecha_viaje=fecha_ruta,deleted_at=None)
                        
                            if rutas_comuna is not None:
                    
                                context = {'form':form,'rutas':rutas_comuna}
                        except:
                            rutas_comuna = None
                else:
                    try:
                        rutas_region = Ruta.objects.filter(region=region_origen,region_destino=region_destino,deleted_at=None)
                        
                        if rutas_region is not None:
                        
                            context = {'form':form,'rutas':rutas_region}
                    except:
                        rutas_region = None
                    
                    if ciudad_origen is not None and ciudad_destino is not None:
                        
                        try:
                            rutas_ciudad = Ruta.objects.filter(ciudad=ciudad_origen,ciudad_destino=ciudad_destino,deleted_at=None)
                            
                            if rutas_ciudad is not None:
                        
                                context = {'form':form,'rutas':rutas_ciudad}
                        except:
                            rutas_ciudad = None
                        
                    if comuna_origen is not None and comuna_destino is not None:
                        
                        try:
                            rutas_comuna = Ruta.objects.filter(comuna=comuna_origen,comuna_destino=comuna_destino,deleted_at=None)
                            
                            if rutas_comuna is not None:
                        
                                context = {'form':form,'rutas':rutas_comuna}
                        except:
                            rutas_comuna = None
                    
                    
                print(context)
                
                return render(request,'Gestion_viajes/usr_busqueda_reserva.html',context)
            
            else:
                
                form = RutaForm()
        
                rutas = Ruta.objects.filter(deleted_at=None)
                
                context = {'rutas':rutas,'form':form}
                
                return render(request,'Gestion_viajes/usr_busqueda_reserva.html',context)
        
    else:
        
        form = RutaForm()
        
        rutas = Ruta.objects.filter(deleted_at=None)
        
        context = {'rutas':rutas,'form':form}
        
        return render(request,'Gestion_viajes/usr_busqueda_reserva.html',context)
    
def usr_reclamacion(request):
    
    usuario = request.session.get('user')
    
    if usuario is not None:
    
        if request.method == 'POST':
            
            usuario_sesion = Usuario.objects.get(id=usuario)
            
            form = ReclamoForm(request.POST)
            
            if form.is_valid():
                
                context = {}
                
                reclamo_usuario = form.save(commit=False)
                
                reclamo_usuario.autor = usuario_sesion
                
                reclamo_usuario.estado = 0
                
                reclamo_usuario.created_at = datetime.now()
                
                viaje = request.POST.get('cod_viaje',None)
                
                if viaje == '':
                    viaje = None
                
                reserva = request.POST.get('cod_reserva',None)
                
                if reserva == '':
                    reserva = None
                
                print(viaje)
                
                if viaje is not None:
                    
                    cod_viaje = viaje
                    
                    try:
                    
                        reclamo_usuario.viaje = Viaje.objects.get(id=cod_viaje)
                        
                    except:
                        
                        reclamo_usuario.viaje = None
                        
                        err_v = "No se encontro el viaje especificado, porfavor consulte con la empresa: +56971208446"
                        
                        context = {'error':err_v}
                        
                        return render(request,'Gestion_viajes/usr_reclamos_fail.html',context)
                    
                print(reserva)
                    
                if reserva is not None:
                    
                    cod_reserva = reserva
                    
                    print(cod_reserva)
                    print(type(cod_reserva))
                    
                    try:
                        
                        reclamo_usuario.reserva = Reserva.objects.get(id=cod_reserva)
                        
                    except:
                        
                        reclamo_usuario.reserva = None
                        
                        err_r = "No se encontro la reserva especificada, porfavor consulte con la empresa: +56971208446"
                        
                        context = {'error':err_r}
                        
                        return render(request,'Gestion_viajes/usr_reclamos_fail.html',context)
                
                reclamo_usuario.save()
                
                return render(request,'Gestion_viajes/usr_reclamos_exito.html',context)
            
            else:
                
                print(form.errors)
                
                form = ReclamoForm()
                
                error = "Ocurrio un error con el ingreso de la reclamacion, intente nuevamente"
            
                context = {'form':form,'error':error}
                
                return render(request,'Gestion_viajes/usr_reclamos.html',context)
            
        else:
            
            form = ReclamoForm()
            
            context = {'form':form}
            
            return render(request,'Gestion_viajes/usr_reclamos.html',context)
        
    else:
        
        return render(request,'Gestion_viajes/err_frb.html')
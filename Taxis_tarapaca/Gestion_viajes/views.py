from django.shortcuts import render, redirect
from .forms import *
from datetime import datetime
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.

def get_monto_tarifa(request):
    tipo_tarifa = request.GET.get('tipo_tarifa')
    
    try:

        tarifa = Tarifa.objects.get(id=tipo_tarifa)
    
    except:
        
        tarifa = None
    
    if tarifa is not None:
        monto = tarifa.monto_tarifa
    else:
        monto = 0
    
    return JsonResponse({'monto': monto})

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
            
            nuevo_usu.tipo = 0
            
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
                
                if viaje is not None:
                    
                    cod_viaje = viaje
                    
                    try:
                    
                        reclamo_usuario.viaje = Viaje.objects.get(id=cod_viaje)
                        
                    except:
                        
                        reclamo_usuario.viaje = None
                        
                        err_v = "No se encontro el viaje especificado, porfavor consulte con la empresa: +56971208446"
                        
                        context = {'error':err_v}
                        
                        return render(request,'Gestion_viajes/usr_reclamos_fail.html',context)
                    
                if reserva is not None:
                    
                    cod_reserva = reserva
                    
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
    
def scr_registrar_taxista(request):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        try:
            
            secretaria = Secretaria.objects.get(id=usuario)
        
        except:
            
            secretaria = None
            
        if request.method == 'POST':
            
            form = TaxistaForm(request.POST)
            
            if form.is_valid():
                
                nuevo_taxista = form.save(commit=False)
                
                genero = request.POST.get('genero',None)
                
                if genero is not None and genero == 'otro':
                
                    genero = request.POST.get('otro_genero')
                
                nuevo_taxista.secretaria_encargada = secretaria
                
                nuevo_taxista.estado = 0
                
                nuevo_taxista.genero = genero
                
                nuevo_taxista.created_at = datetime.now()
                
                nuevo_taxista.save()
                
                return render(request,'Gestion_viajes/scr_registrar_taxista_exito.html')
        
        else:
            
            form = TaxistaForm()
            
            context = {'form':form}
            
            return render(request,'Gestion_viajes/scr_registrar_taxista.html',context)
        
    else:
        
        return render(request,'Gestion_viajes/err_frb.html')
    
def scr_mostrar_taxistas(request):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        
        form = BusquedaTaxistaForm()
                
        try:
            
            secretaria = Secretaria.objects.get(id=usuario)
            
        except:
            
            secretaria = None
            
        try:
            
            taxistas = Taxista.objects.filter(secretaria_encargada=secretaria,deleted_at=None)
            
        except:
            
            taxistas = None
            
        context = {'taxistas':taxistas,'busqueda_form':form}
        
        return render(request,'Gestion_viajes/scr_admin_taxistas.html',context)
    
def scr_buscar_taxistas(request):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        
        if request.method == 'GET':
    
            form = BusquedaTaxistaForm(request.GET)
            taxistas = None

            if form.is_valid():
                
                busqueda = form.cleaned_data['busqueda']
                
                print(busqueda)
                # Realiza la búsqueda en base al campo que desees
                
                context = {'busqueda_form': form}
                
                try:
                    taxistas = Taxista.objects.filter(nombre__icontains=busqueda)
                    
                    context = {'busqueda_form': form,'taxistas': taxistas}
                    
                except:
                    taxistas = None
                
                if taxistas == None or not taxistas :
                    try:
                        taxistas = Taxista.objects.filter(run=busqueda)
                        
                        context = {'busqueda_form': form,'taxistas': taxistas}
                        
                    except:
                        taxistas = None
                
                if taxistas == None or not taxistas :
                    
                    print(taxistas)
                    try:
                        
                        taxistas = Taxista.objects.filter(id=busqueda)
                        
                        context = {'busqueda_form': form,'taxistas': taxistas}
                        
                    except:
                        
                        taxistas= None
                
                if taxistas == None:
                    
                    err = "No se encontro a ningun taxista con la busqueda solicitada."
                    
                    context = {'busqueda_form': form,'error':err}

                return render(request, 'Gestion_viajes/scr_admin_taxistas.html',context)
            
            else:
                
                err = "No se encontro a ningun taxista con la busqueda solicitada."
                    
                context = {'busqueda_form': form,'error':err}
                
                return render(request, 'Gestion_viajes/scr_admin_taxistas.html',context)
        else:
            
            form = BusquedaTaxistaForm()
            
            context = {'busqueda_form':form}
            
            return render(request,'Gestion_viajes/scr_admin_taxistas.html',context)
        
    else:
        
        return render(request,'Gestion_viajes/err_frb.html')
    
def scr_ver_datos_taxista(request,id_taxista):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        try:
            
            taxista = Taxista.objects.get(id=id_taxista,deleted_at=None)
            
            context = {'taxista':taxista}
            
            return render(request,'Gestion_viajes/scr_ver_datos_taxista.html',context)
            
        except:
            
            taxista = None
            
            err = "Ocurrio un error inesperado: no se encontro al taxista."
            
            context = {'error':err}
            
            return render(request,'Gestion_viajes/scr_ver_datos_taxista.html',context)
    else:
        
        return render(request,'Gestion_viajes/err_frb.html')

def scr_editar_taxista(request,id_taxista):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        
        if request.method == 'POST':
            
            taxista = Taxista.objects.get(id=id_taxista)
        
            form = EditarTaxistaForm(request.POST, instance=taxista)
            
            if form.is_valid():
            
                taxista_editado = form.save(commit=False)
                
                taxista_editado.save()
                
                context = {'taxista':taxista}
                
                return render(request,'Gestion_viajes/scr_ver_datos_taxista.html',context)
            
            else:
                
                taxista = Taxista.objects.get(id=id_taxista)
                
                context = {'taxista':taxista}
                
                print(form.errors)
                
                return render(request,'Gestion_viajes/scr_ver_datos_taxista.html',context)
            
            
        
        else:
            
            taxista = Taxista.objects.get(id=id_taxista,deleted_at=None)
            
            context = {'taxista':taxista}
            
            return render(request,'Gestion_viajes/scr_edicion_taxista.html',context)
    
def scr_ingresar_ruta(request):
    
    usuario = request.session.get('user',None)
    
    if usuario is not None:
        
        if request.method == 'POST':
            
            form = IngresarRutaForm(request.POST)
            
            if form.is_valid():
                
                nueva_ruta = form.save(commit=False)
                
                nueva_ruta.created_at = datetime.now()
                
                nueva_ruta.save()
                
                return render(request,'Gestion_viajes/scr_registrar_ruta_exito.html')
            
        else:
            
            form = IngresarRutaForm()
            
            context = {'form':form}
            
            return render(request,'Gestion_viajes/scr_registrar_ruta.html',context)
        
    else:
        
        return render(request,'Gestion_viajes/err_frb.html')
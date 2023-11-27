from django.shortcuts import render
#hay que importar tarifas igual

# Create your views here.
def usr_mostrar_tarifas(request):
    #aqui va la logica para mostrar las tarifas
    #ejemplo
    
    tarifas = Tarifas.objects.filter(deleted_at=None) #para mostrar todas
    
    return render(request,'gestion_viajes/tu_html.html')
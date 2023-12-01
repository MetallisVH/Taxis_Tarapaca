from django.shortcuts import render
#hay que importar tarifas igual

# Create your views here.

def usr_home_login(request):
    return render(request, 'Gestion_viajes/usr_home_login.html')

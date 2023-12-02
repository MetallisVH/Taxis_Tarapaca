from django.urls import path
from . import views

urlpatterns = [
    path("home_lgn/",views.home_login_usuario,name='home_login_usuario'),
    path('home_rgs/',views.home_registrar_usuario,name='home_registrar_usuario'),
    path('home_uauth/',views.home_autenticar_usuario,name='home_autenticar_usuario'),
    path('usr_slrs/',views.usr_solicitud_reserva,name='usr_solicitud_reserva'),
]
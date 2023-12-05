from django.urls import path
from . import views

urlpatterns = [
    path("auth_usr/",views.check_usuario_login,name='check_usuario_login'),
    path("chk_comn/",views.check_comunas,name='check_comunas'),
    path("chk_ciud/",views.check_ciudades,name='check_ciudades'),
    path("home_lgn/",views.home_login_usuario,name='home_login_usuario'),
    path("home_rgs/",views.home_registrar_usuario,name='home_registrar_usuario'),
    path("home_uauth/",views.home_autenticar_usuario,name='home_autenticar_usuario'),
    path("usr_slrs/",views.usr_solicitud_reserva,name='usr_solicitud_reserva'),
    path("usr_srap/",views.usr_busqueda_reserva,name='usr_busqueda_reserva'),
    path("usr_crec/",views.usr_reclamacion,name='usr_reclamacion'),
]
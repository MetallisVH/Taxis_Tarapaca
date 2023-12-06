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
    path("scr_rtax/",views.scr_registrar_taxista,name='scr_registrar_taxista'),
    path("scr_admtax/",views.scr_mostrar_taxistas,name='scr_mostrar_taxistas'),
    path("scr_btax/",views.scr_buscar_taxistas,name='scr_buscar_taxistas'),
    path("scr_vtax/<int:id_taxista>/",views.scr_ver_datos_taxista,name='scr_ver_datos_taxista'),
    path("scr_etax/<int:id_taxista>/",views.scr_editar_taxista,name="scr_editar_taxista")
]
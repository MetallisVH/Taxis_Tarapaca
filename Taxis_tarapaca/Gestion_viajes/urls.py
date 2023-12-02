from django.urls import path
from . import views

urlpatterns = [
    path("home_lgn/",views.home_login_usuario,name='home_login_usuario'),
    path('home_rgs/',views.home_registrar_usuario,name='home_registrar_usuario'),
]
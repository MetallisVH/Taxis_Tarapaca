from django.urls import path
from . import views

urlpatterns = [
    path("usr_home_lgn/",views.usr_home_login,name='usr_home_login'),
]
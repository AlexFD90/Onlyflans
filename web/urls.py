from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index_web'),
    path('about', views.about, name='about_web'),
    path('welcome', views.welcome, name='welcome_web'),
    path('contact', views.contact, name='contact_web'),
    path('exito', views.exito, name='exito_web'),
    path('vegan', views.vegan, name='vegan_web'),
    path('muffins', views.muffins, name='muffins_web'),
    path('sucursal', views.sucursal, name='sucursal_web'),
]
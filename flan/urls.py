from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index_flan'),
    path('crearflan', views.crearflan, name='crearflan_flan'),
    path('crearmuffin', views.crearmuffin, name='crearmuffin'),
    path('exito_product', views.exito_product, name='exito_product'),

]
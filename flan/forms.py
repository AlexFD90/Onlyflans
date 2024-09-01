from django import forms

class FlanFormModelForm(forms.Form):
    name = forms.CharField(max_length = 64, label='Nombre')
    description = forms.CharField(label='Descripcion')
    image_url = forms.URLField(label='URL Imagen')
    short_name = forms.SlugField(label='Nombre corto')
    is_private = forms.BooleanField(label='Es Privado')
    vegan = forms.BooleanField(label='Vegano')  

class MuffinFormModelForm(forms.Form):
    name = forms.CharField(max_length = 64, label='Nombre')
    description = forms.CharField(label='Descripcion')
    image_url = forms.URLField(label='URL Imagen')
    short_name = forms.SlugField(label='Nombre corto')
    is_private = forms.BooleanField(label='Es Privado')
    vegan = forms.BooleanField(label='Vegano') 
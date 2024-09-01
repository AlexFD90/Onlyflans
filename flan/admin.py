from django.contrib import admin
from .models import FlanForm, ContactForm, Muffins, Sucursal
# Register your models here.

class FlanAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'image_url', 'short_name', 'is_private', 'vegan']

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name','customer_email','message']

class MuffinsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'image_url', 'short_name', 'is_private', 'vegan']    

class SucursalAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'address', 'image_address']  

admin.site.register(FlanForm,FlanAdmin)
admin.site.register(ContactForm,ContactFormAdmin)
admin.site.register(Muffins, MuffinsAdmin)
admin.site.register(Sucursal, SucursalAdmin)
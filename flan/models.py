from django.db import models
from django.forms import ModelForm

# Create your models here.

class FlanForm(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    image_url = models.URLField()
    short_name = models.SlugField()
    is_private = models.BooleanField()
    vegan = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class FlanFormModelForm(ModelForm):
    class Meta:
        modelo = FlanForm()
        campos = ['name','description','image_url','short_name','is_private','vegan']

        def __str__(self) -> str:
            return self.modelo    
        
class Muffins(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    image_url = models.URLField()
    short_name = models.SlugField()
    is_private = models.BooleanField()
    vegan = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class MuffinformModelForm(ModelForm):
    class Meta:
        modelo = Muffins()
        campos = ['name','description','image_url','short_name','is_private','vegan']

        def __str__(self) -> str:
            return self.modelo 

class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length = 64)
    message = models.TextField()

    def __str__(self) -> str:
        return self.customer_name
    
class ContactFormModelForm(ModelForm):
    class Meta:
        modelo = ContactForm()
        campos = ['customer_email','customer_name','message']

        def __str__(self) -> str:
            return self.modelo
    
    
class Sucursal(models.Model):
    name = models.CharField(max_length = 64)
    address = models.TextField()
    image_address = models.URLField(max_length = 200)
    
    def __str__(self) -> str:
        return self.name
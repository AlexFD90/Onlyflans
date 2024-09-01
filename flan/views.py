from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flan.models import FlanForm, ContactForm, Muffins, Sucursal
from django.contrib.auth.decorators import login_required
from .forms import FlanFormModelForm, MuffinFormModelForm



# Create your views here.

def index(request):
    flans = FlanForm.objects.all()
    context = {'flans':flans}
    return render(request, 'flan/index.html',context)

def crearflan(request):
    if request.method=='POST':
        form = FlanFormModelForm(request.POST)
        if form.is_valid():
            crearflan_form = FlanForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito_product') 
    else:
        form = FlanFormModelForm() 
    
    return render(request,'flan/create_flan.html',{'form':form})

def crearmuffin(request):
    if request.method=='POST':
        form = MuffinFormModelForm(request.POST)
        if form.is_valid():
            crearmuffin_form = Muffins.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito_product') 
    else:
        form = MuffinFormModelForm() 
    
    return render(request,'flan/create_muffin.html',{'form':form})

def exito_product(request):
    return render(request, 'flan/exito_product.html')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flan.models import FlanForm, ContactForm, Muffins, Sucursal
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    flans = FlanForm.objects.all()
    flans_public = FlanForm.objects.filter(is_private = False)   
    context = {'flans':flans}
    context_public = {'flans':flans_public}
    return render(request, 'web/index.html', context_public)

def about(request):
    return render(request, 'web/about.html')

@login_required
def welcome(request):
    flans_private = FlanForm.objects.filter(is_private = True)
    context = {'flans':flans_private}   
    return render(request, 'web/welcome.html',context)

def contact(request):
    if request.method =='POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito')
    else:
        form = ContactFormModelForm() 
            
    return render(request, 'web/contact.html', {'form':form})

def exito(request):
    return render(request, 'web/exito.html')

def vegan(request):
    vegan = FlanForm.objects.filter(vegan = True) 
    context = {'flans':vegan}
    return render(request, 'web/vegan.html',context)

def muffins(request):
    muffins = Muffins.objects.all()
    context = {'muffins':muffins}
    return render(request, 'web/muffins.html',context)

def sucursal(request):
    sucursal = Sucursal.objects.all()
    context = {'sucursal':sucursal}
    return render(request, 'web/sucursal.html',context)
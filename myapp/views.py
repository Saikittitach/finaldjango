from django.shortcuts import render
from .models import Datatabase
from .forms import databaseform
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def datatable(request):
    # products  = Product.objects.all()
    form = Datatabase.objects.all()

    if request.method=="POST":
    
        filled_form = databaseform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        form = databaseform()
    return render(request, 'frontend/datatable.html',{'form':form})


def contact(request):
    return render(request, 'frontend/contact.html')


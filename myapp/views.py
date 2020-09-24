from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def datatable(request):
    products  = Product.objects.all()
    return render(request, 'frontend/datatable.html',{'products': products})

def contact(request):
    return render(request, 'frontend/contact.html')


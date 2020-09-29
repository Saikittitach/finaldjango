from django.shortcuts import render
from .models import Product
from .forms import NameForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def datatable(request):
    # products  = Product.objects.all()
    form = NameForm.objects.all()
    if request.method=="POST":
        
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        print(firstname, lastname, email, phone,desc)
    return render(request, 'frontend/datatable.html',{'form': form}) 

def contact(request):
    return render(request, 'frontend/contact.html')


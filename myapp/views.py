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
    # if request.method=="POST":
        
    #     firstname= request.POST['firstname']
    #     lastname= request.POST['lastname']
    #     email= request.POST['email']
    #     phone= request.POST['phone']
    #     desc= request.POST['desc']
    #     print(firstname, lastname, email, phone,desc)
    # return render(request, 'frontend/datatable.html',{'database': database}) 

    # form = databaseform(request.POST or None)
    # if form.is_valid():
        
    #     form.save()
        
    # context={'form':form}

    # return render(request, 'frontend/datatable.html',context)

    if request.method=="POST":
    
        filled_form = databaseform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
    form = databaseform()
    return render(request, 'frontend/datatable.html',{'order':form})


    # form = databaseform(request.POST or None)
    # context = {'form':form}
    # if form.is_valid():
    #     firstname = form.cleaned_data['firstname']
    #     context.update({'firstname':firstname})
    #     lastname = form.cleaned_data['lastname']
    #     context.update({'lastname':lastname})
    #     email = form.cleaned_data['email']
    #     context.update({'email':email})
    #     desc = form.cleaned_data['desc']
    #     context.update({'desc':desc})

    # return render(request,'frontend/datatable.html' , context)


def contact(request):
    return render(request, 'frontend/contact.html')


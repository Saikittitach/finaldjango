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

# def datatable_submit(request):
#     print("form submit")
#     return render(request, 'frontend/database.html')

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'datatable.html', {'form': form})

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Product()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'frontend/datatable.html')  

        else:
                return render(request,'frontend/datatable.html')
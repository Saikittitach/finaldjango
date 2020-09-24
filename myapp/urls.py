from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('datatable',views.datatable, name='datatable'),
    path('contact',views.contact, name='contact'),
    # path('datatable_submit ',views.datatable_submit, name='datatable_submit'),  
]

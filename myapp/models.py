from django.db import models
# class Product(models.Model):
#     product_name = models.CharField(max_length=128)
#     product_details = models.TextField()
#     product_barcode = models.CharField(max_length=32)
#     product_qty = models.IntegerField()
#     product_price = models.DecimalField(decimal_places=2 ,max_digits=7)
#     product_image = models.CharField(max_length=64)
#     product_status = models.IntegerField()
# Create your models here.

class Datatabase(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    desc = models.TextField()

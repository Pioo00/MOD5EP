from django.shortcuts import render
from .models import Supplier, WaterBottle

# Create your views here.

def view_supplier(request): 
    supplier = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier_list.html',{'suppliers': supplier})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottle_list.html', {'bottles': bottles})
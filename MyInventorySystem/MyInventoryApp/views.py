from django.shortcuts import render
from .models import Supplier

# Create your views here.

def view_supplier(request): 
    supplier = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier_list.html',{'suppliers': supplier})

def add_waterbottle(request):
    return render(request, 'MyInventoryApp/add_waterbottle.html')
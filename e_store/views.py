
from django.shortcuts import render

from . models import *

# Create your views here.


def store(request):
    product=Product.objects.all()
    print(product)
    context={
        'products': product
    }
    return render(request,"store.html",context)


def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")
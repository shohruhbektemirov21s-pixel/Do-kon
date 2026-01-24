from django.shortcuts import render

# Create your views here.

from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
    
from django.http import HttpResponse

def home(request):
    return HttpResponse("Salom! Bosh sahifa ishlayapti 🚀")

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.filter(status=True)
    return render(request, 'index.html', {"products" : products})
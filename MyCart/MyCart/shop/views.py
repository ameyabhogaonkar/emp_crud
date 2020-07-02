
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
     products = Product.objects.all()
     print(products)
     params = {}
     return render(request,"shop/index.html",params)

def about(request):
     return render(request,"shop/about.html")

def contact(request):
     return HttpResponse("this is about")

def tracker(request):
     return HttpResponse("this is about")

def search(request):
     return HttpResponse("this is about")

def productview(request):
     return HttpResponse("this is about")

def checkout(request):
     return HttpResponse("this is about")
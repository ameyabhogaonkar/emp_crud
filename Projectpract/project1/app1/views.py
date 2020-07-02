from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    return render(request,'home.html',{'name' :'Ameya'})

def add(request):
     try:
      val1 = int(request.POST["num1"])
      val2 = int(request.POST["num2"])
      res = val1 + val2
     except MultiValueDictKeyError:
        return render(request,'result.html',{'result': res})

# This file is crated by EIS

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  # return HttpResponse("This is home page")
  return render(request,'productms/index.html')

def product(request):
  return render(request,'productms/product.html')

def customer(request):
  return render(request,'productms/customer.html')
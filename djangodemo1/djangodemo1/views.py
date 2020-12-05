# This file is cated by Emran Ibn Shayed

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hi, I'm Emran Ibn Shayed")

def home(request):
    return render(request,"index.html")



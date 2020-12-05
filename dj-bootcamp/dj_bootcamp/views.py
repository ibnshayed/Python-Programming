from django.shortcuts import render

def index(request):
  return render(request,"dj_bootcamp/index.html")
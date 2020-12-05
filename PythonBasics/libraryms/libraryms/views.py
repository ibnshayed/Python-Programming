from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
  # return HttpResponse("Library Manament System Home Page")
  return render(request, 'libraryms/index.html')

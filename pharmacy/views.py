from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pharmacy_home(request):
    return HttpResponse('<h1>This is the pharmacy Homepage')
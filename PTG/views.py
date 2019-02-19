from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Pharmacy Homepage</h1><br><a href="/pharmacy">Pharmacy Homepage</a>')
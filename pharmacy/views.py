from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class pharmacy_home(View):
    def get(self, request):
        return render(request, "pharmacy/pharmacy_home.html")
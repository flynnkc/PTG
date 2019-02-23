from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class project_home(View):
    def get(self, request):
        return render(request, 'ptg/project_home.html')
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Decorator sets login required on GET requests
@method_decorator(login_required, name='get')
class pharmacy_home(View):

    def get(self, request):
        return render(request, "pharmacy/pharmacy_home.html")

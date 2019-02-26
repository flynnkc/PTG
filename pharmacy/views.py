from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='get')
class pharmacy_home(View):

    def get(self, request):
        return render(request, "pharmacy/pharmacy_home.html")
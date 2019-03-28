from django.shortcuts import render
from django.views import View

# Class based view to render project landing page from template
class project_home(View):
    def get(self, request):
        # Render page into template. Takes request, template, and context as inputs.
        return render(request, 'ptg/project_home.html')

class pharmacy_about(View):

    def get(self, request):
        return render(request, "ptg/pharmacy_about.html" )
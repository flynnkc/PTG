"""PTG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as project_views
from django.contrib.auth import views as auth_views

#### This list will contain the url patterns at the PROJECT level ####
urlpatterns = [
    path('', project_views.project_home.as_view(), name='project_home'),
    path('admin/', admin.site.urls),
    path('pharmacy/', include('pharmacy.urls')), # include() Directs search to urls.py in pharmacy app folder
    path('accounts/', include('django.contrib.auth.urls')), # Directs to default auth module url structure
    path('about/', project_views.pharmacy_about.as_view(), name='project_about')
]

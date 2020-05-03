"""projectdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from src.test_app.views import hello, gen_password, get_unique_firstnames, get_filtered_by_state_and_city, get_revenue, \
    get_invoices

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('gen-password', gen_password),
    path('get-unique-firstnames', get_unique_firstnames),
    path('filter-by-state-and-city', get_filtered_by_state_and_city),
    path('get-revenue', get_revenue),
    path('get-invoices', get_invoices),


]

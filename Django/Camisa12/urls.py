from django.contrib import admin
from django.urls import path

from Camisa12 import views

app_name = "Camisa12"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('notas/', views.notas, name='notas'),
    path('times/', views.busca_times, name='busca_times'),
    path('times/', views.busca_times, name='busca_times'),
]

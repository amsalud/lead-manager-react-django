from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ui.urls')),
    path('', include('leads.urls')),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms-conditions/', views.terms_conditions, name='terms-conditions'),

    
]
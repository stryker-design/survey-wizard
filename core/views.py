from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# DRF IMPORTS
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def roadmap(request):
    context = {}
    return render(request, 'core/roadmap.html', context)




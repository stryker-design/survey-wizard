from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# DRF IMPORTS
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/survey-list/',
		'Detail View':'/survey-detail/<str:pk>/',
		'Create':'/survey-create/',
		'Update':'/survey-update/<str:pk>/',
		'Delete':'/survey-delete/<str:pk>/',
		}

    return Response(api_urls)

# def surveyList(request):
# 	tasks = surveyList.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)
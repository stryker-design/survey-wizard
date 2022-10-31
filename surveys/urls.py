from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import dashboard_views, survey_views, api_views

urlpatterns = [
    path('dashboard/', dashboard_views.dashboard_view, name='dashboard'),

    path("surveys/", survey_views.survey_list, name="survey-list"),
    path("surveys/<uuid:uuid>/", survey_views.detail, name="survey-detail"),
    path("surveys/create/", survey_views.create, name="survey-create"),
    path("surveys/<uuid:uuid>/delete/", survey_views.delete, name="survey-delete"),
    path("surveys/<uuid:uuid>/edit/", survey_views.edit, name="survey-edit"),
    path("surveys/<uuid:uuid>/question/", survey_views.question_create, name="survey-question-create"),
    path("surveys/<uuid:uuid>/delete-question", survey_views.question_delete, name='question-delete'),
    path(
        "surveys/<uuid:survey_uuid>/question/<uuid:question_uuid>/option/",
        survey_views.option_create,
        name="survey-option-create",
    ),
    path(
        "surveys/<uuid:survey_uuid>/question/<uuid:question_uuid>/option-checked/",
        survey_views.option_create_checked,
        name="survey-option-create-checked",
    ),
    path("surveys/<uuid:pk>/start/", survey_views.start, name="survey-start"),
    path("surveys/<uuid:survey_pk>/submit/<int:sub_pk>/", survey_views.submit, name="survey-submit"),
    path("surveys/<uuid:pk>/thanks/", survey_views.thanks, name="survey-thanks"),

    # RESULTS

    path('results/<uuid:pk>/', dashboard_views.results, name='results'),


    # API
    path('api/', api_views.apiOverview, name='api'),

    # path('survey-list/', views.surveyList, name="survey-list"),
	# path('task-detail/<str:pk>/', views.surveyDetail, name="survey-detail"),
	# path('task-create/', views.surveyCreate, name="survey-create"),
	# path('task-update/<str:pk>/', views.surveyUpdate, name="survey-update"),
	# path('task-delete/<str:pk>/', views.surveyDelete, name="survey-delete"),

        
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # APPS
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('surveys.urls')),
    path('', include('blog.urls')),

    # DRF
    path('api-auth/', include('rest_framework.urls')),

    # TAILWIND
    path("__reload__/", include("django_browser_reload.urls")),

]

handler404 = 'core.views.not_found'

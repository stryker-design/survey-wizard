from django.contrib import admin
from django.urls import path, include
from blog.views import blog_views


urlpatterns = [
        path('blog/', blog_views.BlogView.as_view(), name='blog-list'),
        path('blog/<int:pk>', blog_views.BlogDetailView.as_view(), name='blog-detail'),     

        path('product-blog/', blog_views.ProductBlogView.as_view(), name='product-blog-list'),
        path('blog/<int:pk>', blog_views.ProductBlogDetailView.as_view(), name='product-blog-detail'),       
]
from django.urls import path

from . import views

urlpatterns = [
    path('links/', views.LinkAPIViewGet.as_view(), name='api_links'),
    path('links/create', views.LinkAPIViewPost.as_view(), name='api_links_create'),
]

from django.urls import path

from api import views

urlpatterns = [
    path("link/", views.LinkAPIView.as_view(), name="api_links"),
    path("file/", views.FileAPIView.as_view(), name="api_file"),
    path("logs/", views.LogsAPIView.as_view(), name="logs"),
]

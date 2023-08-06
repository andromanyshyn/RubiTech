from django.urls import path

from api.views import LinkAPIView, FileAPIView, LogsAPIView

urlpatterns = [
    path("link/", LinkAPIView.as_view(), name="api_links"),
    path("file/", FileAPIView.as_view(), name="api_file"),
    path("logs/", LogsAPIView.as_view(), name="logs"),
]

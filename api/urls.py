from django.urls import path

from api import views

urlpatterns = [
    path('link/', views.LinkAPIView.as_view(), name='api_links'),
]

from django.urls import path, include

urlpatterns = [
    path("", include("api.urls")),
    path("users/", include("users.urls")),
]

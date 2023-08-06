from django.urls import path
from users.views import CustomAuthToken, UserLogoutView

urlpatterns = [
    path("auth/", CustomAuthToken.as_view(), name="auth"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]

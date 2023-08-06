from rest_framework.authtoken.views import ObtainAuthToken
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import logout

logger = logging.getLogger(__name__)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            logger.info(f"User logged in {request.data['username']}", )
        return response


class UserLogoutView(APIView):
    @staticmethod
    def post(request):
        username = request.user.username
        logout(request)
        logger.info(f"User logged out {username}", )
        return Response({"status": status.HTTP_200_OK, "message": "User Logout successfully"})

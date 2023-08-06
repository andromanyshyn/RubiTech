from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.tasks import download
import logging
from app_service.models import Link
from api.filters import LinkFilter

from api.serializers import LinkSerializer, LinkListSerializer, FileSerializer

logger = logging.getLogger(__name__)


class LinkAPIView(ListCreateAPIView):
    queryset = Link.objects.all()
    filterset_class = LinkFilter

    def get_serializer_class(self):
        return LinkListSerializer if self.request.method == 'GET' else LinkSerializer

    def list(self, request, *args, **kwargs):
        logger.info(f"Received GET request: {request}")
        response = super().list(request, *args, **kwargs)
        logger.info(f"Response - {response}")
        return response

    def create(self, request, *args, **kwargs):
        logger.info(f"Received POST request: {request}")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        logger.info(f"Response - {response}")
        return Response(response, status=status.HTTP_201_CREATED)


class FileAPIView(APIView):
    @staticmethod
    def post(request):
        logger.info(f"Received POST request: {request}")
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file'].read().decode('utf-8')
        try:
            download.delay(file)
        except Exception as error:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, "error": error})
        response = {'status': status.HTTP_201_CREATED, 'info': "in process"}
        logger.info(f"Response - {response}")
        return Response(
            response
        )


class LogsAPIView(APIView):
    @staticmethod
    def get(request):
        logger.info(f"Received GET request: {request}")
        with open(settings.LOG_FILE, "r") as file:
            list_logs = [log for log in file.read().splitlines()[-20:][::-1]]
            response = Response({"status": status.HTTP_200_OK, "logs": list_logs})
            logger.info(f"Response - {response}")
            return response

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.tasks import download

from app_service.models import Link

from api.serializers import LinkSerializer, LinkListSerializer, FileSerializer


class LinkAPIView(ListCreateAPIView):
    queryset = Link.objects.all()

    def get_serializer_class(self):
        return LinkListSerializer if self.request.method == 'GET' else LinkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response, status=status.HTTP_201_CREATED)


class FileAPIView(APIView):
    @staticmethod
    def post(request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file'].read().decode('utf-8')
        try:
            download.delay(file)
        except Exception as error:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, "error": error})
        return Response(
            {'status': status.HTTP_201_CREATED, 'info': "in process"}
        )

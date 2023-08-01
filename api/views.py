import uuid

from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from app_service.models import Link, LinkImport

from api.serializers import LinkSerializer, LinkListSerializer


class LinkAPIView(ListCreateAPIView):
    queryset = Link.objects.all()

    def get_serializer_class(self):
        return LinkListSerializer if self.request.method == 'GET' else LinkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response, status=status.HTTP_201_CREATED)

        # else:
        #     csv_file = serializer.validated_data['csv_field']
        #     file_data = csv_file.read().decode('utf-8')  # open file
        #     for link in file_data.split():
        #         Link.objects.create(link_code=uuid.uuid4(),
        #                             protocol=link.split(':')[0],
        #                             domain=link.split('//')[1].split('.')[0] if 'www' not in link.split('//')[
        #                                 1].split('.') else link.split('//')[1].split('.')[1],
        #                             domain_zone=link.split('//')[1].split('.')[1].split('/')[0] if 'www' not in
        #                                                                                            link.split('//')[
        #                                                                                                1].split(
        #                                                                                                '.') else
        #                             link.split('//')[1].split('.')[-1].split('/')[0],
        #                             path='/'.join(link.split('//')[1].split('/')[1:]))
        #     count_links = len([i for i in file_data.split()])
        #     last_created_objects = Link.objects.order_by('-id')[:count_links].values()  # get last five objects
        #
        #     return Response({'links': list(last_created_objects)})

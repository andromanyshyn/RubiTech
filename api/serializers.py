import uuid

from rest_framework import serializers

from api.utils import create_link
from app_service.models import Link


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"


class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()

    def save(self, **kwargs):
        return create_link(self.validated_data.get("link"))


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

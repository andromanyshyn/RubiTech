from rest_framework import serializers

from app_service.models import Link


class LinkSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

        extra_kwargs = {
            'link_field': {'read': True},
            'link_code': {'read_only': True},
            'protocol': {'read_only': True},
            'domain': {'read_only': True},
            'domain_zone': {'read_only': True},
            'path': {'read_only': True},
        }


class LinkSerializer(serializers.Serializer):
    link = serializers.URLField(required=False)
    csv_field = serializers.FileField(required=False)

    class Meta:
        fields = (
            'link',
            'csv_field',
        )

        # extra_kwargs = {
        #     'link_field': {'write_only': True},
        #     'link_code': {'read_only': True},
        #     'protocol': {'read_only': True},
        #     'domain': {'read_only': True},
        #     'domain_zone': {'read_only': True},
        #     'path': {'read_only': True},
        # }

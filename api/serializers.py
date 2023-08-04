import uuid

from rest_framework import serializers

from app_service.models import Link


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()

    def save(self, **kwargs):
        link_code = uuid.uuid4()
        link = self.validated_data.get('link')
        protocol = link.split(':')[0]
        domain = link.split('//')[1].split('.')[0] if 'www' not in link.split('//')[1].split('.') else \
            link.split('//')[1].split('.')[1]
        domain_zone = link.split('//')[1].split('.')[1].split('/')[0] if 'www' not in link.split('//')[1].split(
            '.') else link.split('//')[1].split('.')[-1].split('/')[0]
        path = ''.join(link.split(domain_zone)[1].split('?')[0]) if '?' in link else ''.join(link.split(domain_zone)[1])

        get_parameters = link.split('?')[1] if '?' in link else ''
        parameters = {}
        if get_parameters:
            if '&' in get_parameters:
                param_pairs = get_parameters.split("&")
                for pair in param_pairs:
                    key_value = pair.split("=")
                    key, value = key_value
                    parameters[key] = value
            else:
                key_value = get_parameters.split("=")
                key, value = key_value
                parameters[key] = value

        Link.objects.create(link_code=uuid.uuid4(), protocol=protocol, domain=domain,
                            domain_zone=domain_zone, path=path, parameters=parameters)

        link_data = {
            'code': link_code,
            'protocol': protocol,
            'domain': domain,
            'domain_zone': domain_zone,
            'path': path,
            'parameters': parameters
        }
        return link_data


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

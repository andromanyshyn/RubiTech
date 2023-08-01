from celery import shared_task
import uuid
from app_service.models import Link


@shared_task
def download(file):
    for link in file.splitlines():
        Link.objects.create(
            link_code=uuid.uuid4(),
            protocol=link.split(':')[0],
            domain=link.split('//')[1].split('.')[0] if 'www' not in link.split('//')[
                1].split('.') else link.split('//')[1].split('.')[1],
            domain_zone=link.split('//')[1].split('.')[1].split('/')[0] if 'www' not in
                                                                           link.split('//')[
                                                                               1].split(
                                                                               '.') else
            link.split('//')[1].split('.')[-1].split('/')[0],
            path='/'.join(link.split('//')[1].split('/')[1:])
        )

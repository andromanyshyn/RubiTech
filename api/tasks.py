from celery import shared_task
import uuid
# from app_service.models import Link
from api.utils import create_link


@shared_task
def download(file):
    for link in file.splitlines():
        create_link(link, return_data=False)

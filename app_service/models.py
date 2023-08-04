from django.db import models


class Link(models.Model):
    link_code = models.UUIDField(unique=True, null=True, blank=True)
    protocol = models.CharField(max_length=10)
    domain = models.CharField(max_length=32)
    domain_zone = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    parameters = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'ID{self.id} {self.link_code} {self.protocol}'


class LinkImport(models.Model):
    csv_file = models.FileField(upload_to='files')

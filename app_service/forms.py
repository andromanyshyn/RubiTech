from django import forms
from django.db import ProgrammingError

from .models import *


class LinkCreateForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


class FilterDomainZone(forms.Form):
    try:
        domain_zones = [link.domain_zone for link in Link.objects.all()]
        CHOICES = [tuple([i, i]) for i in domain_zones]

        filters = forms.MultipleChoiceField(choices=CHOICES, required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'js-example-basic-multiple', }))
    except:
        ProgrammingError(print('Make Migrations'))


class LinkImportForm(forms.ModelForm):
    class Meta:
        model = LinkImport
        fields = ('csv_file',)

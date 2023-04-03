import uuid

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from .forms import *
from .models import *


def index(request):
    if request.method == 'POST':
        if 'csv_file' in request.FILES:
            form2 = LinkImportForm(data=request.POST, files=request.FILES)
            if form2.is_valid():
                csv_file = form2.cleaned_data['csv_file']
                file_data = csv_file.read().decode('utf-8')  # open file
                for link in file_data.split():
                    Link.objects.create(link_code=uuid.uuid4(),
                                        protocol=link.split(':')[0],
                                        domain=link.split('//')[1].split('.')[0] if 'www' not in link.split('//')[
                                            1].split('.') else link.split('//')[1].split('.')[1],
                                        domain_zone=link.split('//')[1].split('.')[1].split('/')[0] if 'www' not in
                                                                                                       link.split('//')[
                                                                                                           1].split(
                                                                                                           '.') else
                                        link.split('//')[1].split('.')[-1].split('/')[0],
                                        path='/'.join(link.split('//')[1].split('/')[1:]))
                return redirect(reverse('links'))
        else:
            form = LinkCreateForm(request.POST)
            if form.is_valid():
                link = request.POST['link']
                Link.objects.create(link_code=uuid.uuid4(),
                                    protocol=link.split(':')[0],
                                    domain=link.split('//')[1].split('.')[0] if 'www' not in link.split('//')[
                                        1].split('.') else link.split('//')[1].split('.')[1],
                                    domain_zone=link.split('//')[1].split('.')[1].split('/')[0] if 'www' not in
                                                                                                   link.split('//')[
                                                                                                       1].split(
                                                                                                       '.') else
                                    link.split('//')[1].split('.')[-1].split('/')[0],
                                    path='/'.join(link.split('//')[1].split('/')[1:]))
                return redirect(reverse('links'))
    else:
        form = LinkCreateForm()
        form2 = LinkImportForm()
    return render(request, 'app_service/base.html', context={
        'form': form, 'form2': form2})


class LinksListView(ListView):
    template_name = 'app_service/links.html'
    model = Link
    paginate_by = 10
    context_object_name = 'links'

    def get_queryset(self):
        if 'domain_name' in self.request.GET:
            domain = self.request.GET['domain_name']
            queryset = Link.objects.filter(domain=domain)
        elif 'filters' in self.request.GET:
            domain_zone = self.request.GET['filters']
            queryset = Link.objects.filter(domain_zone=domain_zone)

        else:
            queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = FilterDomainZone()
        return context


def delete_link(request, link_id):
    link = Link.objects.get(id=link_id)
    link.delete()
    return redirect(reverse('links'))

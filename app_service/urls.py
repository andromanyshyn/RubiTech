from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('links/', views.LinksListView.as_view(), name='links'),
    # path('csv/', views.link_import, name='link_csv'),
    path('link_delete/<int:link_id>', views.delete_link, name='link_delete'),
    # path('sendlink/', views.LinkCreateView.as_view(), name='sendlink'),
]

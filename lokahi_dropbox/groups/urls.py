from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'^create_group/$', views.create_group, name='create_group'),
    url(r'^view_groups/$', views.view_group, name='view_group'),
    url(r'^edit_group/$', views.edit_group, name='edit_group'),
    url(r'^add_members/$', views.add_members, name='add_members'),
]

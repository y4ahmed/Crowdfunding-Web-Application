from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wall, name='wall'),
    url(r'^post/$', views.post, name='post'),
    url(r'^make_post/$', views.make_post, name='make_post'),
    url(r'^view_wall/$', views.view_wall, name='view_wall'),
]

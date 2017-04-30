from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.messaging, name='messaging'),
    url(r'^send_message/$', views.send_message, name='send_message'),
    url(r'^receive_message/$', views.receive_message, name='receive_message'),
    url(r'^delete_message/$', views.delete_message, name='delete_message'),
    url(r'^decrypt_message/$', views.decrypt_message, name='decrypt_message'),
]

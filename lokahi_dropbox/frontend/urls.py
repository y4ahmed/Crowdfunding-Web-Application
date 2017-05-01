from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success,
        name='register_success'),
    url(r'^logout/$', views.logout_page, name='logout'),

    # Temporarily handle broken links
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^upload_success/$', views.upload_success, name='upload_succes'),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from frontend.views import *
from messaging.views import *
from groups.views import *

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload', upload_file),
    url(r'^upload_success', upload_success),
    url(r'^send_message', send_message),
    url(r'^receive_message', receive_message),
    url(r'^groups/$', groups),
    url(r'^groups/create_group/$', create_group),
    url(r'^groups/view_groups/$', view_group),
    url(r'^delete_message/$', delete_message),
    url(r'^edit_group/$', edit_group),
    url(r'^add_members/$', add_members),
    url(r'^decrypt_message/$', decrypt_message),
)

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'lokahi_dropbox.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# ]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import *

urlpatterns = patterns(
    '',
    url(r'^$', 'django.contrib.auth.views.login'),
    # If user is not login it will redirect to login page
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('frontend.urls'), name='home'),
    url(r'^messaging/', include('messaging.urls'), name='messaging'),
    url(r'^groups/', include('groups.urls'), name='groups'),
    url(r'^wall/', include('wall_post.urls'), name='wall'),

    # Search views
    url(r'^home/search/$', basic_search),
)

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'lokahi_dropbox.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# ]

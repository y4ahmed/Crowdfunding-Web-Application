from django.conf.urls import include, url
# from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from search.views import *

# Regular website patterns
urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    # If user is not login it will redirect to login page
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('frontend.urls'), name='home'),
    url(r'^messaging/', include('messaging.urls'), name='messaging'),
    url(r'^groups/', include('groups.urls'), name='groups'),
    url(r'^wall/', include('wall_post.urls'), name='wall'),

    # Search views
    url(r'^home/search/$', basic_search),
]

# Serve static files
urlpatterns += staticfiles_urlpatterns()

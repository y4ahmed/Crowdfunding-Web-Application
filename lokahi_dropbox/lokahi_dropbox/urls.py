from django.conf.urls import include, url
# from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
# from django.contrib.auth.decorators import user_passes_test
from search.views import *
from django.conf.urls.static import static
from django.conf import settings

# login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

# Regular website patterns
urlpatterns = [
    url(r'^$', login, name='login'),
    # If user is not login it will redirect to login page
    url(r'^accounts/login/$', login, name='login'),
    # url(r'^admin/', include(admin.site.urls)),

    # App urls
    url(r'^', include('frontend.urls'), name='home'),
    url(r'^messaging/', include('messaging.urls'), name='messaging'),
    url(r'^groups/', include('groups.urls'), name='groups'),
    url(r'^wall/', include('wall_post.urls'), name='wall'),
    url(r'^user_management/', include('site_manager.urls'), name='manager_users'),
    url(r'^reports/', include('reports.urls'), name='reports'),
    # url(r'^createReport/', createReport),
    # url(r'^viewReport/', viewReport),
    # Search views
    url(r'^home/search/$', basic_search),
    url(r'^home/advanced_search/$', advanced_search),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files
urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA.ROOT)

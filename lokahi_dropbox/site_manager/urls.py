from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_management, name='user_management'),
    url(r'^give_site_manager_role/$', views.user_management,
        name='give_site_manager_role'),
    url(r'^suspend_user/$', views.suspend_user, name='suspend_user'),
    url(r'^give_site_manager_role/$', views.restore_user, name='restore_user'),
]

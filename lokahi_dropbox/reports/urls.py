from django.conf.urls import url

from . import views

urlpatterns = [
    # view Reports
    url(r'^view_report/$', views.view_report, name='view_report'),
    # createReports
    url(r'^create_report/$', views.create_report, name='create_report'),
    # editReports
    url(r'^edit_reports/$', views.edit_report, name='edit_report'),
    # deleteReports
    url(r'^delete_reports/$', views.delete_report, name='delete_report'),
]

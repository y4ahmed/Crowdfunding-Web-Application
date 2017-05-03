from django.conf.urls import url

from . import views
from .views import list_report

urlpatterns = [
    # view Reports
    url(r'^view_report/$', views.view_report, name='view_report'),
    # createReports
    url(r'^list_report/$', list_report.as_view()),
    #list_report
    url(r'^create_report/$', views.create_report, name='create_report'),
    # editReports
    url(r'^edit_report/$', views.edit_report, name='edit_report'),
    url(r'^edit_report/(?P<pk>\d+)/',views.edit_report, name='edit_report'),
    # deleteReports
    url(r'^delete_report/$', views.delete_report, name='delete_report'),
]

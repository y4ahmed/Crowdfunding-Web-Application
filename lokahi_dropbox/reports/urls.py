from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewReport, name='view_Report'),
    #view Reports
    url(r'^create_Report/$', views.createReport, name='create_Report'),
    #createReports
    url(r'^edit_Reports/$', views.editReport, name='edit_Report'),
    #editReports
    url(r'^delete_Reports/$', views.deleteReport, name='delete_Report'),
    #deleteReports
]

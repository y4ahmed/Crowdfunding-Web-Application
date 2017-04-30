rom django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewReport, name='viewReport'),
    #view Reports
    url(r'^create_Reports/$', views.createReport, name='createReport'),
    #createReports
    url(r'^edit_Reports/$', views.editReport, name='editReport'),
    #editReports
    url(r'^delete_Reports/$', views.deleteReport, name='deleteReport'),
    #deleteReports
]

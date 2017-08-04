from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 
        views.indexNoUser, name='indexNoUser'),
    url(r'^login/$', 
        views.login, name='login'),
    url(r'^(?P<user_id>[0-9]+)/$', 
        views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/browse-files/$', 
        views.browseFiles, name='browseFiles'),
    url(r'^(?P<user_id>[0-9]+)/upload-file/$', 
        views.upload, name='upload'),
    url(r'^(?P<user_id>[0-9]+)/delete-file/(?P<file_id>[0-9]+)/$', 
        views.deleteFile, name='deleteFile'),
    url(r'^(?P<user_id>[0-9]+)/edit-file/(?P<file_id>[0-9]+)/$', 
        views.setConcentrations, name='editFile'),
    url(r'^(?P<user_id>[0-9]+)/delete-curve/(?P<curve_id>[0-9]+)/$', 
        views.setConcentrations, name='deleteCurve'),
    url(r'^(?P<user_id>[0-9]+)/show-file/(?P<file_id>[0-9]+)/$', 
        views.showFile, name='showFile'),
    url(r'^(?P<user_id>[0-9]+)/generate-plot/(?P<plot_type>[a-z]+)/(?P<value_id>[0-9,]+)/$',
        views.generatePlot, name='generatePlot'),
    url(r'^(?P<user_id>[0-9]+)/browse-calibrations/$', 
        views.browseCalibrations, name='browseCalibrations'),
    url(r'^(?P<user_id>[0-9]+)/select-curves-for-calibration/$', 
        views.prepareCalibration, name='selectCurvesForCalibration'),
    url(r'^(?P<user_id>[0-9]+)/show-calibration/(?P<calibration_id>[0-9]+)/$', 
        views.showCalibration, name='showCalibration'),
    url(r'^(?P<user_id>[0-9]+)/edit-calibration/(?P<calibration_id>[0-9]+)/$', 
        views.editCalibration, name='editCalibration'),
]

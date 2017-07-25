from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/browse-files/$', views.browseFiles, name='browseFiles'),
    url(r'^(?P<user_id>[0-9]+)/upload-file/$', views.upload, name='upload'),
    url(r'^(?P<user_id>[0-9]+)/show-file/(?P<curvefile_id>[0-9]+)$', views.showFile, name='showFile'),
    url(r'^(?P<user_id>[0-9]+)/generate-plot/(?P<plot_type>[a-z]+)/(?P<value_id>[0-9]+)/', views.generatePlot, name='generatePlot'),
    url(r'^(?P<user_id>[0-9]+)/browse-calibrations/$', views.prepareCalibration, name='browseCalibrations'),
    url(r'^(?P<user_id>[0-9]+)/prepare-calibration/$', views.prepareCalibration, name='prepareCalibration'),
    url(r'^(?P<user_id>[0-9]+)/show-calibration/(?P<calibration_id>[0-9]+)$', views.prepareCalibration, name='showCalibration'),
]

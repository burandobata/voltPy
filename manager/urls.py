from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 
        views.indexNoUser, name='indexNoUser'),
    url(r'^(?P<user_id>[0-9]+)/$', 
        views.index, name='index'),
    url(r'^login/$', 
        views.login, name='login'),
    url(r'^logout/$', 
        views.logout, name='logout'),
    url(r'^(?P<user_id>[0-9]+)/browse-files/$', 
        views.browseCurveFile, name='browseCurveFile'),
    url(r'^(?P<user_id>[0-9]+)/upload-file/$', 
        views.upload, name='upload'),
    url(r'^(?P<user_id>[0-9]+)/delete-file/(?P<file_id>[0-9]+)/$', 
        views.deleteCurveFile, name='deleteCurveFile'),
    url(r'^(?P<user_id>[0-9]+)/edit-file/(?P<file_id>[0-9]+)/$', 
        views.editCurveFile, name='editCurveFile'),
    url(r'^(?P<user_id>[0-9]+)/show-file/(?P<file_id>[0-9]+)/$', 
        views.showCurveFile, name='showCurveFile'),
    url(r'^(?P<user_id>[0-9]+)/delete-curve/(?P<curve_id>[0-9]+)/$', 
        views.deleteCurve, name='deleteCurve'),
    url(r'^(?P<user_id>[0-9]+)/browse-curvesets/$', 
        views.browseCurveSet, name='browseCurveSet'),
    url(r'^(?P<user_id>[0-9]+)/create-curve-set/$', 
        views.createCurveSet, name='createCurveSet'),
    url(r'^(?P<user_id>[0-9]+)/show-curveset/(?P<curveset_id>[0-9]+)/$', 
        views.showCurveSet, name='showCurveSet'),
    url(r'^(?P<user_id>[0-9]+)/edit-curveset/(?P<curveset_id>[0-9]+)/$', 
        views.editCurveSet, name='editCurveSet'),
    url(r'^(?P<user_id>[0-9]+)/delete-curveset/(?P<curveset_id>[0-9]+)/$', 
        views.deleteCurveSet, name='deleteCurveSet'),
    url(r'^(?P<user_id>[0-9]+)/analyze/(?P<analysis_id>[0-9]+)/$', 
        views.analyze, name='analyze'),
    url(r'^(?P<user_id>[0-9]+)/process/(?P<processing_id>[0-9]+)/$', 
        views.process, name='process'),
    url(r'^(?P<user_id>[0-9]+)/show-analysis/(?P<analysis_id>[0-9]+)/$', 
        views.showAnalysis, name='showAnalysis'),
    url(r'^(?P<user_id>[0-9]+)/browse-analysis/$', 
        views.browseAnalysis, name='browseAnalysis'),
    url(r'^(?P<user_id>[0-9]+)/delete-analysis/(?P<analysis_id>[0-9]+)/$', 
        views.deleteAnalysis, name='deleteAnalysis'),
    url(r'^(?P<user_id>[0-9]+)/edit-analysis/(?P<analysis_id>[0-9]+)/$', 
        views.editAnalysis, name='editAnalysis'),
    url(r'^(?P<user_id>[0-9]+)/show-processed/(?P<processing_id>[0-9]+)/$', 
        views.showProcessed, name='showProcessed'),
    url(r'^(?P<user_id>[0-9]+)/plot-interaction/$',
        views.plotInteraction, name='plotInteraction'),
]

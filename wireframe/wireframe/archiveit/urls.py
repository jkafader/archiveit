from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'wireframe.archiveit.views.index'),
    url(r'^create-collection/$', 'wireframe.archiveit.views.CollectionWizard'),
)

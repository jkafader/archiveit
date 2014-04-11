from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wireframe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('wireframe.archiveit.urls', namespace='archiveit')),
    # TODO: add urls for account system.
    #url(r'^account/$', include(wireframe.accounts.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

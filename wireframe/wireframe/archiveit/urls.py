from django.conf.urls import patterns, url
from wireframe.archiveit.views import CollectionWizard
#from wireframe.archiveit.forms import COLLECTION_WIZARD_STEPS

urlpatterns = patterns('wireframe.archiveit.views',
    # the index renders the partner home page.
    url(r'^$', 'index'),
    # /json/ url to deserialize and save objects in JSON format from Angular.
    url(r'json/$', 'handle_json_data'),
    # the views for the collection wizard
    url(r'collection/add/$', CollectionWizard().as_view(0)),
    url(r'collection/(?P<id>\d+)/create/$', CollectionWizard().as_view(0)),
    url(r'collection/(?P<id>\d+)/add-seeds/$', CollectionWizard().as_view(1)),
    url(r'collection/(?P<id>\d+)/add-metadata/$', CollectionWizard().as_view(2)),
    url(r'collection/(?P<id>\d+)/add-scope/$', CollectionWizard().as_view(3)),
    url(r'collection/(?P<id>\d+)/review/$', CollectionWizard().as_view(4)),
    url(r'collection/(?P<id>\d+)/$', 'collection_display'),
    #url(r'^create-collection/$', CollectionWizard.as_view(COLLECTION_WIZARD_STEPS)),
)

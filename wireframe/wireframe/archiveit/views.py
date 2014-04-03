from django.shortcuts import render
from django.contrib.formtools.wizard.views import SessionWizardView
from wireframe.archiveit.models import Collection, Seed

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    collections = Collection.objects.filter(owner = request.user.account)
    render(request, "PAGE-partner_home.html", {'collections': collections})

class CollectionWizard(SessionWizardView):
    template_name = "PAGE-collection_wizard.html"
    def done(self, form_list, **kwargs):
        form_date = process_form_data(form_list)
        return render(request, 'PAGE-collection_review.html', {'form_data': form_data})

def process_form_data(form_list):
    for form in form_list:
        # TODO setup processing for each form.
        pass
    logger.debug(form_list)
    return form_list

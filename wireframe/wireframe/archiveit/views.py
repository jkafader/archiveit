from django.shortcuts import render
#from django.contrib.formtools.wizard.views import SessionWizardView
from wireframe.archiveit.models import Collection, Seed
from django.contrib.auth.decorators import login_required
from wireframe.archiveit.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

import logging
logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def index(request):
    inactive_collections = Collection.objects.filter(owner = request.user.get_profile().account, active=False)
    active_collections = Collection.objects.filter(owner = request.user.get_profile().account, active=True)
    return render(request, "PAGE-partner_home.html", {'active_collections': active_collections, 'inactive_collections': inactive_collections, 'request': request})

@login_required
def collection_display(request, id):
    collection = Collection.objects.get(pk=id, owner=request.user.get_profile().account)
    return render(request, "PAGE-collection_display.html", {"collection": collection, 'request':request})

@login_required
def handle_json_data(request):
    if request.method == "POST" and request.POST.get('models'):
        for obj in serializers.deserialize('json', request.POST.get('models')):
            #raise Exception("Testing")
            obj.save()
        if request.POST.get('next'):
            return HttpResponseRedirect(request.POST.get('next'))
        return HttpResponse("""{"success": "true"}""")
    #raise Exception("Testing")
    return HttpResponse("""{"success": "false"}""")


class CollectionWizard():
    def __init__(self):
        self.creation_steps = [
            {'name': '1. Collection Info', 	'template':'PAGE-collection_create.html',			'form': CollectionAddForm,			'sub_form': False, 	'next': "/collection/{}/add-seeds"},
            {'name': '2. Add Seeds', 		'template':'PAGE-collection_add_seeds.html',		'form': CollectionAddSeedForm,		'sub_form': True, 	'next': "/collection/{}/add-seeds/"},
            {'name': '3. Add Metadata', 	'template':'PAGE-collection_add_metadata.html',		'form': CollectionAddMetadataForm,	'sub_form': False, 	'next': "/collection/{}/add-scope/"},
            {'name': '4. Define Scope', 	'template':'PAGE-collection_add_seed_scope.html',	'form': CollectionAddSeedScopeForm,	'sub_form': True, 	'next': "/collection/{}/add-scope/"},
            {'name': '5. Review Summary', 	'template':'PAGE-collection_review.html',			'form': CollectionReviewForm,		'sub_form': False, 	'next': "/collection/{}/"},
        ]
    def as_view(self, step):
        self.step = self.creation_steps[step]
        @login_required
        def func(request, id=None):
            Form = self.step['form']
            collection = id == None and Collection(owner=request.user.get_profile().account) or Collection.objects.get(owner=request.user.get_profile().account, pk=id)
            form = Form(**(self.step['sub_form'] and {'initial':{"collection":collection}} or {'instance':collection}))
            if request.method == "POST":
                save_form = Form(request.POST, instance=(not self.step['sub_form']) and collection or None)
                if save_form.is_valid():
                    key = save_form.save()
                    return HttpResponseRedirect(self.step['next'].format(*[(self.step['sub_form'] and collection.pk or key.pk),]))
                else:
                    form = save_form
            return render(request, self.step['template'], { 'collection':collection, 'form':form,  'steps': [(step['name'],) for step in self.creation_steps], 'step':step, 'request':request })
        return func

# TODO: this section should really be refactored into a class-based view. It's sharing much of its state between these functions.
# DONE.

#CREATION_STEPS = [
#    ('1. Collection Info', 'collection_create'),
#    ('2. Add Seeds', 'collection_add_seeds'),
#    ('3. Add Metadata', 'collection_add_metadata'),
#    ('4. Define Scope', 'collection_add_seed_scope'),
#    ('5. Review Summary',  'collection_review'),
#]

#@login_required
#def collection_create(request):
#    collection = Collection(owner=request.user.get_profile().account)
#    form = CollectionAddForm(instance=collection)
#    if request.method == 'POST':
#        form = CollectionAddForm(request.POST)
#        if form.is_valid():
#            collection = form.save()
#            return HttpResponseRedirect(reverse('archiveit:wireframe.archiveit.views.collection_add_seeds', args=[collection.id]))
#    return render(request, "PAGE-collection_create.html", {"collection": collection, "form": form, 'steps': CREATION_STEPS, 'step': 0, 'request': request})
#
#@login_required
#def collection_add_seeds(request, id):
#    collection = Collection.objects.get(pk=id, owner=request.user.get_profile().account)
#    form = CollectionAddSeedForm(initial={"collection": collection})
#    if request.method == 'POST':
#        save_form = CollectionAddSeedForm(request.POST)
#        if save_form.is_valid():
#            seed = save_form.save()
#        else:
#            form = save_form
#    return render(request, "PAGE-collection_add_seeds.html", {"collection": collection, "form": form, 'steps': CREATION_STEPS, 'step': 1, 'request': request})
#
#@login_required
#def collection_add_metadata(request, id):
#    collection = Collection.objects.get(pk=id, owner=request.user.get_profile().account)
#    form = CollectionAddMetadataForm(instance=collection)
#    if request.method == 'POST':
#        form = CollectionAddMetadataForm(request.POST, instance=collection)
#        if form.is_valid():
#            collection = form.save()
#            return HttpResponseRedirect(reverse('archiveit:wireframe.archiveit.views.collection_add_seed_scope', args=[collection.id]))
#    return render(request, "PAGE-collection_add_metadata.html", {"collection":collection, "form":form, 'steps': CREATION_STEPS, 'step': 2, 'request': request})
#
#@login_required
#def collection_add_seed_scope(request, id):
#    collection = Collection.objects.get(pk=id, owner=request.user.get_profile().account)
#    form = CollectionAddSeedScopeForm(initial={"collection": collection})
#    if request.method == 'POST':
#        save_form = CollectionAddSeedScopeForm(request.POST)
#        if save_form.is_valid():
#            seed_scope = save_form.save()
#        else:
#            form = save_form
#    return render(request, "PAGE-collection_add_seed_scope.html", {"collection": collection, "form": form, 'steps': CREATION_STEPS, 'step': 3, 'request': request})
#
#@login_required
#def collection_review(request, id):
#    collection = Collection.objects.get(pk=id, owner=request.user.get_profile().account)
#    form = CollectionReviewForm(instance=collection)
#    if request.method == "POST":
#        form = CollectionReviewForm(request.POST)
#        if form.is_valid():
#            collection = form.save()
#    return render(request, "PAGE-collection_review.html", {"collection": collection, 'steps': CREATION_STEPS, 'step': 4, 'request': request})


#class CollectionWizard(SessionWizardView):
#    template_name = "PAGE-collection_wizard.html"
#    def done(self, form_list, **kwargs):
#        form_date = process_form_data(form_list)
#        return render(request, 'PAGE-collection_review.html', {'form_data': form_data})
#
#def process_form_data(form_list):
#    for form in form_list:
#        # TODO setup processing for each form.
#        pass
#    logger.debug(form_list)
#    return form_list

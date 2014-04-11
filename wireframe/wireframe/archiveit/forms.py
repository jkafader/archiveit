from django import forms
from django.forms.models import inlineformset_factory
from wireframe.archiveit.models import Collection, Seed, SeedScopeRule, CONSTANTS
from wireframe.accounts.models import Account

class CollectionAddForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Collection
        fields = ['name', 'public', 'topics', 'owner']

#SeedFormSet = inlineformset_factory(Collection, Seed)

# class CollectionWizardForm2(forms.ModelForm):
#    class Meta:
#        model = Collection
#        fields = ['seed_set',]

class CollectionAddSeedForm(forms.ModelForm):
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Seed
        fields = ['url', 'frequency', 'capture', 'public', 'folder', 'collection']

class CollectionAddBulkSeedsForm(forms.Form):
    seeds = forms.fields.CharField(widget=forms.Textarea)
    # TODO: add parse/save system via form validation.

class CollectionAddMetadataForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Collection
        fields = ['metadata', 'id']

class CollectionAddSeedScopeForm(forms.ModelForm):
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = SeedScopeRule
        fields = ['collection','rule_type','rule_match','use_document_limit','document_limit']
    
class CollectionReviewForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Collection
        fields = ['name', 'public', 'id']


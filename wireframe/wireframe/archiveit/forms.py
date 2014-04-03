from django import forms
from archiveit.models import Collection, Seed

class CollectionWizardForm1(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'public', 'topics']

class CollectionWizardForm2(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['seed_set']

class SeedForm(forms.ModelForm):
    class Meta:
        model = Seed
        fields = ['url', 'frequency', 'capture', 'public', 'group']

class SeedBulkAddForm(forms.Form):
    seeds = forms.TextField()
    # TODO: add parse/save system via form validation.


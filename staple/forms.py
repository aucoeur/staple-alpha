from django import forms
from staple.models import Document


class DocumentForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Document
        fields = '__all__'
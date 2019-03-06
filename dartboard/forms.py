from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SetDecisionForm(forms.Form):
    name = forms.CharField(help_text="Enter the decision you need help making")
    def clean_name(self):
        data = self.cleaned_data['name']
        return data

class AddChoicesForm(forms.Form):
    c1 = forms.CharField(help_text="Enter choice 1")
    c2 = forms.CharField(help_text="Enter choice 2")
    c3 = forms.CharField(help_text="Enter choice 3")
    c4 = forms.CharField(help_text="Enter choice 4")
    c5 = forms.CharField(help_text="Enter choice 5")

    def clean_c1 (self):
        data = self.cleaned_data['c1']
        return data

    def clean_c2 (self):
        data = self.cleaned_data['c2']
        return data

    def clean_c3 (self):
        data = self.cleaned_data['c3']
        return data

    def clean_c4 (self):
        data = self.cleaned_data['c4']
        return data

    def clean_c5 (self):
        data = self.cleaned_data['c5']
        return data

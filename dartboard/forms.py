from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddChoicesForm(forms.Form):
    c1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 1'}), required=True)
    c2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 2'}), required=False)
    c3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 3'}), required=False)
    c4 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 4'}), required=False)
    c5 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 5'}), required=False)
    c6 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 6'}), required=False)
    c7 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 7'}), required=False)
    c8 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 8'}), required=False)
    c9 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 9'}), required=False)
    c10 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Choice 10'}), required=False)

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

    def clean_c6 (self):
        data = self.cleaned_data['c6']
        return data

    def clean_c7 (self):
        data = self.cleaned_data['c7']
        return data

    def clean_c8 (self):
        data = self.cleaned_data['c8']
        return data

    def clean_c9 (self):
        data = self.cleaned_data['c9']
        return data

    def clean_c10 (self):
        data = self.cleaned_data['c10']
        return data

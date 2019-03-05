from django import forms    'django.contrib.auth.middleware.AuthenticationMiddleware',  #Associates users with requests using sessions.
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddDecisionForm(forms.Form):
    name = forms.CharField(help_text="Enter the decision you need help making.")

    def clean_name(self):
        data = self.cleaned_data['name']

        return data

from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Decision(models.Model):
    """Model representing a decision to make."""
    name = models.CharField(max_length=200, help_text='Enter the decision you need help making')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('decision-detail-view', args=[str(self.id)])

class Choice(models.Model):
    """Model representing a choice for a decsion."""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, help_text='Enter the name of the choice')
    decision = models.ForeignKey(Decision, on_delete=models.SET_NULL, null=True, help_text='Select a decision for this choice')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('choice-detail-view', args=[str(self.id)])

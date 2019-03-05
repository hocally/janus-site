from django.shortcuts import render
from dartboard.models import Decision, Choice

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_decisions = Decision.objects.all().count()
    num_choices = Choice.objects.all().count()

    #num_decisions = 4
    #num_choices = 3

    context = {
        'num_decisions': num_decisions,
        'num_choices': num_choices,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

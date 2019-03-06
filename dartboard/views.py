from django.shortcuts import render
from dartboard.models import Decision, Choice

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_visits = request.session.get('num_visits', 0)
    num_decisions = Decision.objects.all().count()
    num_choices = Choice.objects.all().count()
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_decisions': num_decisions,
        'num_choices': num_choices,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def about(request):
    """View function for about page of site"""
    return render(request, 'about.html')

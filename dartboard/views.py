from django.shortcuts import render
from dartboard.models import Decision, Choice
from django.contrib.auth.decorators import login_required

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

@login_required
def choose(request):

    return render(request, 'choose.html')

@login_required
def set_decision(request):

    return render(request, 'set_decision.html')

@login_required
def add_choices(request):

    return render(request, 'add_choices.html')

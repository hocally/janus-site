from dartboard.models import Choice, Decision
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from dartboard.forms import AddChoicesForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import DeleteView, CreateView
import json
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_visits = request.session.get('num_visits', 0)
    num_choices = Choice.objects.all().count()
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_choices': num_choices,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def about(request):
    """View function for about page of site"""
    return render(request, 'about.html')

def view_choices(request):
    #Generic class-based view listing books on loan to current user.
    template_name ='choice_list_author.html'
    context = {'choice_list' : Choice.objects.filter(author=request.user)}
    return render(request, 'choice_list_author.html', context=context)

@login_required
def add_choices_user(request):

    #time_threshold = datetime.now() - timedelta(hours=5)
    #Deletes old choices
    #Choice.objects.filter(author=request.user, timestamp).delete()

    decision = Decision()
    decision.author = request.user
    choices = [Choice(), Choice(), Choice(), Choice(), Choice(), Choice(), Choice(), Choice(), Choice(), Choice()]

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddChoicesForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            choices[0].name = form.cleaned_data['c1']
            choices[1].name = form.cleaned_data['c2']
            choices[2].name = form.cleaned_data['c3']
            choices[3].name = form.cleaned_data['c4']
            choices[4].name = form.cleaned_data['c5']
            choices[5].name = form.cleaned_data['c6']
            choices[6].name = form.cleaned_data['c7']
            choices[7].name = form.cleaned_data['c8']
            choices[8].name = form.cleaned_data['c9']
            choices[9].name = form.cleaned_data['c10']

            currentTime = datetime.now()
            decision.timestamp = currentTime
            decision.save()
            for choice in choices:
                if choice.name is not '':
                    choice.author = request.user
                    choice.decision = decision
                    choice.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('dartboard:choose')) #should redirect to enter choices page

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_name = 'What to eat for dinner'
        form = AddChoicesForm()

    context = {
        'decision' : decision,
        'form': form,
        'c1': choices[0],
        'c2': choices[1],
        'c3': choices[2],
        'c4': choices[3],
        'c5': choices[4],
        'c6': choices[5],
        'c7': choices[6],
        'c8': choices[7],
        'c9': choices[8],
        'c10': choices[9],
    }

    return render(request, 'add_choices_user.html', context)

@login_required
def choose(request):
    currentDecision = Decision.objects.filter(author=request.user).order_by('-timestamp')[0]
    choices = Choice.objects.filter(decision=currentDecision)

    context = {
        'choices': choices,
    }

    return render(request, 'choose.html', context=context)

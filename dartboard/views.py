from dartboard.models import Decision, Choice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from dartboard.forms import SetDecisionForm, AddChoicesForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import DeleteView, CreateView

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

class ChoicesByAuthorListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Choice
    template_name ='dartboard/choice_list_author.html'
    paginate_by = 10

    def get_queryset(self):
        return Choice.objects.filter(author=self.request.user)

@login_required
def set_decision_user(request):
    #Deletes old choices
    Choice.objects.filter(author=request.user).delete()
    #Deletes old decision
    Decision.objects.filter(author=request.user).delete()

    decision = Decision()
    decision.author = request.user
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SetDecisionForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            decision.name = form.cleaned_data['name']
            decision.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('add-choices-user')) #should redirect to enter choices page

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_name = 'What to eat for dinner'
        form = SetDecisionForm(initial={'name': proposed_name})

    context = {
        'form': form,
        'decision': decision,
    }

    return render(request, 'dartboard/set_decision_user.html', context)

@login_required
def add_choices_user(request):

    choices = [Choice(), Choice(), Choice(), Choice(), Choice()]

    for choice in choices:
        choice.author = request.user

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

            for choice in choices:
                choice.decision = Decision.objects.filter(author=request.user)[0]
                if choice.name is not '':
                    choice.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index')) #should redirect to enter choices page

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_name = 'What to eat for dinner'
        form = AddChoicesForm(initial={'c1': "Enter", 'c2': "Your", 'c3': "Desired", 'c4': "Choices", 'c5': "Here"})

    context = {
        'form': form,
        'c1': choices[0],
        'c2': choices[1],
        'c3': choices[2],
        'c4': choices[3],
        'c5': choices[4],
    }

    return render(request, 'dartboard/add_choices_user.html', context)

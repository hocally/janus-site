from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import DeleteView, CreateView
import json
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def personal_index(request):
    return render(request, 'personal_index.html')

def power_distribution_module(request):
    return render(request, 'power_distribution_module.html')

def ride_height_sensor(request):
    return render(request, 'ride_height_sensor.html')

def strain_gauge_amp(request):
    return render(request, 'strain_gauge_amp.html')

def slip_angle_sensor(request):
    return render(request, 'slip_angle_sensor.html')

def khab_2018(request):
    return render(request, 'khab_2018.html')

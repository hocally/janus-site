from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

app_name="personal_homepage"
urlpatterns = [
    path('', views.personal_index, name='index'),
    path('projects/power-distribution-module/', views.power_distribution_module, name='power-distribution-module'),
    path('projects/ride-height-sensor/', views.ride_height_sensor, name='ride-height-sensor'),
    path('projects/strain-gauge-amp/', views.strain_gauge_amp, name='strain-gauge-amp'),
    path('projects/slip-angle-sensor/', views.slip_angle_sensor, name='slip-angle-sensor'),
    path('projects/khab-2018/', views.khab_2018, name='khab-2018'),
]

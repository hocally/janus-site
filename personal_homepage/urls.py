from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

app_name="personal_homepage"
urlpatterns = [
    path('', views.personal_index),
]

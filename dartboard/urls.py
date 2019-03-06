from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('choose', views.choose, name='choose'),
    path('set_decision', views.set_decision, name='set_decision'),
    path('add_choices', views.add_choices, name='add_choices'),

]

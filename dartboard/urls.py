from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('choose', views.choose, name='choose'),
    path('set_decision', views.set_decision, name='set_decision'),
    path('add_choices', views.add_choices, name='add_choices'),
    path('mychoices/', views.ChoicesByAuthorListView.as_view(), name='my-choices'),
    path('decision/set/', views.set_decision_user, name='set-decision-user'),
    path('choices/add/', views.add_choices_user, name='add-choices-user'),

]

from django.urls import path
from . import views

app_name="dartboard"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('choose', views.choose, name='choose'),
    path('choices', views.view_choices, name='choices'),
    path('choices/add/', views.add_choices_user, name='add-choices-user'),
    path('signup', views.SignUp.as_view(), name='signup'),
]

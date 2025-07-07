from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name='questions')
]

""" first input = url endpoint name, second input = name of the view you chose in view.py, name = doesn't matter/docs """
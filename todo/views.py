from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView

class TodoView(ListView):
    model=TodoModel
    template_name='list.html'
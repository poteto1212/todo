from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView,DetailView

class TodoView(ListView):
    model=TodoModel
    template_name='list.html'

class Detail(DetailView):
    model=TodoModel
    template_name='detail.html'
from django.urls import path
from .views import TodoView

urlpatterns=[
    path('list/',TodoView.as_view(),name='list'),
    ]
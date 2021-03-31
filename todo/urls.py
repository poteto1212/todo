from django.urls import path
from .views import TodoView,Detail

urlpatterns=[
    path('list/',TodoView.as_view(),name='list'),
    path('detail/<int:pk>/',Detail.as_view(),name='detail')
    ]
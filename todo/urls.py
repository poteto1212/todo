from django.urls import path
from .views import TodoView,Detail,TodoCreateView,TodoDelete,TodoUpdateView

urlpatterns=[
    path('list/',TodoView.as_view(),name='list'),
    path('detail/<int:pk>/',Detail.as_view(),name='detail'),
    path('create/',TodoCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',TodoDelete.as_view(),name='delete'),
    path('update/<int:pk>/',TodoUpdateView.as_view(),name='update')
    
    ]
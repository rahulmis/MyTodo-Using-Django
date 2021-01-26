from django.urls import path
from .views import Home, Delete, UnComplete, Complete

urlpatterns = [
    path('', Home, name='Home'),
    path('delete/<int:id>', Delete, name='Delete'),
    path('complete/<int:id>', Complete, name='Complete'),
    path('uncomplete/<int:id>', UnComplete, name='UnComplete'),
]

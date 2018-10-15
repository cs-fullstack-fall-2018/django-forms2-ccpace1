from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.recipe_list, name='list'),
]
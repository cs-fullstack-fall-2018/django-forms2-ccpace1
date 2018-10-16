from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('recipe/new/', views.recipe_new, name="new")
]
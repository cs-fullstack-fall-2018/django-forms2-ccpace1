from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    form_list = Recipe.objects.all()
    return render(request, 'forms_app/recipe_list.html', {'form_list': form_list})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'forms_app/post_detail.html', {'recipe': recipe})

def recipe_new(request):
    if request.method == "POST":
        recipe = RecipeForm(request.POST)
        if recipe.is_valid():
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe = Recipe
        return redirect(request, 'recipe_detail', {'recipe': recipe})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.published_date = timezone.now()
            recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'forms_app/recipe_edit.html', {'form': form})


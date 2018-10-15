from django.shortcuts import render, redirect
from .forms import RecipeForm

from .models import Recipe


def recipe_list(request):
    form_list = Recipe.objects.all()
    return render(request, 'forms_app/index.html', {'form_list': form_list})

def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
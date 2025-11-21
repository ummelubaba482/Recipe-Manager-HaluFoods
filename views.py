from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Recipe
from .forms import RecipeForm, SignUpForm
from django.db.models import Q

# Admin check
def is_admin(user):
    return user.is_staff


def home(request):
    return render(request, 'registration/home.html')


@login_required
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@user_passes_test(is_admin)
@login_required
def recipe_create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_form.html', {'form': form})


@user_passes_test(is_admin)
@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('recipe_detail', pk=recipe.pk)
    return render(request, 'recipes/recipe_form.html', {'form': form})

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('recipe_list')
    return render(request, 'registration/signup.html', {'form': form})
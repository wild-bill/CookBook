from .models import Recipe
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm

# Create your views here.

def post_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cookbook/post_list.html', {'recipes': recipes})

def post_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'cookbook/post_detail.html',{'recipe':recipe})

def post_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.recipe_yield = request.recipe_yield
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = RecipeForm()
    
    return render(request, 'cookbook/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = RecipeForm(instance=post)
    
    return render(request, 'cookbook/post_edit.html', {'form': form})

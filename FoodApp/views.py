from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from .form import *
from .utils import *

# Create your views here.
def index(request):
    return render(request, "home.html")


def add_recipe(request):

    form = RecipeForm(request.POST, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.save()

            return redirect('Delivery:success')
    context = {'form': form}
    # return render(request, 'Delivery/create.html', context)


def save_recipe_to_db(recipe_dict):
    for data in recipe_dict:
        new_instance = Recipe()
        new_instance.title = data['title']
        new_instance.link = data['link']
        new_instance.ingredients = data['ingredients']
        new_instance.source = data['source']
        new_instance.rating = data['rating']
        new_instance.reviews = data['reviews']
        new_instance.total_time = data['total_time']
        new_instance.thumbnail = data['thumbnail']
        new_instance.price = data['rating'] * 1000
        new_instance.save()


def recipe(request):
    search = ""
    if request.method == "POST":
        rep = request.POST.get('recipe')
        rep = str(rep).lower()
        try:
            if not Searches.objects.filter(search__icontains=rep):
                new_instance = Searches()
                new_instance.search = rep
                new_instance.save()
                recipe_dict = get_recipe(rep)
                save_recipe_to_db(recipe_dict)
                search = rep
        except Exception as E:
            search = rep
    recipes = Recipe.objects.filter(title__icontains=search)
    print(recipes)
    pages = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = pages.get_page(page_number)
    context = {'page': page, 'data': recipes}
    return render(request, "Food/recipe.html", context)


def single_recipe(request, id):
    try:
        get_usd = get_usd_rate()
        get_usd = get_usd['rates']['NGN']
    except Exception as E:
        get_usd = 800
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe, 'get_usd':get_usd}
    return render(request, "Food/single_recipe.html", context)


def restaurants(request):
    restaurants = Restaurant.objects.all()
    curr = get_location(request)
    print(curr)
    context = {'restaurants': restaurants, 'nearby_rest': curr}
    return render(request, "Food/restaurant.html", context)


def single_restaurants(request, id):
    restaurant = Restaurant.objects.get(id=id)
    context = {'restaurant': restaurant}
    return render(request, "Food/single_restaurant.html", context)

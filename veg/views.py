from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'recipes/index.html')

@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description
        )

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'Recipes': queryset}

    return render(request, 'recipes/recipes.html', context = context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()

    return redirect('/recipes/')

def update(request, id):
    queryset = Recipe.objects.get(id = id)
    

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        queryset.save()

        return redirect('/recipes/')
    
    context = {'recipe' : queryset}
    
    return render(request, 'recipes/update.html', context = context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # user = User.objects.filter(username = username)
        # if not user.exists():
        #     messages.error(request, 'Invalid Username')
        #     return redirect('/login/')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
        
    return render(request, 'recipes/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')

    return render(request, 'recipes/register.html')
    
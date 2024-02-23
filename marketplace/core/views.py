from django.shortcuts import render, redirect
from item.models import Category, Item
from blog.models import Post
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q



def logout_view(request):
    logout(request)
    return redirect('/login/')


def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    posts = Post.objects.all()
    categories = Category.objects.all()
    filled_categories = Category.objects.filter()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'posts': posts,
        'filled_categories': filled_categories,
    })


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Добро пожаловать, {username}, Ваш аккаунт успешно создан!')
            return redirect('/login/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

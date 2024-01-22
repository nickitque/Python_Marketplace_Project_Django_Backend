from django.shortcuts import render, redirect
from item.models import Category, Item
from blog.models import Post
from .forms import SignUpForm
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/login/')


def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'posts': posts,
    })


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

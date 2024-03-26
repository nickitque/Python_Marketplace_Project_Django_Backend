from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from item.models import Item
from blog.models import Post


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    posts = Post.objects.filter(likes=request.user)
    return render(request, 'dashboard/index.html', {
        'items': items,
        'posts': posts,
    })



@login_required
def account(request):
    items = Item.objects.filter(created_by=request.user)
    posts = Post.objects.filter(likes=request.user)
    return render(request, 'dashboard/account.html', {
        'items': items,
        'posts': posts,
    })


@login_required
def favorites(request):
    items = Item.objects.filter(created_by=request.user)
    liked_items = Item.objects.filter(liked_by=request.user)
    posts = Post.objects.filter(likes=request.user)
    return render(request, 'dashboard/favorites.html', {
        'items': items,
        'liked_items': liked_items,
        'posts': posts,
    })


@login_required
def moderation(request):
    items = Item.objects.filter(is_moderated=False).order_by('created_at').reverse()
    return render(request, 'dashboard/moder.html', {
        'items': items,
    })

def seller_detail(request, pk):
    user = User.objects.get(pk=pk)
    items = Item.objects.filter(created_by=user.id, is_moderated=True)
    return render(request, 'dashboard/seller_detail.html', {
        'user': user,
        'items': items,

    })

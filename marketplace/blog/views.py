from django.shortcuts import render
from django.views.generic import RedirectView
from .models import Post, Comment


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    return render(request, "blog/index.html", {
        "posts": posts,
    })


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blogpost_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)


# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         pk = self.kwargs.get("pk")
#         obj = Post.objects.get(pk=pk)
#         return obj.get_absolute_url()

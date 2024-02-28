from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView
from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    logged_user = request.user
    return render(request, "blog/index.html", {
        "posts": posts,
        "logged_user": logged_user,
    })


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
        "logged_user": request.user,
    }
    return render(request, "blog/category.html", context)


def blogpost_detail(request, slug):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()

    else:
        comment_form = CommentForm()

    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, "blog/detail.html", context)


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print(slug)
        obj = Post.objects.get(slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


def like_post(request):
    """Is not used right now"""
    post_id = request.POST.get('post_id', '')
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('blog_index')

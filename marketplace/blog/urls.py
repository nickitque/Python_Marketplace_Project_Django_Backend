from django.urls import path
from . import views
from .views import PostLikeRedirect

app_name = 'blog'


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<slug:slug>/", views.blogpost_detail, name="blogpost_detail"),
    path("post/<slug:slug>/like/", PostLikeRedirect.as_view(), name="like"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]
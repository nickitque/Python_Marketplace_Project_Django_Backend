from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag('blog/blog_navbar.html')
def blog_navbar():
    posts = Post.objects.all().order_by("-created_on")
    return {'posts': posts}

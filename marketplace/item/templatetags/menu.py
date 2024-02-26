from django import template
from item.models import Item, Category


register = template.Library()


@register.inclusion_tag('item/menu.html')
def menu():
    categories = Category.objects.all()
    return {'categories': categories}

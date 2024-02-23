from django import template
from item.models import Item


register = template.Library()


@register.inclusion_tag('dashboard/menu.html')
def menu_dashboard():
    items = Item.objects.all()
    return {'items': items}

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    pagination_items = Item.objects.filter(is_sold=False)
    items = Item.objects.filter(is_sold=False).order_by('created_at').reverse()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # paginator code
    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, 'item/items.html', {
        'items': items,
        'pagination_items': pagination_items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def category_detail(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    category_id = request.GET.get('category', 0)
    items = category.items.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    return render(request, 'item/category_detail.html', {
        'category': category,
        'items': items,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, category_slug, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    price_usd = item.price * 0.31
    price_byn = item.price / 0.31

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'price_usd': price_usd,
        'price_byn': price_byn,
    })


class ItemLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        category = self.kwargs.get("slug")
        pk = self.kwargs.get("pk")
        obj = Item.objects.get(pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.liked_by.all():
                obj.liked_by.remove(user)
            else:
                obj.liked_by.add(user)
        return url_


def like_item(request, pk):
    item = get_object_or_404(Item, id=pk)

    if item.liked_by.filter(id=request.user.id).exists():
        item.liked_by.remove(request.user)
    else:
        item.liked_by.add(request.user)


@login_required()
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', category_slug=item.category.slug, id=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required()
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', category_slug=item.category.slug, pk=item.pk)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

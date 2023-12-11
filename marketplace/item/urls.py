from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new.html/', views.new, name='new'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/delete', views.delete, name='delete'),
    path('<slug:slug>/edit', views.edit, name='edit'),
]
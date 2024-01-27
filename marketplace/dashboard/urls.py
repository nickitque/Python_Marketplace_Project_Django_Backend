from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('seller/<slug:pk>', views.seller_detail, name='seller_detail')
]

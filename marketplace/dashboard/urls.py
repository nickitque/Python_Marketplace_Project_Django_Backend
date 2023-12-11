from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('seller/<int:pk>', views.vendor_detail, name='vendor_detail')
]
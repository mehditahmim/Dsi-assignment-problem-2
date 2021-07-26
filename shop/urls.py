from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('productList/', views.home, name='home'),
    path('productList/sort_low_to_high', views.sortLowtoHigh, name='sortLowtoHigh'),
]
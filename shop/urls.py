from django.urls import path
from .views import category_list, product_list, product_detail

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
    path('products/<slug:slug>/',product_detail,name='product_detail'),
]

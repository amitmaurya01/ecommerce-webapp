from django.urls import path
from .views import category_list, product_list, product_detail,add_to_cart,view_cart

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
    path('products/<slug:slug>/',product_detail,name='product_detail'),
    path('cart/', view_cart, name='view_cart'),  # Cart view
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]

from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_list')

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})
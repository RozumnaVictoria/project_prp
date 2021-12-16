from django.shortcuts import render, redirect
from product.models import Kind
from cart.forms import CartForm


def main(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'index.html')


def menu(request):
    cart_form = CartForm
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'menu.html', {'product_list': Kind.objects.all(), 'cart_form': cart_form})




from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView

from apps.cart.forms import CartAddProductForm
from apps.shop.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/shop-single.html'
    context_object_name = 'product'
    cart_product_form = CartAddProductForm()


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/shop-single.html', {'product': product,
                                                     'cart_product_form': cart_product_form})




class MainPageView(TemplateView):
    template_name = 'shop/index.html'

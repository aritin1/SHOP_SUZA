from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView

from apps.cart.forms import CartAddProductForm
from apps.shop.models import Product


def product_list(request):
    gender = request.GET.get('gender', 'all')
    products = Product.objects.all()
    if gender == 'men':
        products = products.filter(gender='Men')
    elif gender == 'women':
        products = products.filter(gender='Women')
    return render(request, 'shop/shop.html', {'products': products, 'gender': gender})


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

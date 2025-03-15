from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from apps.shop.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})

class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/shop-single.html'
    context_object_name = 'product'



class MainPageView(TemplateView):
    template_name = 'shop/index.html'

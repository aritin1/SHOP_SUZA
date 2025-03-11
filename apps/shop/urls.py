from django.urls import path
from .views import product_list, ProductDetail, MainPageView

urlpatterns = [
    path('list/', product_list, name='products-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='shop-single'),
    path('', MainPageView.as_view(), name='main'),
    # path('list/', ProductsListView.as_view(), name='products-list'),
]
from django.urls import path
from .views import product_list, ProductDetail, MainPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/', product_list, name='products-list'),
    path('product/<int:pk>/',  ProductDetail.as_view(), name='product-detail'),
    path('', MainPageView.as_view(), name='main'),
    # path('list/', ProductsListView.as_view(), name='products-list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
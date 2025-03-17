# from django.urls import path
# from apps.cart.views import cart_add, cart_detail, cart_remove
#
# app_name = 'cart'
#
# urlpatterns = [
#     path('', cart_detail, name='cart_detail'),
#     path('add/<int:product_id>/', cart_add, name='cart_add'),
#     path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
# ]
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
]
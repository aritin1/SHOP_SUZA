from django.urls import path

from apps.users.views import register_view, login_view, custom_logout, account_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path("account/", account_view, name="account"),

]
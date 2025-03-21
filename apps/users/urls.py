from django.urls import path

from apps.users.views import register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
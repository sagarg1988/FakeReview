from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from reviews.views import add_review, product_list, contactus, aboutus, services
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [

    path('contactus/', contactus, name='contactus'),
    path('aboutus/', aboutus, name='aboutus'),
    path('services/', services, name='services'),
    path('add_review/', add_review, name='add_review'),
    path('product_list/', product_list, name='product_list'),
]

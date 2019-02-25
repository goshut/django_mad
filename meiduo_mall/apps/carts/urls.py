from django.conf.urls import url

from . import views

urlpattern = [
    url(r'^carts/$', views.CartView.as_view()),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/(?P<category_id>\d+)/skus/$', views.SKUListView.as_view()),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryView.as_view()),
]

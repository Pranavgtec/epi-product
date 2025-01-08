from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_scheme_manage, name='product_scheme_manage'),
]

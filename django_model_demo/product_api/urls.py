
from django.urls import path

from . import views as v

app_name = 'product_api'

urlpatterns = [
    path('products/', v.product_list, name='product_list'),
    path('products/<int:pk>/', v.product_detail, name='product_detail'),
]

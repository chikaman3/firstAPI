from django.urls import path
from .views import ProductListCreateView , ProductDetailView


urlpatterns = [
    path('product/', ProductListCreateView.as_view() , name = 'product'),
    path('detail/<int:pk>', ProductDetailView.as_view() , name = 'detail'),
]

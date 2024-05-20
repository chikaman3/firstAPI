from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
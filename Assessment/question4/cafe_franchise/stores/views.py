from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsManager, IsOwner
from .models import Cafe, StoreOrders
from .serializers import CafeSerializer, StoreOrderSerializer

# Create your views here.

class CafeList(generics.ListCreateAPIView):
    permission_classes = (IsOwner,)
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

# class OrderList(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated)
#     queryset = StoreOrders.objects.all()
#     serializer_class = StoreOrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, IsManager,)
    queryset = StoreOrders.objects.all()
    serializer_class = StoreOrderSerializer
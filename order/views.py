from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        coustomer_id=self.request.query_params.get("coustomer_id")
        if coustomer_id:
            queryset=queryset.filter(coustomer_id=coustomer_id)
        return queryset

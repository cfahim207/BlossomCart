from django.shortcuts import render
from .models import Flower,FlowerColor,CategoryFlower,Review
from rest_framework import viewsets
from .serializer import FlowerSerializer,CategorySerializer,ColorSerializer,ReviewSerializer
from rest_framework import filters, pagination
# Create your views here.

class FlowerPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class FlowerViewset(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    pagination_class=FlowerPagination
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get("id")
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryFlower.objects.all()
    serializer_class = CategorySerializer
class ColorViewset(viewsets.ModelViewSet):
    queryset = FlowerColor.objects.all()
    serializer_class = ColorSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
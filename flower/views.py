from django.shortcuts import render
from .models import Flower,FlowerColor,CategoryFlower,Review
from rest_framework import viewsets
from .serializer import FlowerSerializer,CategorySerializer,ColorSerializer,ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination
# Create your views here.

class FlowerViewset(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        # Only allow admin to delete a flower
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to delete this flower."}, status=403)
        return super().destroy(request, *args, **kwargs)
    
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
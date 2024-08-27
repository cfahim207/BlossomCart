from rest_framework import serializers
from .models import Flower,FlowerColor,CategoryFlower,Review

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flower
        fields="__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryFlower
        fields="__all__"
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlowerColor
        fields="__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
    

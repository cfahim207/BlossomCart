from rest_framework import serializers
from .models import Flower,FlowerColor,CategoryFlower,Review

class FlowerSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    color=serializers.StringRelatedField(many=True)
    class Meta:
        model= Flower
        fields=['category','color','image','name','price']
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryFlower
        fields="__all__"
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlowerColor
        fields="__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    # flower = serializers.StringRelatedField(many=False)
    
    class Meta:
        model=Review
        fields="__all__"
    

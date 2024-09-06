from rest_framework import serializers
from .models import Flower,FlowerColor,CategoryFlower,Review

class FlowerSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=CategoryFlower.objects.all())  # For writing
    category_display = serializers.StringRelatedField(many=True, source='category', read_only=True)  # For reading
    color = serializers.PrimaryKeyRelatedField(many=True, queryset=FlowerColor.objects.all())  # For writing
    color_display = serializers.StringRelatedField(many=True, source='color', read_only=True)  # For reading

    class Meta:
        model = Flower
        fields = ['id','category', 'category_display', 'color', 'color_display', 'image', 'name', 'price']


        
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
    flower = serializers.StringRelatedField(many=False)
    
    class Meta:
        model=Review
        fields="__all__"
    

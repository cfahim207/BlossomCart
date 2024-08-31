from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Order
        fields='__all__'
        
    def create(self,validated_data):
        flower=self.validated_data["flower"]
        buyer=self.validated_data["coustomer"]
        
        if buyer.balance<flower.price:
            raise serializers.ValidationError({'error': "Insufficient balance"})
        else:
            buyer.balance-=flower.price
            buyer.save()
    
        order=Order(**validated_data)
        order.save()
        return order
    
        
        
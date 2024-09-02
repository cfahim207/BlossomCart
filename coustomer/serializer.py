from rest_framework import serializers
from .models import Coustomer,Deposite
from django.contrib.auth.models import User

class CoustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model= Coustomer
        fields='__all__'
        
class DepositTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposite
        fields = ['coustomer', 'amount', 'timestamp']
    
    def create(self,validated_data):
        coustomer=validated_data["coustomer"]
        amount=validated_data["amount"]
        coustomer.balance+=amount
        coustomer.save()
    
        deposit=Deposite(**validated_data)
        deposit.save()
        return deposit
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    image = serializers.ImageField(required=False)  # Image might be optional
    mobile_no = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'image', 'mobile_no']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        image = validated_data.get('image')
        mobile_no = validated_data['mobile_no']

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.is_active = False  # Assuming you want the user to be inactive initially
        user.save()

        # Create the related Customer object
        Coustomer.objects.create(
            user=user,
            image=image,
            mobile_no=mobile_no
        )

        return user
    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','email','is_superuser','date_joined']
    
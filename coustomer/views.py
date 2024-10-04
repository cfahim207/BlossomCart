from django.shortcuts import render
from rest_framework import viewsets
from .models import Coustomer,Deposite
from .serializer import CoustomerSerializer,RegistrationSerializer,UserLoginSerializer,DepositTransactionSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from flower.models import Flower,FlowerColor,CategoryFlower,Review
from flower.serializer import FlowerSerializer,ColorSerializer,CategorySerializer,ReviewSerializer
from order.models import Order
from order.serializer import OrderSerializer
from contact_us.models import ContactUs
from contact_us.serializer import ContactUsSerializer
# Create your views here.
class CoustomerViewset(viewsets.ModelViewSet):
    queryset=Coustomer.objects.all()
    serializer_class=CoustomerSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get("id")
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class DepositeViewset(viewsets.ModelViewSet):
    queryset=Deposite.objects.all()
    serializer_class=DepositTransactionSerializer  
    

class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f'https://blossom-cart-8wo2.vercel.app/coustomer/active/{uid}/{token}'
            email_subject="Confirm Your Email"
            email_body=render_to_string("confirm_email.html",{'confirm_link': confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response('Check your mail for confirmation')
        return Response(serializer.errors)


def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("https://cfahim207.github.io/BlossomCart-Frontend/login.html")
    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            
            user=authenticate(username=username,password=password)
            
            
            if user:
                token,_=Token.objects.get_or_create(user=user)
                coustomer,_=Coustomer.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token': token.key,'user_id': user.id,'coustomer_id':coustomer.id})

            else:
                return Response({'error':'Invalid Credential'})
        
        return Response(serializer.errors)
    
class UserlogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")
    

class DashboardView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # Admin Dashboard
            coustomer = Coustomer.objects.all()
            deposite = Deposite.objects.all()
            orders = Order.objects.all()
            flower=Flower.objects.all()
            color=FlowerColor.objects.all()
            category=CategoryFlower.objects.all()
            review=Review.objects.all()
            contactus=ContactUs.objects.all()
            

            return Response({
                "coustomer": CoustomerSerializer(coustomer, many=True).data,
                "user": UserSerializer(request.user).data,
                "deposite": DepositTransactionSerializer(deposite, many=True).data,
                "orders": OrderSerializer(orders, many=True).data,
                "flower": FlowerSerializer(flower, many=True).data,
                "color": ColorSerializer(color, many=True).data,
                "category": CategorySerializer(category, many=True).data,
                "review": ReviewSerializer(review, many=True).data,
                "contactus": ContactUsSerializer(contactus, many=True).data
            })
        else:
            # Regular User Dashboard
            coustomer = request.user.coustomer
            deposite = Deposite.objects.filter(coustomer=coustomer)
            orders = Order.objects.filter(coustomer=coustomer)
            

            return Response({
                "profile": CoustomerSerializer(coustomer).data,
                "user": UserSerializer(request.user).data,
                "deposite": DepositTransactionSerializer(deposite, many=True).data,
                "orders": OrderSerializer(orders, many=True).data
            })
            
            

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
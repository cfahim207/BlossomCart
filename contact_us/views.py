from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializer import ContactUsSerializer
# Create your views here.

class ContactUsViewset(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
    def perform_create(self, serializer):
        # Save the order instance
        order = serializer.save()

        # Send an email to the customer
        email_subject="Congratulation for successfully Ordered.."
        email_body=render_to_string("order.html",{'user':order.coustomer.user, 'flower':order.flower})
        email=EmailMultiAlternatives(email_subject,'',to=[order.coustomer.user.email])
        email.attach_alternative(email_body,'text/html')
        email.send()
        
        
    def get_queryset(self):
        queryset=super().get_queryset()
        coustomer_id=self.request.query_params.get("coustomer_id")
        if coustomer_id:
            queryset=queryset.filter(coustomer_id=coustomer_id)
        return queryset
 
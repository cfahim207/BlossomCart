from django.contrib import admin
from .models import Order
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['flower_name','coustomer_name','order_status']
    
    def flower_name(self,obj):
        return obj.flower.name
    def coustomer_name(self,obj):
        return obj.coustomer.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.order_status== "Complete":
            email_subject="Your Product is successfully Delivered"
            email_body=render_to_string("admin_email.html",{'user':obj.coustomer.user, 'flower':obj.flower})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.coustomer.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
admin.site.register(Order,OrderAdmin)
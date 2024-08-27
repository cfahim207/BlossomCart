from django.contrib import admin
from .models import Coustomer
# Register your models here.
class CoustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','mobile_no']
    
    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(Coustomer,CoustomerAdmin)
from django.contrib import admin
from .import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':
        ('name',),}
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':
        ('name',),}
    
admin.site.register(models.CategoryFlower,CategoryAdmin)
admin.site.register(models.FlowerColor,ColorAdmin)
admin.site.register(models.Flower)
admin.site.register(models.Review)
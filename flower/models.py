from django.db import models
from coustomer.models import Coustomer
# Create your models here.
class CategoryFlower(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
class FlowerColor(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Flower(models.Model):
    image=models.ImageField(upload_to="flower/images")
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    color=models.ManyToManyField(FlowerColor)
    category=models.ManyToManyField(CategoryFlower)
    
    def __str__(self):
        return f"{self.name}"

STAR_CHOICE=[
    
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
    
class Review(models.Model):
    image=models.ImageField(upload_to="flower/images",default=True)
    name=models.CharField(max_length=20)
    flower=models.ForeignKey(Flower,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICE, max_length=10)
    
    def __str__(self):
        return self.name
    
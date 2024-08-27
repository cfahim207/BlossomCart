from django.db import models
from coustomer.models import Coustomer
from flower.models import Flower,FlowerColor
# Create your models here.

ORDER_STATUS=[
    ('Complete','Complete'),
    ('Pending','Pending'),
]
class Order(models.Model):
    flower=models.ForeignKey(Flower,on_delete=models.CASCADE)
    coustomer=models.ForeignKey(Coustomer,on_delete=models.CASCADE)
    order_status=models.CharField(choices=ORDER_STATUS,max_length=10,default="Pending")
    cancel=models.BooleanField(default=False)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Coustomer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='coustomer/image/',default=False) 
    mobile_no=models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"
    
class Deposite(models.Model):
    coustomer=models.ForeignKey(Coustomer,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.coustomer.user.username} - {self.amount} on {self.timestamp}"
    
    
    
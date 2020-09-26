from django.db import models
from datetime import datetime

class Agent(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    description=models.TextField(blank=True)
    phone_no=models.IntegerField()
    email=models.CharField(max_length=200)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
    num_prop=models.IntegerField()
     
    
    def __str__(self):
        return self.name

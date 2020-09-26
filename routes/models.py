from django.db import models
from datetime import datetime
from agents.models import Agent

class Testemonial(models.Model):
    seller=models.ForeignKey(Agent,on_delete=models.DO_NOTHING)  
    client=models.CharField(max_length=200)
    emp_status=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    rating=models.IntegerField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
  
    
    def __str__(self):
        return self.client
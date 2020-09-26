from django.db import models
from datetime import datetime
from agents.models import Agent
# reference from brad traversy's btre project
class Property(models.Model):
    seller=models.ForeignKey(Agent,on_delete=models.DO_NOTHING)  
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    zipcode=models.IntegerField()
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    areaSqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    is_forSale=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    property_date=models.DateTimeField(default=datetime.now,blank=True)
    built_year= models.IntegerField()
    storey = models.IntegerField()
    Terrace = models.BooleanField(default= False)
    
    def __str__(self):
        return self.title
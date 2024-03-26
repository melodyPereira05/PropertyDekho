from django.shortcuts import render
from django.http import HttpResponse
from properties.models import Property
from agents.models import Agent
from .data_searching import statess,price_choices
from routes.models import Testemonial


def index(request):
    testemonial=Testemonial.objects.all()[:3]
    context={
        'properties': Property.objects.filter(is_featured=True)[:3],
        'sellers':Agent.objects.all(),
        'states' : statess,
        'prices' :price_choices,
        'testemonial':testemonial
        
    }
    
    return render(request,'index.html',context)
    

def about(request):
    return render(request,'about.html')
    

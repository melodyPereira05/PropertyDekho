from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from  routes.data_searching import statess,price_choices
from routes.models import Testemonial
# Create your views here.


def index(request): 
     #fetching data from database
    properties=Property.objects.order_by('-property_date')  #latest date
    paginator = Paginator(properties, 6) # Show 25 contacts per page.
   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context={
        'properties': page_obj,
             
     }
    return render(request,'Allproperties.html',context)   #mvc model
    
    
    
    
def properties(request,property_id):
    sproperty=get_object_or_404(Property,pk=property_id)
    context={
        'sproperty':sproperty
    }
    return render(request,'propertySinglePage.html', context )
    
    
def search(request):
    property_filters=Property.objects.order_by('-property_date')
    
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            property_filters=property_filters.filter(description__icontains=keywords)
            
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            property_filters=property_filters.filter(state__iexact=state)
            
    # if 'bedrooms' in request.GET:
    #     bedrooms=request.GET['bedrooms']
    #     if bedrooms:
    #         property_filters=property_filters.filter(bedrooms__lte=bedrooms)
            
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            property_filters=property_filters.filter(price__lte=price)
            
    # if 'bedrooms' in request.GET:
    #     bedrooms=request.GET['bedrooms']
    #     if bedrooms:
    #         property_filters=property_filters.filter(bedrooms__lte=bedrooms)
            
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            property_filters=property_filters.filter(city__iexact=city)        
    
    context ={
        'states' : statess,
        'prices' :price_choices,
        'properties':property_filters,
        'values':request.GET
    }
    return render(request,'search.html', context)
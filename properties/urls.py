from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='all-property'),
    path('<int:property_id>/', views.properties, name="property"),
    path('search/',views.search,name="property-search"),
    
]
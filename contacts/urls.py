from django.urls import path
from  . import views


urlpatterns = [
  
    path('<int:sproperty_id>/',views.contact,name="contact"),
    path('',views.contact_submit,name="contact-submit"),
    
]
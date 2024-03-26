from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from properties.models import Property
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request,sproperty_id):
    sproperty=get_object_or_404(Property,pk=sproperty_id)
    context={
        'sproperty':sproperty,
         #'title': sproperty.title 
    }
    return render(request,'contact.html',context)


def contact_submit(request):
    if request.method=='POST':
        property_id=request.POST['property_id']
        property_name=request.POST['property_title']
        name=request.POST['name']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        email=request.POST['email']
        #seller_email=request.POST['seller_email']
        message=request.POST['message']
        
        #check if user has already make enquiry
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(property_id=property_id,user_id=user_id)
            if has_contacted:
                messages.add_message(request, messages.ERROR,'You have already made an enquiry for this property')
                return redirect('/properties/'+property_id)
                
        
        #create instance of the class contact
        contact =Contact(property_name=property_name,property_id=property_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        
        #sending email
        # send_mail(
        #         'Property Enquiry',
        #         'There was an enquiry made for the property',
        #         'melzpereira0509@gmail.com',
        #         ['melodypereira05@gmail.com','answeetapereira13@gmail.com'],
        #         fail_silently=False
        #     )
        
        
        messages.add_message(request, messages.SUCCESS, 'YOUR Enquiry has been submitted, the Seller will get back to you soon. Thank you')
        return redirect('dashboard')
        
    messages.add_message(request, messages.ERROR, 'There was some issue parsing your request,please try again')
    return redirect('dashboard')
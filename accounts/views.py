from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact

def register(request):
    if request.method =='POST':
        #getting form values
        
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        #validation
        
        if password1==password2:
            
            #check username no duplicate.
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    
                    user.save();  #save user to db
                    messages.add_message(request, messages.SUCCESS, 'You are now register, please log in')
                    return redirect('login')
                    
            
        else :
            messages.add_message(request, messages.ERROR, 'passwords do not match')
            return redirect('register')
        
    else :
        redirect('register')
    return render(request,'register.html')
    
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)   #login the user
            messages.add_message(request, messages.SUCCESS, 'You are now logged in')
            return redirect('home-page')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            
            
            
           
        return redirect('login')
    else :
        redirect('login')
    return render(request,'login.html')
    
def logout(request):
    if request.method =='POST':
        auth.logout(request)  #logout user
        messages.add_message(request, messages.SUCCESS, 'You are now logged Out')
    return redirect('home-page')
    


def dashboard(request):
    contact_dashboard=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)  
   
    context={
        'contacts':contact_dashboard
      
    }
    return render(request,'dashboard.html',context)
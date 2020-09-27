from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

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
           
        return redirect('home-page')
    else :
        redirect('login')
    return render(request,'login.html')
    
def logout(request):
    return redirect('home-page')
    

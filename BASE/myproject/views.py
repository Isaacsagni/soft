from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request, 'index.html') # home page rendered

def services(request):

    return render(request, 'services.html')



def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')

            
    else:
        
      
      return render(request, 'signin.html')





def signup (request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        username = request.POST['username']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email taken')
                return redirect('signup')
                
            else:
                 user = User.objects.create_user(username=username, password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 messages.success(request, 'User created successfully')
                 return redirect('signin')
        else:
             messages.error(request, 'Passwords do not match')
             return redirect('signup')
    else:
        return render(request, 'signup.html')

 
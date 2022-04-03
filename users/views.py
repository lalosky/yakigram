from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def signup(request):
    if request.method=='POST':
        form = request.POST
        if request.POST.get('passwd') == request.POST.get('passwd_confirmation'):

            username = request.POST['username']
            password= request.POST['passwd']
            
            user = User(username= username, password = password)
            
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST.get('email')
            try:
                user.save()
                profile = Profile(user = user)
                profile.save()
                return redirect('list_posts')
            except IntegrityError:      
                return render(request, 'users/signup.html', {'error':'usuario ya esta en uso'})        
            
            
           
        return render(request, 'users/signup.html', {'error':'Error en el formulario'})

    return render(request, 'users/signup.html')
from users.models import Profile
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method=='POST':
        form = request.POST
        if request.POST.get('passwd') == request.POST.get('passwd_confirmation'):

            username = request.POST['username']
            password= request.POST['passwd']
            
            user = User.objects.create_user(username= username, password = password)
            
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST.get('email')
            try:
                user.save()
                profile = Profile(user = user)
                profile.save()
                return redirect('login_view')
            except IntegrityError:      
                return render(request, 'users/signup.html', {'error':'usuario ya esta en uso'})        
            
            
           
        return render(request, 'users/signup.html', {'error':'Error en el formulario'})

    return render(request, 'users/signup.html')
def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username =request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request,user)
            return redirect('list_posts')
        else:
            return render(request, 'users/login.html', {'error':'Clave invalidad o usuario'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')
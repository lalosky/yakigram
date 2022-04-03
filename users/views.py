from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

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
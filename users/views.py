from django.shortcuts import render

# Create your views here.


def login_view(request):
    print('que rompiiiiiiiiiiiiiiiiiiiii')
    return render(request, 'users/login.html')
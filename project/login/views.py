from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def user_join(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            success = "Successfully created account."
            return render(request, 'join.html', {'success': success})
        else:
            error = "Try another username or email."
            return render(request, 'join.html', {'error': error})
    return render(request, 'join.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Invalid username or password.'
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')

@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    return redirect('/login')

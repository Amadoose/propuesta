from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('ventas')  # Fixed: redirect to existing URL
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('ventas')  # Fixed: redirect to existing URL
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')
   
    return render(request, 'login.html')  # Fixed: proper login template

@login_required
def dashboard_view_ventas(request):
    return render(request, 'dashboard/ventas.html')

@login_required
def dashboard_view_performance(request):
    return render(request, 'dashboard/performance.html')

@login_required
def dashboard_view_3(request):
    return render(request, 'dashboard/3.html')

@login_required
def dashboard_view_4(request):
    return render(request, 'dashboard/4.html')

def logout_view(request):
    """Custom logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
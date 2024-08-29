from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register_user(request):
    form =UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully registered")
            return redirect('userauth:login')
            
    context = {
        "form": form,
    }
    return render(request,'register.html',context=context)


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("app:dashboard")
    context = {
        "form": form,
    }    
    return render(request,'login.html',context=context)


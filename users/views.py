from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login,authenticate, logout
# Create your views here.

def login_user(request):
	form=CustomUserCreationForm
	if request.method=="POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		remember_me=request.POST.get('remember-me')
		user = authenticate(request, email=email, password=password)
		form = CustomUserCreationForm(request.POST)
		if user is not None:
			login(request, user)
			return redirect("dashboard")
		else:
			message="*Wrong login details, please try again"
			return render(request,"login.html",{"message":message})
	else:
		print("no form")
		return render(request,"login.html",{"form":form})


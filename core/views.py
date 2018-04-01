from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
	return render(request, "core/home.html")

def signup(request):
	return render(request, "core/signup.html")

def signin(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
		return redirect("/admin/")

	return render(request, "core/login.html")
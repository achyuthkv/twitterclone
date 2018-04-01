from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def home(request):
	return render(request, "core/home.html")

def signup(request):
	if request.user.is_authenticated:
		return redirect("/home/")
	if request.method == "POST":
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		try: 
			user = User.objects.get(email=email)
			return render(request, "core/signup.html", {"error": "User with this email already exists."})
		except:
			if password1 == password2:
				#Register
				user = User.objects.create_user(username=email,
												email=email,
												password=password1,
												is_staff = True)
				login(request, user)
				return redirect('/home/')
			else:
				return render(request, "core/signup.html", {"error": "The passwords do not match."})

	return render(request, "core/signup.html")

def signin(request):
	if request.user.is_authenticated:
		return redirect("/home/")
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
		return redirect("/home/")

	return render(request, "core/login.html")

def signout(request):
	logout(request)
	return redirect("/")
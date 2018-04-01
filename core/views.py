from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import Profile



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

def editprofile(request):
	id = request.user.id
	user = User.objects.get(pk=id)
	profile = Profile.objects.get(user=user)
	if not user.is_authenticated:
		return redirect("/login/")

	if request.method == "POST":
		fname = request.POST.get('fname', "First Name")
		lname = request.POST.get('lname', "Last name")
		about = request.POST.get('about', "This is about")
		user.first_name = fname
		user.last_name = lname
		profile.about = about
		user.save()
		profile.save()

		return redirect("/edit/")

	profile = Profile.objects.get(user=request.user)
	print(profile.user, profile.about, profile.dob)
	return render(request, "core/editprofile.html", {"profile":profile})
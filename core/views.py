from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "core/home.html")

def signup(request):
	return render(request, "core/signup.html")

def signin(request):
	return render(request, "core/login.html")
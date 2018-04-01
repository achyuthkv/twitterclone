from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tweetdeck.models import Tweet


def tweeter(request):
	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method=="POST":
		#Create tweet
		text = request.POST.get('tweet')
		tweet = Tweet(text = text, user=request.user)
		tweet.save()
		return redirect("/home/")

	tweets = Tweet.objects.all().order_by('-timestamp')
	return render(request, "tweetdeck/tweeter.html", {"tweets": tweets})

def tweetsof(request, user_id):
	user = User.objects.get(pk=user_id)
	tweets = Tweet.objects.filter(user=user)
	return render(request, "tweetdeck/tweetsof.html", {"tweets": tweets, "profile":user})
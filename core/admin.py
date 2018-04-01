from django.contrib import admin
from core.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'about', 'dob']
	search_fields = ['user']
	
admin.site.register(Profile, ProfileAdmin)

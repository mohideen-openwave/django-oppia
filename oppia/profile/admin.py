# oppia/profile/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from oppia.profile.models import CustomUser


class ProfileAdmin(admin.ModelAdmin):   
    list_display = ('phoneno', 'professional', 'town', 'city', 'state', 'country', 'worktype', 'currentlyworking', 'stafftype', 'familyplaning', 'providedit', 'nurhitraining', 'education', 'religion', 'sex', 'age') #user.email creates the error - tried some variations here, but no luck.

admin.site.register(CustomUser, ProfileAdmin)

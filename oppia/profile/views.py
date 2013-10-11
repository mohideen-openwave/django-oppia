from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate, login, views)
from django.contrib.auth.models import User
#from models import CustomUser 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from tastypie.models import ApiKey
from oppia.models import Points,Award, AwardCourse, Course
from oppia.profile.models import CustomUser
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from forms import RegisterForm, ResetForm, ProfileForm

def register(request):
    if request.method == 'POST': # if form submitted...
        form = RegisterForm(request.POST)        
        if form.is_valid(): # All validation rules pass
            # Create new user
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
        
            #OWC added new field
            phoneno = form.cleaned_data.get("phoneno")            
            current_working_city = form.cleaned_data.get("current_working_city")
            currently_working_facility = form.cleaned_data.get("currently_working_facility")
            staff_type = form.cleaned_data.get("staff_type")
            nurhi_sponsor_training = form.cleaned_data.get("nurhi_sponsor_training")
            current_place_employment = form.cleaned_data.get("current_place_employment")
            highest_education_level = form.cleaned_data.get("highest_education_level")
            religion = form.cleaned_data.get("religion")
            sex = form.cleaned_data.get("sex")
            age = form.cleaned_data.get("age")
            
            
            #OWC Derived from User Super Class and added new fields
            user = CustomUser.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.phoneno = phoneno            
            user.current_working_city = current_working_city            
            user.currently_working_facility = currently_working_facility
            user.staff_type = staff_type
            user.nurhi_sponsor_training = nurhi_sponsor_training
            user.current_place_employment = current_place_employment
            user.highest_education_level = highest_education_level
            user.religion = religion
            user.sex = sex
            user.age = age 
            user.save()
            u = authenticate(username=username, password=password)
            if u is not None:
                if u.is_active:
                    login(request, u)
                    return HttpResponseRedirect('thanks/') # Redirect after POST
            return HttpResponseRedirect('thanks/') # Redirect after POST
    else:
        form = RegisterForm() # An unbound form

    return render(request, 'oppia/profile/register.html', {'form': form,})

#Dump print
"""
           def dump(user):
               for attr in dir(user):
                   print "user.%s = %s" % (attr, getattr(user, attr))
"""
def reset(request):
    if request.method == 'POST': # if form submitted...
        form = ResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username__exact=username)
            newpass = User.objects.make_random_password(length=8)
            user.set_password(newpass)
            user.save()
            if request.is_secure():
                prefix = 'https://'
            else:
                prefix = 'http://'
            # TODO - better way to manage email message content
            send_mail('OppiaMobile: Password reset', 'Here is your new password for OppiaMobile: '+newpass 
                      + '\n\nWhen you next log in you can update your password to something more memorable.' 
                      + '\n\n' + prefix + request.META['SERVER_NAME'] , 
                      settings.SERVER_EMAIL, [user.email], fail_silently=False)
            return HttpResponseRedirect('sent')
    else:
        form = ResetForm() # An unbound form

    return render(request, 'oppia/profile/reset.html', {'form': form,})

def edit(request):    
    key = ApiKey.objects.get(user = request.user)
    if request.method == 'POST':
        
        form = ProfileForm(request.POST,request=request)
        if form.is_valid():
            # update basic data
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")            
            #OWC Additional fields are added
            phoneno = form.cleaned_data.get("phoneno")
            current_working_city = form.cleaned_data.get("current_working_city")
            currently_working_facility = form.cleaned_data.get("currently_working_facility")
            staff_type = form.cleaned_data.get("staff_type")
            nurhi_sponsor_training = form.cleaned_data.get("nurhi_sponsor_training")
            current_place_employment = form.cleaned_data.get("current_place_employment")
            highest_education_level = form.cleaned_data.get("highest_education_level")
            religion = form.cleaned_data.get("religion")
            sex = form.cleaned_data.get("sex")
            age = form.cleaned_data.get("age")
                                  
            
            request.user.email = email
            request.user.first_name = first_name
            request.user.last_name = last_name
            #OWC Additional fields are added
            request.user.phoneno = phoneno
            request.user.current_working_city = current_working_city
            request.user.currently_working_facility = currently_working_facility
            request.user.staff_type = staff_type
            request.user.nurhi_sponsor_training = nurhi_sponsor_training
            request.user.current_place_employment = current_place_employment
            request.user.highest_education_level = highest_education_level            
            request.user.religion = religion
            request.user.sex = sex
            request.user.age = age
            
            
            request.user.save()
            messages.success(request, _(u"Profile updated"))
            
            # if password should be changed
            password = form.cleaned_data.get("password")
            if password:
                request.user.set_password(password)
                request.user.save()
                messages.success(request, _(u"Password updated"))
    else:
        request.user= CustomUser.objects.get(pk=request.user.id)
        
        form = ProfileForm(initial={'username':request.user.username,
                                    'email':request.user.email,
                                    'first_name':request.user.first_name,
                                    'last_name':request.user.last_name,                                    
                                    'phoneno':request.user.phoneno,
                                    'current_working_city':request.user.current_working_city,
                                    'currently_working_facility':request.user.currently_working_facility,
                                    'staff_type':request.user.staff_type,
                                    'nurhi_sponsor_training':request.user.nurhi_sponsor_training,
                                    'current_place_employment':request.user.current_place_employment,
                                    'highest_education_level':request.user.highest_education_level,                                    
                                    'religion':request.user.religion,
                                    'sex':request.user.sex,
                                    'age':request.user.age,                                                                                                                                             
                                    'api_key': key.key},request=request)
        
    return render(request, 'oppia/profile/profile.html', {'form': form,})

def points(request):
    points = Points.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(points, 25) # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        mypoints = paginator.page(page)
    except (EmptyPage, InvalidPage):
        mypoints = paginator.page(paginator.num_pages)
    return render(request, 'oppia/profile/points.html', {'page': mypoints,})

def badges(request):
    awards = Award.objects.filter(user=request.user).order_by('-award_date')
    return render(request, 'oppia/profile/badges.html', {'awards': awards,})

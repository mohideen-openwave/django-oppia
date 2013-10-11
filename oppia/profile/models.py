from django.db import models
from django.contrib.auth.models import User, UserManager 



# Create your models here.
class CustomUser(User):
    """User with app settings."""
    phoneno = models.CharField(max_length=50, default='')    
    current_working_city = models.CharField(max_length=50, default='')
    currently_working_facility = models.CharField(max_length=50, default='')
    staff_type = models.CharField(max_length=50, default='')
    nurhi_sponsor_training = models.CharField(max_length=50, default='')
    current_place_employment = models.CharField(max_length=50, default='')
    highest_education_level = models.CharField(max_length=50, default='')    
    religion = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    
  

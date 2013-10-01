from django.db import models
from django.contrib.auth.models import User, UserManager 



# Create your models here.
class CustomUser(User):
    """User with app settings."""
    phoneno = models.CharField(max_length=50, default='')    
    professional = models.CharField(max_length=50, default='')
    town = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    worktype = models.CharField(max_length=50, default='')
    currentlyworking = models.CharField(max_length=50, default='')
    stafftype = models.CharField(max_length=50, default='')
    familyplaning = models.CharField(max_length=50, default='')
    providedit = models.CharField(max_length=50, default='')
    nurhitraining = models.CharField(max_length=50, default='')
    education = models.CharField(max_length=50, default='')
    religion = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    
    
class CustomUser(models.Model):
    """User with app settings for Administrator settings."""
        
    phoneno = models.CharField(max_length=50, default='')    
    professional = models.CharField(max_length=50, default='')
    town = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    worktype = models.CharField(max_length=50, default='')
    currentlyworking = models.CharField(max_length=50, default='')
    stafftype = models.CharField(max_length=50, default='')
    familyplaning = models.CharField(max_length=50, default='')
    providedit = models.CharField(max_length=50, default='')
    nurhitraining = models.CharField(max_length=50, default='')
    education = models.CharField(max_length=50, default='')
    religion = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    
    # Use UserManager to get the create_user method, etc.
    #objects = UserManager()
                          
    def name(self):          
        return self.last_name
    
    def phoneno(self):
        return self.phoneno
    
    def professional(self):
        return self.professional
    
    def town(self):
        return self.town
    
    def city(self):
        return self.city
    
    def state(self):
        return self.state
    
    def country(self):
        return self.country
    
    def worktype(self):
        return self.worktype
    
    def currentlyworking(self):
        return self.currentlyworking
    
    def stafftype(self):
        return self.stafftype
    
    def familyplaning(self):
        return self.familyplaning
    
    def providedit(self):
        return self.providedit
    
    def nurhitraining(self):
        return self.nurhitraining
    
    def education(self):
        return self.education
    
    def religion(self):
        return self.religion
    
    def sex(self):
        return self.sex
    
    def age(self):
        return self.age
    
        
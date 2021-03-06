from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from oppia.profile.models import CustomUser 
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, 
                               min_length=4,
                               error_messages={'required': _(u'Please enter a username.')},)
    email = forms.CharField(validators=[validate_email],
                                error_messages={'invalid': _(u'Please enter a valid e-mail address.'),
                                                'required': _(u'Please enter your e-mail address.')},
                                required=True)
    password = forms.CharField(widget=forms.PasswordInput,
                                error_messages={'required': _(u'Please enter a password.'),
                                                'min_length': _(u'Your password should be at least 6 characters long.')},
                                min_length=6,       
                                required=True)
    password_again = forms.CharField(widget=forms.PasswordInput,
                                    min_length=6,
                                    error_messages={'required': _(u'Please enter your password again.'),
                                                    'min_length': _(u'Your password again should be at least 6 characters long.')},
                                    required=True)
    # added new fields as per the client requirement    
    # Company Openwave Computing services
    current_working_city = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your current working city.'),
                                                'min_length': _(u'Your current working city should be at least 2 characters long.')},
                                min_length=2,
                                required=True)
    currently_working_facility = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your current working facility.'),
                                                'min_length': _(u'Your current working facility should be at least 2 characters long.')},
                                min_length=2,
                                required=True)
    staff_type = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter staff type.'),
                                                'min_length': _(u'Your staff type should be at least 2 characters long.')},
                                min_length=2,
                                required=True)
    nurhi_sponsor_training = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter Nurhi sponsor training.'),
                                                'min_length': _(u'Your Nurhi sponsor training should be at least 2 characters long.')},
                                min_length=1,
                                required=True)
    current_place_employment = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your current employment place.'),
                                                'min_length': _(u'Your current employment place should be at least 2 characters long.')},
                                min_length=2,
                                required=True)
    highest_education_level = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your highest education level.'),
                                                'min_length': _(u'Your highest education level should be at least 2 characters long.')},
                                min_length=1,
                                required=True)
             
    phoneno = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your contact number.'),
                                                'min_length': _(u'Your contact number should be at least 2 characters long.')},
                                min_length=2,
                                required=True)   
   
    religion = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your religion.'),
                                                'min_length': _(u'Your religion name should be at least 2 characters long.')},
                                min_length=2,
                                required=True)
    sex = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your sex.'),
                                                'min_length': _(u'Your gender should be at least 1 characters long.')},
                                min_length=1,
                                required=True)
    age = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your age.'),
                                                'min_length': _(u'Your age should be at least 1 characters long.')},
                                min_length=1,
                                required=True)
     
    first_name = forms.CharField(max_length=100,
                                    error_messages={'required': _(u'Please enter your first name.'),
                                                    'min_length': _(u'Your first name should be at least 2 characters long.')},
                                    min_length=2,
                                    required=True)
    last_name = forms.CharField(max_length=100,
                                error_messages={'required': _(u'Please enter your last name.'),
                                                'min_length': _(u'Your last name should be at least 2 characters long.')},
                                min_length=2,
                                required=True)

    
    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")

        # check the email address not already used
        num_rows = User.objects.filter(email=email).count()
        if num_rows != 0:
            raise forms.ValidationError( _(u"Email has already been registered"))

        # check the password are the same
        if password and password_again:
            if password != password_again:
                raise forms.ValidationError( _(u"Passwords do not match."))

        # Always return the full collection of cleaned data.
        return cleaned_data

class ResetForm(forms.Form):
    username = forms.CharField(max_length=30,
        error_messages={'invalid': _(u'Please enter a username.')},
        required=True)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get("username")
        num_rows = User.objects.filter(username__exact=username).count()
        if num_rows != 1:
            raise forms.ValidationError( _(u"Username not found"))
        return cleaned_data

class ProfileForm(forms.Form):
    api_key = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}),
                               required=False)
    username = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}),
                               required=False)
    email = forms.CharField(validators=[validate_email],
                            error_messages={'invalid': _(u'Please enter a valid e-mail address.')},
                            required=True)
    password = forms.CharField(widget=forms.PasswordInput,
                               required=False,
                               min_length=6,
                               error_messages={'min_length': _(u'Your new password should be at least 6 characters long')},)
    password_again = forms.CharField(widget=forms.PasswordInput,
                                     required=False,
                                     min_length=6)
    phoneno = forms.CharField(widget = forms.TextInput(),
                               required=False)
    current_working_city = forms.CharField(widget = forms.TextInput(),
                               required=False)
    currently_working_facility = forms.CharField(widget = forms.TextInput(),
                               required=False)
    staff_type = forms.CharField(widget = forms.TextInput(),
                               required=False)
    nurhi_sponsor_training = forms.CharField(widget = forms.TextInput(),
                               required=False)
    current_place_employment = forms.CharField(widget = forms.TextInput(),
                               required=False)
    highest_education_level = forms.CharField(widget = forms.TextInput(),
                               required=False)    
    religion = forms.CharField(widget = forms.TextInput(),
                               required=False)
    sex = forms.CharField(widget = forms.TextInput(),
                               required=False)
    age = forms.CharField(widget = forms.TextInput(),
                               required=False)
    first_name = forms.CharField(max_length=100,
                                 min_length=2,
                                 required=True)
    last_name = forms.CharField(widget = forms.TextInput(),
                               required=True)

    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ProfileForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = self.cleaned_data
        # check email not used by anyone else
        email = cleaned_data.get("email")
        num_rows = CustomUser.objects.exclude(username__exact=self.request.user.username).filter(email=email).count()
        if num_rows != 0:
            raise forms.ValidationError( _(u"Email address already in use"))
        
        # if password entered then check they are the same
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")
        if password and password_again:
            if password != password_again:
                raise forms.ValidationError( _(u"Passwords do not match."))
            
        return cleaned_data
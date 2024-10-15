from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ServiceSeeker, ServiceProvider

# Service Seeker Registration Form
class ServiceSeekerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create associated ServiceSeeker profile after saving user
            ServiceSeeker.objects.create(user=user)
        return user

# Service Provider Registration Form
class ServiceProviderRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create associated ServiceProvider profile after saving user
            ServiceProvider.objects.create(user=user)
        return user

# Login Form (common for both Service Seekers and Service Providers)
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    USER_TYPE_CHOICES = [
        ('service_seeker', 'Service Seeker'),
        ('service_provider', 'Service Provider'),
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_type = self.cleaned_data['user_type']
            
            # Based on the user_type, create the appropriate profile
            if user_type == 'service_seeker':
                ServiceSeeker.objects.create(user=user)
            elif user_type == 'service_provider':
                ServiceProvider.objects.create(user=user)
        return user

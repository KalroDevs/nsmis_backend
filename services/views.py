from rest_framework import viewsets
from .models import ServiceProvider, ServiceSeeker, Skill, SkillCategory, TrainingProgram, Certification, SeekerSkill, Service, ServiceRequest, Transaction, Review
from .serializers import ServiceProviderSerializer, ServiceSeekerSerializer, SkillSerializer, SkillCategorySerializer, TrainingProgramSerializer, CertificationSerializer, SeekerSkillSerializer, ServiceSerializer, ServiceRequestSerializer, TransactionSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404



# ServiceProvider ViewSet
class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]




# ServiceSeeker ViewSet
class ServiceSeekerViewSet(viewsets.ModelViewSet):
    queryset = ServiceSeeker.objects.all()
    serializer_class = ServiceSeekerSerializer

# SkillCategory ViewSet
class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

# Skill ViewSet
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# TrainingProgram ViewSet
class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

# Certification ViewSet
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

# SeekerSkill ViewSet
class SeekerSkillViewSet(viewsets.ModelViewSet):
    queryset = SeekerSkill.objects.all()
    serializer_class = SeekerSkillSerializer

# Service ViewSet
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
   # permission_classes = [IsAuthenticated]

# ServiceRequest ViewSet
class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

# Transaction ViewSet
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Sign up registration
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ServiceSeekerRegistrationForm, ServiceProviderRegistrationForm, UserLoginForm, UserRegistrationForm


# Service Seeker Registration View
def service_seeker_register(request):
    if request.method == 'POST':
        form = ServiceSeekerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Redirect to the home page or dashboard
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ServiceSeekerRegistrationForm()
    return render(request, 'access/register_service_seeker.html', {'form': form})

# Service Provider Registration View
def service_provider_register(request):
    if request.method == 'POST':
        form = ServiceProviderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Redirect to the home page or dashboard
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ServiceProviderRegistrationForm()
    return render(request, 'access/register_service_provider.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')  # Redirect to the home page or dashboard
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'access/login.html', {'form': form})





def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Redirect to home page or dashboard
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'access/register.html', {'form': form})



def home(request):
    is_authenticated = request.user.is_authenticated
    return render(request, 'nsmis/home.html', {'is_authenticated': is_authenticated})
    # return render(request, 'nsmis/home.html')




def service_listings(request):
    services = Service.objects.all()  # Retrieve all services
    return render(request, 'nsmis/service_listings.html', {'services': services})



def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'nsmis/service_detail.html', {'service': service})

from rest_framework_simplejwt.views import TokenBlacklistView
class CustomLogoutView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]
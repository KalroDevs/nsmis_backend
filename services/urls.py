from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import ServiceProviderViewSet, ServiceSeekerViewSet, SkillViewSet, SkillCategoryViewSet, TrainingProgramViewSet, CertificationViewSet, SeekerSkillViewSet, ServiceViewSet, ServiceRequestViewSet, TransactionViewSet, ReviewViewSet
from .views import service_seeker_register, service_provider_register, user_login, user_register, home, service_listings, service_detail
# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'service-providers', ServiceProviderViewSet)
router.register(r'service-seekers', ServiceSeekerViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'skill-categories', SkillCategoryViewSet)
router.register(r'training-programs', TrainingProgramViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'seeker-skills', SeekerSkillViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'service-requests', ServiceRequestViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'reviews', ReviewViewSet)

# Include the router URLs in the project's URL patterns
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token obtain endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
    path('services-api/', include(router.urls)),
    path('register/service-seeker/', service_seeker_register, name='register_service_seeker'),
    path('register/service-provider/', service_provider_register, name='register_service_provider'),
    path('login/', user_login, name='login'),
    path('register/one/', user_register, name='register'),
    path('', home, name='home'),  # Home page URL

    path('services/', service_listings, name='service_listings'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
]







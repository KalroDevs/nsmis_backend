from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Service Provider admin
@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    list_display = ('user', 'location', 'is_verified', 'rating')
    search_fields = ('user__username', 'location')
    list_filter = ('is_verified', 'location')

# Service Seeker admin
@admin.register(ServiceSeeker)
class ServiceSeekerAdmin(ImportExportModelAdmin):
    list_display = ('user', 'location')
    search_fields = ('user__username', 'location')

# Skill Category admin
@admin.register(SkillCategory)
class SkillCategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Skill Category admin
@admin.register(ServiceCategories)
class ServiceCategoriesAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Skill Category admin
@admin.register(Institution)
class InstitutionsAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Skill Category admin
@admin.register(County)
class CountiesAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




# Skill admin
@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

# Training Program admin
@admin.register(TrainingProgram)
class TrainingProgramAdmin(ImportExportModelAdmin):
    list_display = ('title', 'provider', 'start_date', 'end_date', 'is_online')
    search_fields = ('title', 'provider__user__username', 'location')
    list_filter = ('is_online', 'start_date', 'end_date')

# Certification admin
@admin.register(Certification)
class CertificationAdmin(ImportExportModelAdmin):
    list_display = ('seeker', 'skill', 'issue_date', 'expiry_date')
    search_fields = ('seeker__user__username', 'skill__name')
    list_filter = ('issue_date', 'expiry_date')

# Seeker Skill admin
@admin.register(SeekerSkill)
class SeekerSkillAdmin(ImportExportModelAdmin):
    list_display = ('seeker', 'skill', 'proficiency_level')
    search_fields = ('seeker__user__username', 'skill__name')
    list_filter = ('proficiency_level',)

# Service admin
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('title', 'provider', 'price_per_hour', 'category')
    search_fields = ('title', 'provider__user__username', 'category')
    list_filter = ('category',)

# Service Request admin
@admin.register(ServiceRequest)
class ServiceRequestAdmin(ImportExportModelAdmin):
    list_display = ('service', 'seeker', 'request_date', 'status', 'hours_requested', 'total_cost')
    search_fields = ('service__title', 'seeker__user__username', 'status')
    list_filter = ('status', 'request_date')

# Transaction admin
@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    list_display = ('request', 'transaction_date', 'amount', 'payment_status')
    search_fields = ('request__service__title', 'amount')
    list_filter = ('payment_status', 'transaction_date')

# Review admin
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('service_request', 'rating')
    search_fields = ('service_request__service__title', 'rating')
    list_filter = ('rating',)


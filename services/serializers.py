from rest_framework import serializers
from .models import ServiceProvider, ServiceSeeker, Skill, SkillCategory, TrainingProgram, Certification, SeekerSkill, Service, ServiceRequest, Transaction, Review

# ServiceProvider Serializer
class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'

# ServiceSeeker Serializer
class ServiceSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSeeker
        fields = '__all__'

# SkillCategory Serializer
class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# TrainingProgram Serializer
class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProgram
        fields = '__all__'

# Certification Serializer
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

# SeekerSkill Serializer
class SeekerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerSkill
        fields = '__all__'

# Service Serializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

# ServiceRequest Serializer
class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

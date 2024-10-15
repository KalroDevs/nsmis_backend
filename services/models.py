from django.db import models
from django.contrib.auth.models import User

length =255
class County(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name
    

# Service Provider model
class ServiceProvider(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer Not To Say'),
    ]
    PWD_CHOICES = [
        ('None', 'None'),
        ('Specific learning disability (SLD)', 'Specific learning disability (SLD)'),
        ('Speech or language impairment', 'Speech or language impairment'),
        ('Autism spectrum disorder (ASD)', 'Autism spectrum disorder (ASD)'),
        ('Intellectual disability', 'Intellectual disability'),
        ('Emotional disturbance', 'Emotional disturbance'),
        ('Multiple disabilities', 'Multiple disabilities'),
        ('Hearing impairment, including deafness', 'Hearing impairment, including deafness'),
        ('Orthopedic impairment', 'Orthopedic impairment'),
        ('Visual impairment, including blindness', 'Visual impairment, including blindness'),
        ('Traumatic brain injury', 'Traumatic brain injury'),
        ('Deaf-blindness', 'Deaf-blindness'),
    ]
    EDU_CHOICES = [
        ('None', 'None'),
        ('Primary School', 'Primary School'),
        ('High/Secondary School', 'High/Secondary School'),
        ('TVET', 'TVET'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    CRIM_CHOICES = [
        ('None', 'None'),
        ('Primary School', 'Primary School'),
        ('High/Secondary School', 'High/Secondary School'),
        ('TVET', 'TVET'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male', blank=True, null=True)
    pwd =  models.CharField(max_length=length, choices=PWD_CHOICES, default='None', blank=True, null=True)
    next_of_kin_full_name =models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_contact = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    alternative_phone_number =models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    highest_level_of_education = models.CharField(max_length=length, choices=EDU_CHOICES, default='None', blank=True, null=True)
    kra_pin = models.CharField(max_length=50, blank=True, null=True)
    conducted_criminal_offense = models.CharField(max_length=length, choices=CRIM_CHOICES, default='None', blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE,  blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='provider_pics/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.location}"

# Service Seeker model
class ServiceSeeker(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer Not To Say'),
    ]
    PWD_CHOICES = [
        ('None', 'None'),
        ('Specific learning disability (SLD)', 'Specific learning disability (SLD)'),
        ('Speech or language impairment', 'Speech or language impairment'),
        ('Autism spectrum disorder (ASD)', 'Autism spectrum disorder (ASD)'),
        ('Intellectual disability', 'Intellectual disability'),
        ('Emotional disturbance', 'Emotional disturbance'),
        ('Multiple disabilities', 'Multiple disabilities'),
        ('Hearing impairment, including deafness', 'Hearing impairment, including deafness'),
        ('Orthopedic impairment', 'Orthopedic impairment'),
        ('Visual impairment, including blindness', 'Visual impairment, including blindness'),
        ('Traumatic brain injury', 'Traumatic brain injury'),
        ('Deaf-blindness', 'Deaf-blindness'),
    ]
    EDU_CHOICES = [
        ('None', 'None'),
        ('Primary School', 'Primary School'),
        ('High/Secondary School', 'High/Secondary School'),
        ('TVET', 'TVET'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    CRIM_CHOICES = [
        ('None', 'None'),
        ('Primary School', 'Primary School'),
        ('High/Secondary School', 'High/Secondary School'),
        ('TVET', 'TVET'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male', blank=True, null=True)
    pwd =  models.CharField(max_length=length, choices=PWD_CHOICES, default='None', blank=True, null=True)
    next_of_kin_full_name =models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_contact = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    alternative_phone_number =models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    highest_level_of_education = models.CharField(max_length=length, choices=EDU_CHOICES, default='None', blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    kra_pin = models.CharField(max_length=50, blank=True, null=True)
    conducted_criminal_offense = models.CharField(max_length=length, choices=CRIM_CHOICES, default='None', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='seeker_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  blank=True, null=True)
    
    def __str__(self):
        return self.user.username


# Service model
class ServiceCategories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)    
    def __str__(self):
        return self.name

# Service model
class Service(models.Model):
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=255)
    description_of_service = models.TextField(null=True, blank=True)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE, related_name="service_categories", blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    description_of_location = models.TextField(max_length=255,  null=True, blank=True)
    # GPS fields
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Example: -90 to 90
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True) # Example: -180 to 180
    service_picture = models.ImageField(upload_to='service_pics/', null=True, blank=True)
    publish = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} by {self.provider.user.username}"

# Service Request model (acts like an "order" in Uber-like systems)
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    seeker = models.ForeignKey(ServiceSeeker, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    hours_requested = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_cost = self.hours_requested * self.service.price_per_hour
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Request for {self.service.title} by {self.seeker.user.username} - {self.status}"

# Transaction model
class Transaction(models.Model):
    request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)  # False means payment pending, True means completed
    
    def __str__(self):
        return f"Transaction for {self.request.service.title} - {self.amount}"

# Review and Rating model
class Review(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)  # 1 to 5 stars
    review = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Review for {self.service_request.service.title} by {self.service_request.seeker.user.username}"






# Skill Category model
class SkillCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

# Skill model
class Skill(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"

class Institution(models.Model):
    INST_CHOICES = [
        ('Public University', 'Public University'),
        ('Private Universities', 'Private University'),
        ('Technical and Vocational Education and Training Institutions (TVET)', 'Technical and Vocational Education and Training Institutions (TVET)'),
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Primary', 'Primary'),
    ]
    name = models.CharField(max_length=255)
    category  = models.CharField(max_length=length, choices=INST_CHOICES, default='institution_categories')
    description = models.TextField(null=True, blank=True)    
    def __str__(self):
        return self.name


# Training Program model
class TrainingProgram(models.Model):
    provider = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="training_programs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    skill = models.ManyToManyField(Skill, related_name='training_programs', blank=True, null=True)
    duration_in_months = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_online = models.BooleanField(default=False)    
    def __str__(self):
        return f"{self.title} by {self.provider.name}"

# Certification model
class Certification(models.Model):
    seeker = models.ForeignKey(ServiceSeeker, on_delete=models.CASCADE, related_name='certifications')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='certifications')
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.SET_NULL, null=True, blank=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)  # Optional if certification doesn't expire
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.skill.name} certification for {self.seeker.user.username}"

# Seeker Skills model (for tracking the skills a service seeker has)
class SeekerSkill(models.Model):
    seeker = models.ForeignKey(ServiceSeeker, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='seekers')
    proficiency_level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')])
    
    def __str__(self):
        return f"{self.seeker.user.username} - {self.skill.name} ({self.proficiency_level})"


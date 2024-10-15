# Generated by Django 5.0.7 on 2024-10-12 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='service',
            name='description_of_location',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_of_service',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='service_picture',
            field=models.ImageField(blank=True, null=True, upload_to='service_pics/'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='alias',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='alternative_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='conducted_criminal_offense',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Primary School', 'Primary School'), ('High/Secondary School', 'High/Secondary School'), ('TVET', 'TVET'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer Not To Say')], default='Male', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='highest_level_of_education',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Primary School', 'Primary School'), ('High/Secondary School', 'High/Secondary School'), ('TVET', 'TVET'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='kra_pin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='next_of_kin_contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='next_of_kin_full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='pwd',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Specific learning disability (SLD)', 'Specific learning disability (SLD)'), ('Speech or language impairment', 'Speech or language impairment'), ('Autism spectrum disorder (ASD)', 'Autism spectrum disorder (ASD)'), ('Intellectual disability', 'Intellectual disability'), ('Emotional disturbance', 'Emotional disturbance'), ('Multiple disabilities', 'Multiple disabilities'), ('Hearing impairment, including deafness', 'Hearing impairment, including deafness'), ('Orthopedic impairment', 'Orthopedic impairment'), ('Visual impairment, including blindness', 'Visual impairment, including blindness'), ('Traumatic brain injury', 'Traumatic brain injury'), ('Deaf-blindness', 'Deaf-blindness')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='town',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='alias',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='alternative_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='conducted_criminal_offense',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Primary School', 'Primary School'), ('High/Secondary School', 'High/Secondary School'), ('TVET', 'TVET'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer Not To Say')], default='Male', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='highest_level_of_education',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Primary School', 'Primary School'), ('High/Secondary School', 'High/Secondary School'), ('TVET', 'TVET'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='kra_pin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='next_of_kin_contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='next_of_kin_full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='pwd',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Specific learning disability (SLD)', 'Specific learning disability (SLD)'), ('Speech or language impairment', 'Speech or language impairment'), ('Autism spectrum disorder (ASD)', 'Autism spectrum disorder (ASD)'), ('Intellectual disability', 'Intellectual disability'), ('Emotional disturbance', 'Emotional disturbance'), ('Multiple disabilities', 'Multiple disabilities'), ('Hearing impairment, including deafness', 'Hearing impairment, including deafness'), ('Orthopedic impairment', 'Orthopedic impairment'), ('Visual impairment, including blindness', 'Visual impairment, including blindness'), ('Traumatic brain injury', 'Traumatic brain injury'), ('Deaf-blindness', 'Deaf-blindness')], default='None', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='town',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='serviceseeker',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.county'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.county'),
        ),
        migrations.AddField(
            model_name='serviceseeker',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.county'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_categories', to='services.servicecategories'),
        ),
    ]
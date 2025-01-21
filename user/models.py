from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_permission_set', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['email']),  
        ]

class Profile(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    url_github = models.URLField(max_length=50, blank=True, null=True)
    url_linkdin = models.URLField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(max_length=50, blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True)
    
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('volunteer', 'Volunteer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),  
        ]

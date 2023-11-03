from django.db import models

class MEMBER(models.Model):
    fullName = models.CharField(max_length=60, null=False)
    userName = models.CharField(max_length=20, null=False, unique=True)
    profilePhoto = models.ImageField(upload_to='members/', blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    tokenData = models.CharField(max_length=255, null=True, blank=True)
    
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    register_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.userName}'

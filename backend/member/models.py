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
    
    email_subscribe = models.BooleanField(default=False)
    
    register_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.userName}'


class SocialMediaLink(models.Model):
    member = models.ForeignKey(MEMBER, to_field='userName', related_name='socialMedia', on_delete=models.CASCADE)
    x_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.member}'


# class SocialMedia(models.Model):
#     member = models.ForeignKey(MEMBER, to_field='userName', related_name='Social Media', on_delete=models.CASCADE)
#     twitter_url = models.CharField(max_length=200, blank=True, null=True)
#     github_url = models.CharField(max_length=200, blank=True, null=True)
#     linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    
#     def __str__(self):
#         return f'{self.member}'
from django.db import models
from django.conf import settings

from mdeditor.fields import MDTextField

from member.models import MEMBER

# class MEMBER(models.Model):
#     fullName = models.CharField(max_length=60, null=False)
#     userName = models.CharField(max_length=20, null=False, unique=True)
#     profilePhoto = models.ImageField(upload_to='members/', blank=True, null=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     tokenData = models.CharField(max_length=255, null=True)
    
#     is_active = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
    
#     register_date = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f'{self.userName}'
    
    
class POST(models.Model):
    CATEGORIES = (
        ('web-development', 'Web Development'),
        ('trends', 'Trends'),
        ('developer-tools', 'Developer Tools'),
        ('discover', 'Discover')
    )
    LANGUAGES = (
        ('en', 'English'),
        ('tr', 'Turkish'),
    )
    title = models.CharField(max_length=60, null=False, unique=True)
    subTitle = models.CharField(max_length=255, null=False)
    postImage = models.ImageField(upload_to='posts/', blank=True, null=True)
    readingTime = models.PositiveIntegerField()
    category = models.CharField(max_length=25, choices=CATEGORIES)
    mdContent = MDTextField(null=False, blank=True)
    
    language = models.CharField(max_length=2, choices=LANGUAGES, default='tr')
    
    is_active = models.BooleanField(default=False)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    

class COMMENT(models.Model):
    content = models.TextField()
    
    member = models.ForeignKey(MEMBER, to_field='userName', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('POST', on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.member} - {self.post}'
    

# class CONTACT(models.Model):
#     email = models.EmailField(null=False)
#     subject = models.CharField(max_length=200, null=False)
#     message = models.TextField(null=False)
    
#     author = models.CharField(null=True, max_length=20)
    
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f'{self.email} - {self.subject}'
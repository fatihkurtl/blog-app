from django.db import models
from django.conf import settings

from mdeditor.fields import MDTextField

from member.models import MEMBER
    
    
class POST(models.Model):
    CATEGORIES = (
        ('web-development', 'Web Development'),
        ('trends', 'Trends'),
        ('developer-tools', 'Developer Tools'),
        ('discover', 'Discover')
    )
    title = models.CharField(max_length=60, null=False, unique=True)
    subTitle = models.CharField(max_length=255, null=False)
    postImage = models.ImageField(upload_to='posts/', blank=True, null=True)
    readingTime = models.PositiveIntegerField()
    category = models.CharField(max_length=25, choices=CATEGORIES)
    mdContent = MDTextField(null=False, blank=True)

    
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


class POST_LIKE(models.Model):
    member = models.ForeignKey(MEMBER, to_field='userName', related_name='likes',  on_delete=models.CASCADE)
    post = models.ForeignKey(POST, related_name='liked', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.member} - {self.post}'
    
    
class POST_SAVE(models.Model):
    member = models.ForeignKey(MEMBER, to_field='userName', related_name='saves', on_delete=models.CASCADE)
    post = models.ForeignKey(POST, related_name='saved', on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.member} - {self.post}'
    
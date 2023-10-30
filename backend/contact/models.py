from django.db import models

class CONTACT(models.Model):
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=200, null=False)
    message = models.TextField(null=False)
    
    author = models.CharField(null=True, max_length=20)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.email} - {self.subject}'

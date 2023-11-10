from django.db import models


class SubscribeVisitors(models.Model):
    visitor_email = models.EmailField(unique=True)
    register_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.visitor_email}'

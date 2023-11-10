from django.contrib import admin
from .models import SubscribeVisitors

class SubscribeVisitorsAdmin(admin.ModelAdmin):
    list_display = ['visitor_email', 'register_date']
    readonly_fields = ['register_date']
    search_fields = ['visitor_email']
    search_help_text = ('You can search by email')
    

admin.site.register(SubscribeVisitors, SubscribeVisitorsAdmin)

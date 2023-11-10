from django.contrib import admin
from .models import CONTACT

class CONTACTAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'create_at')
    list_filter = ['create_at']
    search_fields = ('subject', 'email')
    search_help_text = ('You can search by subject and email')


admin.site.register(CONTACT, CONTACTAdmin)
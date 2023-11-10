from django.contrib import admin
from .models import MEMBER, SocialMediaLink

from blog.models import COMMENT

class COMMENTInline(admin.TabularInline):
    model = COMMENT
    extra = 0
    
class SocialMediaInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 0


class MEMBERAdmin(admin.ModelAdmin):
   list_display = ('userName', 'fullName', 'email', 'is_active', 'is_admin')
   list_filter = ('is_active', 'is_admin')
   search_fields = ('userName', 'fullName', 'email')
   inlines = [COMMENTInline, SocialMediaInline]
   search_help_text = ('You can search by username, full name and email')


class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['member', 'update_at']
    list_filter = ['member']
    search_fields = ['member']
    search_help_text = ('You can search by member name')


admin.site.register(MEMBER, MEMBERAdmin)
admin.site.register(SocialMediaLink, SocialMediaLinkAdmin)

from django.contrib import admin
from .models import MEMBER, SocialMediaLink

from blog.models import COMMENT, POST_LIKE, POST_SAVE

class COMMENTInline(admin.TabularInline):
    readonly_fields = ['post', 'member', 'content', 'create_at'] # !
    model = COMMENT
    extra = 0
       
class SocialMediaInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 0

class POST_LIKEInline(admin.TabularInline):
    readonly_fields=['post', 'member', 'is_liked']
    model = POST_LIKE
    extra = 0

class POST_SAVEInline(admin.TabularInline):
    readonly_fields=['post', 'member', 'is_saved']
    model = POST_SAVE
    extra = 0
    

class MEMBERAdmin(admin.ModelAdmin):
   list_display = ('userName', 'fullName', 'email', 'is_active', 'is_admin')
   list_filter = ('is_active', 'is_admin')
   search_fields = ('userName', 'fullName', 'email')
   inlines = [SocialMediaInline, COMMENTInline, POST_SAVEInline, POST_LIKEInline]
   search_help_text = ('You can search by username, full name and email')


class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['member', 'update_at']
    list_filter = ['member']
    search_fields = ['member']
    search_help_text = ('You can search by member name')


admin.site.register(MEMBER, MEMBERAdmin)
admin.site.register(SocialMediaLink, SocialMediaLinkAdmin)

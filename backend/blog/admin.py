from django.contrib import admin
from .models import MEMBER, POST, COMMENT


class COMMENTInline(admin.TabularInline):
    model = COMMENT
    extra = 0
    

class POSTAdmin(admin.ModelAdmin):
   list_display = ('title', 'category', 'language', 'is_active', 'create_at')
   list_filter = ('category', 'language', 'is_active', 'create_at')
   search_fields = ('title', 'subTitle', 'mdContent')
   list_editable = ['category', 'is_active']
   inlines = [COMMENTInline]
   search_help_text = ('You can search by title subtitle and post content')
   
    
class COMMENTAdmin(admin.ModelAdmin):
    list_display = ('post', 'member', 'is_active', 'create_at')
    list_filter = ('post', 'member', 'is_active', 'create_at')
    search_fields = ('post', 'member')
    readonly_fields = ['create_at']
    search_help_text = ('You can search by post and member information')
    


admin.site.register(POST, POSTAdmin)
admin.site.register(COMMENT, COMMENTAdmin)
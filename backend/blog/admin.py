from django.contrib import admin
from .models import MEMBER, POST, COMMENT


class COMMENTInline(admin.TabularInline):
    model = COMMENT
    extra = 0
    

class POSTAdmin(admin.ModelAdmin):
   list_display = ('title', 'category', 'language', 'is_active')
   list_filter = ('category', 'language', 'is_active')
   search_fields = ('title', 'subTitle', 'mdContent')
   list_editable = ['category', 'is_active']
   inlines = [COMMENTInline]
   
    
class COMMENTAdmin(admin.ModelAdmin):
    list_display = ('post', 'member', 'is_active')
    list_filter = ('post', 'member', 'is_active')
    search_fields = ('post', 'member')


admin.site.register(POST, POSTAdmin)
admin.site.register(COMMENT, COMMENTAdmin)
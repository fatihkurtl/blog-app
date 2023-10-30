from django.contrib import admin
from .models import MEMBER

from blog.models import COMMENT

class COMMENTInline(admin.TabularInline):
    model = COMMENT
    extra = 0


class MEMBERAdmin(admin.ModelAdmin):
   list_display = ('userName', 'fullName', 'email', 'is_active', 'is_admin')
   list_filter = ('is_active', 'is_admin')
   search_fields = ('userName', 'fullName', 'email')
   inlines = [COMMENTInline]


admin.site.register(MEMBER, MEMBERAdmin)
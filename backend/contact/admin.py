from django.contrib import admin
from .models import CONTACT

class CONTACTAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email')
    search_fields = ('subject', 'email')


admin.site.register(CONTACT, CONTACTAdmin)
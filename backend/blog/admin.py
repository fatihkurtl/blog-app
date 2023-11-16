from django.contrib import admin
from .models import MEMBER, POST, COMMENT, POST_LIKE, POST_SAVE
from modeltranslation.admin import TranslationAdmin


class COMMENTInline(admin.TabularInline):
    readonly_fields = ['post', 'member', 'content', 'create_at'] # !
    model = COMMENT
    extra = 0 

class POSTAdmin(TranslationAdmin):
   list_display = ('title', 'category', 'is_active', 'create_at')
   list_filter = ('category', 'is_active', 'create_at')
   search_fields = ('title', 'subTitle', 'mdContent')
   list_editable = ['category', 'is_active']
   inlines = [COMMENTInline]
   search_help_text = ('You can search by title subtitle and post content')
   
   #group_fieldsets = True
   class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
   
    
class COMMENTAdmin(admin.ModelAdmin):
    list_display = ('post', 'member', 'is_active', 'create_at')
    list_filter = ('post', 'member', 'is_active', 'create_at')
    search_fields = ('post', 'member')
    readonly_fields = ['post', 'member', 'content', 'create_at'] # ? duruma gore 'post', 'member', 'content' fieldlari kaldirabilir comment ekleyebilmek icin
    search_help_text = ('You can search by post and member information')
    

class POST_LIKEAdmin(admin.ModelAdmin):
    list_display = ('post', 'member', 'is_liked')
    readonly_fields=['post', 'member', 'is_liked']

class POST_SAVEAdmin(admin.ModelAdmin):
    list_display = ('post', 'member')
    readonly_fields=['post', 'member', 'is_saved']
    


admin.site.register(POST, POSTAdmin)
admin.site.register(COMMENT, COMMENTAdmin)
admin.site.register(POST_LIKE, POST_LIKEAdmin)
admin.site.register(POST_SAVE, POST_SAVEAdmin)
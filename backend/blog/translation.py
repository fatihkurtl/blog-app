from .models import POST
from modeltranslation.translator import TranslationOptions,register

@register(POST)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'subTitle', 'mdContent')
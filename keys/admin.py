from django.contrib.admin import ModelAdmin, register
from .models import Key

@register(Key)
class KeyAdmin(ModelAdmin):
    list_display = ('key_kind', 'is_valid', 'created_at', 'updated_at')
    list_filter = ('is_valid', 'key_kind')
    search_fields = ('key_kind',)
    readonly_fields = ('created_at', 'updated_at')

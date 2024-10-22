from django.contrib.admin import ModelAdmin, register
from .models import Conversation, Message


@register(Conversation)
class ConversationAdmin(ModelAdmin):
    list_display = ('id', 'title', 'user', 'count_messages', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at', 'updated_at', 'user')
    readonly_fields = ('count_messages', 'created_at', 'updated_at')

    def count_messages(self, obj):
        return obj.count_messages()

@register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('id', 'conversation', 'user', 'payload', 'created_at', 'updated_at')
    search_fields = ('payload', 'conversation__title', 'user__username')
    list_filter = ('created_at', 'updated_at', 'conversation', 'user')

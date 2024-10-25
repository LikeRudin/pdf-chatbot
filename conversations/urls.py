from django.urls import path

from .views import Conversations, ConversationWithMessages, AConversation

urlpatterns = [
    path('',view=Conversations.as_view()),
    path('<int:pk>', view=AConversation.as_view()),
    path('<int:pk>/messages', view=ConversationWithMessages.as_view()),
]




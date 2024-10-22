from django.urls import path

from .views import Conversations, ConversationMessages

urlpatterns = [
    path('',view=Conversations.as_view()),
    path('<int:pk>/messages', view=ConversationMessages.as_view()),
]




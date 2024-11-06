from django.urls import path

from .views import Conversations, Messages, AConversation

urlpatterns = [
    path('',view=Conversations.as_view()),
    path('<int:pk>', view=AConversation.as_view()),
    path('<int:pk>/messages', view=Messages.as_view()),
]




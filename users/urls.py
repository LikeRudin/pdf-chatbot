from django.urls import path

from .views import Login, Join, LogOut

urlpatterns = [
    path('login', Login.as_view()),
    path('logout', LogOut.as_view()),
    path('join', Join.as_view())
]

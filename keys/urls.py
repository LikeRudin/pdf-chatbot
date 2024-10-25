from django.urls import path

from .views import Keys, AKey , StaticsAndCharged

urlpatterns = [
    path("", Keys.as_view()),
    path("<int:pk>", AKey.as_view()),
    path("<int:pk>/statics",StaticsAndCharged.as_view() )
]
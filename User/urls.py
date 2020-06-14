from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsersMeView

urlpatterns = [
    path('me/', UsersMeView.as_view()),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('', DomainFlagLView.as_view()),
]

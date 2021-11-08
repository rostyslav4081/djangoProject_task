from django.urls import path
from .views import *
urlpatterns = [
    path('', DomainLView.as_view()),
    path('<int:pk>', DomainRUDViewSpecial.as_view()),
]

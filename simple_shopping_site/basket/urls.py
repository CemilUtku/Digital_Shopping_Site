from django.urls import path
from basket.views import home

urlpatterns = [
    path('', home),
]

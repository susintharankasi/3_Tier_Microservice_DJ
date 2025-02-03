from django.urls import path
from .views import fetch_weather, get_saved_weather

urlpatterns = [
    path('weather/<str:city>/', fetch_weather, name='fetch_weather'),
    path('history/', get_saved_weather, name='get_saved_weather'),
]

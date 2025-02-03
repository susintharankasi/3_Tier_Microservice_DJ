# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_weather
from .models import WeatherData

@api_view(['GET'])
def fetch_weather(request, city):
    weather = get_weather(city)
    if weather:
        WeatherData.objects.create(**weather)
        return Response(weather)
    return Response({"error": "City not found"}, status=404)

@api_view(['GET'])
def get_saved_weather(request):
    data = WeatherData.objects.all().order_by('-timestamp')[:10].values()
    return Response({"history": list(data)})

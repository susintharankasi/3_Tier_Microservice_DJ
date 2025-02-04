from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from .models import User
from .serializers import UserSerializer
import requests

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer



API_URL = "http://localhost:8000/api/users/"

def user_list(request):
    response = requests.get(API_URL)
    users = response.json()
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        requests.post(API_URL, data={"name": name, "email": email})
        return redirect('user_list')

    return render(request, 'user_list.html', {"users": users})

def delete_user(request, id):
    requests.delete(f"{API_URL}{id}/")
    return redirect('user_list')

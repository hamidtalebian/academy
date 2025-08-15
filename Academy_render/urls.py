from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Academy!</h1><p>Deployment is successful 🎉</p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]

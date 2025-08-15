from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# یک صفحه خانگی ساده
def home(request):
    return HttpResponse("<h1>Welcome to Academy!</h1><p>Your Django app is running!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # صفحه اصلی
]

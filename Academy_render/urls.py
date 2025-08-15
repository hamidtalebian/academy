from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # مثال: اگر اپ courses داری
    path('', include('courses.urls')),  
]

from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.select_related('teacher').all().order_by('start_date')
    return render(request, 'home.html', {'courses': courses})

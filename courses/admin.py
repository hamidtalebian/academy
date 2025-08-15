from django.contrib import admin
from .models import Teacher, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise')
    search_fields = ('name', 'expertise')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'start_date', 'end_date')
    list_filter = ('teacher', 'start_date', 'end_date')
    search_fields = ('title', 'description')

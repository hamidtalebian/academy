from django.contrib import admin
from .models import Teacher, Course, Student, Enrollment

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise', 'phone')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'capacity', 'teacher')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')

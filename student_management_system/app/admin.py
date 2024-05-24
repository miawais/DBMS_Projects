from django.contrib import admin
from .models import Customer, Student, Course, Enrollment, Grade, Teacher, Department, Attendance
# Register your models here.
admin.site.register(Customer)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Attendance)
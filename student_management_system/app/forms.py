from django import forms
from .models import Student, Teacher, Course, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'address', 'email']


class TeacherForm(forms.ModelForm):  # Add a form for Teacher
    class Meta:
        model = Teacher
        fields = ['name', 'email']

class CourseForm(forms.ModelForm):  # Add a form for Course
    class Meta:
        model = Course
        fields = ['course_name', 'description']


class GradeForm(forms.ModelForm):  # Add a form for Grade
    class Meta:
        model = Grade
        fields = ['enrollment', 'grade', 'grading_date']
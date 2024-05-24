from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    
    
    def register(self):
        self.save()
    
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email) 
        except:
            return False 
        
        
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        
        return False
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.CharField(max_length=255, default='Not Provided')
    email = models.EmailField(max_length=100, default='example@example.com')

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField(default='No description available.')

    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.student.name} - {self.course.course_name}'

class Grade(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    grading_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.enrollment.student.name} - {self.grade}'

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='teacher@example.com')

    def __str__(self):
        return self.name

class Department(models.Model):
    department_name = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.department_name

class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance_date = models.DateField(default=timezone.now)
    attendance_status = models.CharField(max_length=7, choices=ATTENDANCE_STATUS_CHOICES, default='Present')

    def __str__(self):
        return f'{self.student.name} - {self.course.course_name} - {self.attendance_status}'
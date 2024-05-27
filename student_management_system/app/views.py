from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Count
from app.forms import StudentForm, TeacherForm, CourseForm, GradeForm
from app.models import Customer, Student, Course, Teacher, Enrollment, Grade
from django.views import View

    # Create your views here.
    # def home(request):
    #     return render(request, 'signup_or_login.html')

class Signup(View):
    def get(self, request):
        return render(request, 'signup_or_login.html')
        
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        password = postData.get('password')

        print("\n\n\n", name, email, password, "\n\n\n")
                
        error_message = None
                
        values = {"name" : name,
                    "email" : email,
                    "password" : password}
        customer = Customer(name = name,
                                email = email,
                                password = password)
        error_message = self.validations(customer)
                # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            print("\n\n\ncustomer saved\n\n\n")
            return redirect('signup_or_login')
        else:
            return render(request, 'signup_or_login.html', {'error':error_message, 'values':values})
            

    def validations(self, customer):
            # Form validations 
        error_message = None
        if not customer.name:
            error_message = "Name Reguired!!"
        elif len(customer.name)<=2:
            error_message = "Name must be longer than or equal to 2 characters!!"
        elif not customer.email:
            error_message = "Email Reguired!!"
        elif len(customer.email)<=2:
            error_message = "Email must be longer than or equal to 2 characters!!"
        elif customer.isExists():
            error_message="This Email already exists! Please try another one.."
        elif not customer.password:
            error_message = "Password is required!"
        elif len(customer.password)<=10:
            error_message =" Password should have at least 10 characteres."
            
        return error_message 



class Login(View):
        # return_url = None
    def get(self, request):
            # Login.return_url = request.GET.get('return_url')
        return render(request, 'signup_or_login.html')
    def post(self, request):
            # return login(request)
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                    # if Login.return_url:
                    #     return HttpResponseRedirect(Login.return_url)
                    # else:
                    #     Login.return_url = None
                    #     return redirect('homepage')
                return redirect('dashboard') 
            else:
                error_message = "Invalid email or password"
        else:
            error_message="Invalid Email or Password!"
            
        return render(request, 'signup_or_login.html', {'error':error_message})
            # print(email, password)
            
            
            
def logout(request):
    request.session.clear()
    return redirect('signup_or_login')



# class home(View):
#     def get(self, request):
#         return render(request, 'index.html')
    




class Dashboard(View):
    def get(self, request):
        # Get the total counts
        total_students = Student.objects.count()
        total_courses = Course.objects.count()
        total_teachers = Teacher.objects.count()  # Assuming 'Teacher' model instead of 'Professor'
        total_grades = Grade.objects.count()  # Assuming 'Assignment' is referred as 'Grade'

        # Get recent activities (example: last 5 enrollments and last 5 grades assigned)
        recent_enrollments = Enrollment.objects.select_related('student', 'course').order_by('-enrollment_date')[:5]
        recent_grades = Grade.objects.select_related('enrollment__student', 'enrollment__course').order_by('-grading_date')[:5]

        recent_activities = []

        for enrollment in recent_enrollments:
            recent_activities.append(f'Student {enrollment.student.name} enrolled in Course {enrollment.course.course_name} on {enrollment.enrollment_date}.')

        for grade in recent_grades:
            recent_activities.append(f'Grade {grade.grade} was assigned to Student {grade.enrollment.student.name} for Course {grade.enrollment.course.course_name} on {grade.grading_date}.')

        # Combine the context data
        context = {
            'total_students': total_students,
            'total_courses': total_courses,
            'total_teachers': total_teachers,
            'total_grades': total_grades,
            'recent_activities': recent_activities,
        }

        # Render the dashboard template with the context data
        return render(request, 'dashboard.html', context)
    



# Class-based view for displaying student details
class StudentDetailsView(View):
    def get(self, request):
        students = Student.objects.all().select_related()
        context = {'students': students}
        return render(request, 'student_details.html', context)

# Class-based view for adding or editing a student
class AddEditStudentView(View):
    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
        else:
            student = None
        
        form = StudentForm(instance=student)
        return render(request, 'add_edit_student.html', {'form': form})
    
    def post(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
        else:
            student = None
        
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_details')
        
        return render(request, 'add_edit_student.html', {'form': form})
    



# Class-based view for displaying teacher details
class TeacherDetailsView(View):
    def get(self, request):
        teachers = Teacher.objects.all().select_related()
        context = {'teachers': teachers}
        return render(request, 'teacher_details.html', context)

# Class-based view for adding or editing a teacher
class AddEditTeacherView(View):
    def get(self, request, pk=None):
        if pk:
            teacher = get_object_or_404(Teacher, pk=pk)
        else:
            teacher = None
        
        form = TeacherForm(instance=teacher)
        return render(request, 'add_edit_teacher.html', {'form': form})
    
    def post(self, request, pk=None):
        if pk:
            teacher = get_object_or_404(Teacher, pk=pk)
        else:
            teacher = None
        
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_details')
        
        return render(request, 'add_edit_teacher.html', {'form': form})
    

# Class-based view for displaying course details
class CourseDetailsView(View):
    def get(self, request):
        courses = Course.objects.all().select_related()
        context = {'courses': courses}
        return render(request, 'course_details.html', context)

# Class-based view for adding or editing a course
class AddEditCourseView(View):
    def get(self, request, pk=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
        else:
            course = None
        
        form = CourseForm(instance=course)
        return render(request, 'add_edit_course.html', {'form': form})
    
    def post(self, request, pk=None):
        if pk:
            course = get_object_or_404(Course, pk=pk)
        else:
            course = None
        
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_details')
        
        return render(request, 'add_edit_course.html', {'form': form})
    


# Class-based view for displaying grade details
class GradeDetailsView(View):
    def get(self, request):
        grades = Grade.objects.all().select_related('enrollment__student', 'enrollment__course')
        context = {'grades': grades}
        return render(request, 'grade_details.html', context)

# Class-based view for adding or editing a grade
class AddEditGradeView(View):
    def get(self, request, pk=None):
        if pk:
            grade = get_object_or_404(Grade, pk=pk)
        else:
            grade = None
        
        form = GradeForm(instance=grade)
        return render(request, 'add_edit_grade.html', {'form': form})
    
    def post(self, request, pk=None):
        if pk:
            grade = get_object_or_404(Grade, pk=pk)
        else:
            grade = None
        
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_details')
        
        return render(request, 'add_edit_grade.html', {'form': form})
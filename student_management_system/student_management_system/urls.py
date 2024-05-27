"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import Signup, Login, logout, Dashboard, StudentDetailsView, AddEditStudentView, TeacherDetailsView, AddEditTeacherView, CourseDetailsView, AddEditCourseView, GradeDetailsView, AddEditGradeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signup.as_view(), name="signup_or_login"),
    path('login/', Login.as_view(), name="login"),
    # path('home/', home.as_view(), name="home"),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('logout/', logout, name="logout"),
    path('students/', StudentDetailsView.as_view(), name='student_details'),
    path('students/add/', AddEditStudentView.as_view(), name='add_edit_student'),
    path('students/edit/<int:pk>/', AddEditStudentView.as_view(), name='edit_student'),
    path('teachers/', TeacherDetailsView.as_view(), name='teacher_details'),
    path('teachers/add/', AddEditTeacherView.as_view(), name='add_edit_teacher'),
    path('teachers/edit/<int:pk>/', AddEditTeacherView.as_view(), name='edit_teacher'),
    path('courses/', CourseDetailsView.as_view(), name='course_details'),
    path('courses/add/', AddEditCourseView.as_view(), name='add_edit_course'),
    path('courses/edit/<int:pk>/', AddEditCourseView.as_view(), name='edit_course'),
    path('grades/', GradeDetailsView.as_view(), name='grade_details'),
    path('grades/add/', AddEditGradeView.as_view(), name='add_edit_grade'),
    path('grades/edit/<int:pk>/', AddEditGradeView.as_view(), name='edit_grade'),
]

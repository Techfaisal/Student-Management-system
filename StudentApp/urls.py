from django.urls import path

from StudentApp import views

urlpatterns = [
    path('', views.login_fun, name='login'),   # it will redirect to login.html page
    path('register', views.register_fun, name='register'),   # it will redirect to Register.html page it will be create a account
    path('home',views.home_fun, name='home'),        # it will redirect to home.html page
    path('add_course',views.addcourse_fun,name='addcourse') ,  # redirecting to addcourse.html page   and as well as it will inserting the course data in course table
    path('display_course',views.display_course_fun,name='display_course'),    # It will collect the data from course table and send to display Course.html page
    path('update_course/<int:courseid>',views.update_course_fun,name='update_course'),      # it will update the course data
    path('delete_course/<int:courseid>',views.delete_course_fun,name='delete_course'),       # it will delete the course data from the course table
    path('addstudent',views.addstudent_fun,name='addstudent'),  # it will display add student and read the data from AddStudent.html file
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),     # it will display trhe entire student data

]
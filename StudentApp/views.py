from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from StudentApp.models import Course, City, Student


# Create your views here.


def login_fun(request):
    if request.method == 'POST':
        user_name = request.POST["txtusername"]
        user_password = request.POST["txtpassword"]
        u1 = authenticate(username=user_name,password=user_password)
        if u1 is not None and u1.is_superuser:        # checking whether the data is superuser or not
            request.session['Uname']=user_name
            return redirect('home')
        else:
            return render(request,'Login.html',{'msg': 'Username or password is incorrect'})
    else:
        return render(request,'Login.html')


def register_fun(request):
    if request.method == 'POST':  # this code will execute when we click on submit button in Register.html page
        user_name = request.POST["txtusername"]
        user_password = request.POST["txtpassword"]
        user_email = request.POST["txtemail"]
        u1 = User.objects.create_superuser(username= user_name,password=user_password,email=user_email)
        u1.save()
        return redirect('login')
    else:   # this code will be execute when we click on hyperlink in login.html page
        return render(request, 'Register.html')


def home_fun(request):

    return render(request,'Home.html', {'data': request.session['Uname']})


def addcourse_fun(request):
    if request.method == 'POST':
        c1 = Course()
        c1.course_name=request.POST['txtcoursename']
        c1.course_duration = request.POST['txtcourseduration']
        c1.course_fees = int(request.POST['txtcoursefees'])
        c1.save()
        return render(request, 'AddCourse.html',{'msg': 'Added Successfully'})
    else:
        return render(request, 'AddCourse.html')


def display_course_fun(request):
    course_data = Course.objects.all()    # it will return list of objects
    return render(request, 'DisplayCourse.html', {'data': course_data})


def update_course_fun(request,courseid):
    c1 = Course.objects.get(id=courseid)
    if request.method == 'POST':
        c1.course_name = request.POST['txtcoursename']
        c1.course_duration = request.POST['txtcourseduration']
        c1.course_fees = int(request.POST['txtcoursefees'])
        c1.save()
        return redirect('display_course')
    else:       # when we click on hyperlink else block code will be executed
        return render(request,'UpdateCourse.html',{'data': c1})


def delete_course_fun(request,courseid):
    c1=Course.objects.get(id=courseid)     # get the database on the course id which is passed the object
    c1.delete()     # delete the data which is inside the object
    return redirect('display_course')


def addstudent_fun(request):
    if request.method == 'POST':
        s1= Student()
        s1.stud_name = request.POST['txtname']
        s1.stud_phno = int(request.POST['txtphno'])
        s1.stud_email = request.POST['txtemail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fees = int(request.POST['txtpaidfees'])

        c1 = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.pending_fees = c1.course_fees - s1.paid_fees
        s1.save()
        return redirect('addstudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'AddStudent.html', {'CityData': city, 'CourseData': course})


def displaystudent_fun(request):
    s1 = Student.objects.all()
    return render(request,'DisplayStudent.html',{'studentdata': s1})
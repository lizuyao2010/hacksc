from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Student
from .models import Course
from .models import Student_Course
from .models import Question
from .models import Answer
from forms import UserForm
from forms import StudentForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def main(request):
    return render(request,'polls/main.html',{})

def my_login(request):
    if request.method == "POST":
        # form = loginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/polls/main/')
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    else:
        # form=loginForm()
        pass
    return render(request, 'polls/login.html', {})

def addStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student(**form.cleaned_data)
            new_student.save()
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('/polls/main/')
    else:
        form = StudentForm() 

    return render(request, 'polls/addStudent.html', {'form': form})

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            # login(request,new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('/polls/addStudent/')
    else:
        form = UserForm() 

    return render(request, 'polls/adduser.html', {'form': form}) 

def stuInfo(request, student_id):
    stu_cou = get_object_or_404(Student_Course, pk=student_id)
    stu = get_object_or_404(Student, pk=student_id)
    cou_id_list = []
    for s_c in stu_cou:
        cou_id_list.append(s_c.course_id)

    course_list = []
    for cou_id in cou_id_list:
        course = get_object_or_404(Course, pk=cou_id)
        course_list.append(course)

    context = {'course_list': course_list, 'student_info': stu}
    return render(request, 'polls/stuInfo.html', context)

def couInfo(request, course_id):

    stu_cou = get_object_or_404(Student_Course, pk=course_id)
    cou = get_object_or_404(Course, pk=course_id)

    stu_id_list = []
    for s_c in stu_cou:
        stu_id_list.append(s_c.student_id)

    student_list = []
    for stu_id in stu_id_list:
        student = get_object_or_404(Student, pk=stu_id)
        student_list.append(student)
    context = {'student_list': student_list, 'cou_info': cou}
    return render(request, 'polls/couInfo.html', context)
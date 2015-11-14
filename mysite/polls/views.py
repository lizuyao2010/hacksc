from django.shortcuts import render

# Create your views here.
from .models import Student
from .models import Course
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def lexusadduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm() 

    return render(request, 'adduser.html', {'form': form}) 

def stuOfACourse(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

	student_list = course.students
	context = {'student_list': student_list}
    return render(request, 'polls/stuOfACourse.html', context)

def couOfAStudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    all_course_list = Course.objects.course_id
    course_list = []

    for course in Course.objects:
    	for stu in course.students:
    		if stu.student_id == student_id:
    			course_list.append(course)

	context = {'course_list': course_list}
    return render(request, 'polls/couOfAStudent.html', context)

def stuInfo(request, student_id):
	student = get_object_or_404(Student, pk=student_id)

	context = {'student': student}
    return render(request, 'polls/stuInfo.html', context)

def couInfo(request, course_id):
	student = get_object_or_404(Student, pk=student_id)

	context = {'course': course}
    return render(request, 'polls/couInfo.html', context)



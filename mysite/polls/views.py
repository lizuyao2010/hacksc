from django.shortcuts import render

# Create your views here.
from .models import Student
from .models import Course

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



from django.shortcuts import render

# Create your views here.
from .models import Student
from .models import Course

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
from django.contrib.auth.models import User
from models import Student,Course
from django.forms import ModelForm
from django import forms
import datetime

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    course_id = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=100)
    # question_id = forms.CharField(max_length=100)
    post_time = 0
class AnswerForm(forms.Form):
    # answer_id = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    answerer_id = forms.CharField(max_length=100)
    question_id = forms.CharField(max_length=100)
    answer_time = 0
class StudentForm(ModelForm):
    """docstring for StudentForm"""
    class Meta:
        model = Student
        fields=('user','student_id','gender','year_in_school','major')

class CourseForm(ModelForm):
    """docstring for StudentForm"""
    class Meta:
        model = Course
        fields=('course_id','course_name')
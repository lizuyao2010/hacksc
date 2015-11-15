from django.contrib.auth.models import User
from models import Student
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')

class StudentForm(ModelForm):
    """docstring for StudentForm"""
    class Meta:
        model = Student
        fields=('user','student_id','gender','year_in_school','major')

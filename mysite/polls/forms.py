from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    course_id = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=100)
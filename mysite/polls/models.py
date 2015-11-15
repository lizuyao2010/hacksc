from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,primary_key=True,default=None)
    # user_id=models.CharField(max_length=30,primary_key=True,default="007")
    student_id = models.CharField(max_length=30,null=True)
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length = 1, choices = GENDER,null=True)
    YEAR_IN_SCHOOL_CHOICES = (
        ('UN','UnderGraduate'),
        ('GR', 'Graduate'),
    )
    year_in_school = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES,null=True)
    major = models.CharField(max_length = 20,null=True)

class Course(models.Model):
    course_id=models.CharField(max_length=30,primary_key=True, default = 'NULL')
    course_name=models.CharField(max_length=200, null = True)

class Student_Course(models.Model):
    student_id = models.CharField(max_length=30, default="123")
    course_id = models.CharField(max_length=30, default="123")

class Question(models.Model):
    # question_id = models.CharField(max_length=30,primary_key=True)
    course_id=models.CharField(max_length=30,default=True, null = True)
    student_id = models.CharField(max_length=30,default=True, null = True)
    title = models.CharField(max_length=1024,default=True, null = True)
    post_time=models.CharField(max_length=1024,default=True, null = True)
    content = models.CharField(max_length=1024,default=True, null = True)


class Answer(models.Model):
    # answer_id=models.CharField(max_length=30,default=True)
    answerer_id=models.CharField(max_length=30,default=True)
    question_id=models.CharField(max_length=30,default=True)
    content=models.CharField(max_length=1024,default=True)
    answer_time=models.CharField(default=True, max_length=1024)

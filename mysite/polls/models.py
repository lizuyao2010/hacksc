from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,primary_key=True)
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
    course_id=models.CharField(max_length=30,primary_key=True,default=True)
    course_name=models.CharField(max_length=200,default=True, null = True)
    # course_section=models.CharField(max_length=30,default=True)
    # COURSE_TYPE=(
        # ('Le','Lecture'),
        # ('La','Lab'),
        # ('Q','Quiz'),   
    # )
    # course_type=models.CharField(max_length=2,choices=COURSE_TYPE,default=True)
    # instructor=models.CharField(max_length=30,default=True)
    # location=models.CharField(max_length=30,default=True)
    # capcity=models.IntegerField(default=True)
    # registered=models.IntegerField(default=True)
    # start_time=models.TimeField(default=True)
    # end_time=models.TimeField(default=True)
    # how to add multiple choices?
    # days=models.CharField(max_length=30,default=True)
    # credits=models.FloatField(default=True)
    # students=models.ManyToManyField(Student)

class Student_Course(models.Model):
    student_id = models.CharField(max_length=30,default="123")
    course_id = models.CharField(max_length=30,default="123")

class Question(models.Model):
    question_id = models.CharField(max_length=30,primary_key=True)
    course_id=models.CharField(max_length=30,default=True, null = True)
    student_id = models.CharField(max_length=30,default=True, null = True)
    title = models.CharField(max_length=1024,default=True, null = True)
    post_time=models.CharField(max_length=1024,default=True, null = True)
    content = models.CharField(max_length=1024,default=True, null = True)


class Answer(models.Model):
    answer_id=models.CharField(max_length=30,default=True)
    answerer_id=models.CharField(max_length=30,default=True)
    question_id=models.CharField(max_length=30,default=True)
    content=models.CharField(max_length=1024,default=True)
    answer_time=models.TimeField(default=True)

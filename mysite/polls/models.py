from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=30,primary_key=True,default=True)
    first_name = models.CharField(max_length=30,default=True)
    last_name = models.CharField(max_length=30,default=True)
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length = 1, choices = GENDER,default=True)
    YEAR_IN_SCHOOL_CHOICES = (
        ('UN','UnderGraduate')
        ('GR', 'Graduate'),
    )
    year_in_school = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES,default=True)
    major = models.CharField(max_length = 20,default=True)

class Course(models.Model):
    course_id=models.CharField(max_length=30,default=True)
    course_name=models.CharField(max_length=30,default=True)
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



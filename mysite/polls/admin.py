from django.contrib import admin

# Register your models here.
from .models import Student,Course,Student_Course,Question,Answer

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Student_Course)
admin.site.register(Question)
admin.site.register(Answer)
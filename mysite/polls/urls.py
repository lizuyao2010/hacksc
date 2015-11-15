from django.conf.urls import url

import views

urlpatterns = [
    url(r'^my_login/$', views.my_login, name='my_login`'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^addStudent/$', views.addStudent, name='addStudent'),
    url(r'^main/$', views.main, name='main'),
    url(r'^stuInfo/(?P<student_id>[0-9a-z]+)/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/(?P<course_id>[0-9a-z]+)/$', views.couInfo, name='couInfo'),
]
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^my_login/$', views.my_login, name='my_login`'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^addStudent/$', views.addStudent, name='addStudent'),
    url(r'^addcourse/$', views.addcourse, name='addcourse'),
    url(r'^main/$', views.main, name='main'),
    url(r'^stuInfo/(?P<student_id>[0-9a-z]+)/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/(?P<course_id>[0-9a-zA-Z ]+)/$', views.couInfo, name='couInfo'),
    url(r'^addQuestion/$', views.addQuestion, name='addQuestion'),
    url(r'^questionList/(?P<course_id>[0-9a-z]+)/$', views.questionList, name='questionList'),
    url(r'^answerList/(?P<question_id>[0-9a-z]+)/$', views.answerList, name='answerList')
]
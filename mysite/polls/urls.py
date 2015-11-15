from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lexusadduser, name='lexusadduser'),
    url(r'^stuInfo/(?P<student_id>[0-9a-z]+)/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/(?P<course_id>[0-9a-z]+)/$', views.couInfo, name='couInfo'),
    url(r'^questionList/(?P<course_id>[0-9a-z]+)/$', views.questionList, name='questionList'),
    url(r'^answerList/(?P<question_id>[0-9a-z]+)/$', views.answerList, name='answerList'),
]
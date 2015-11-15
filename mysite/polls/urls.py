from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lexusadduser, name='lexusadduser'),
    url(r'^stuInfo/(?P<student_id>[0-9a-z]+)/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/(?P<course_id>[0-9a-z]+)/$', views.couInfo, name='couInfo'),
]
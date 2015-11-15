from django.conf.urls import url

import views

urlpatterns = [
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^stuInfo/(?P<student_id>[0-9a-z]+)/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/(?P<course_id>[0-9a-z]+)/$', views.couInfo, name='couInfo'),
]
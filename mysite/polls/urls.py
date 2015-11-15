from django.conf.urls import url

import views

urlpatterns = [
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^stuInfo/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/$', views.couInfo, name='couInfo'),
]
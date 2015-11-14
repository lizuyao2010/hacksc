from django.conf.urls import url

import views

urlpatterns = [
    url(r'^lexusadduser/$', views.lexusadduser, name='lexusadduser'),
    url(r'^stuInfo/$', views.stuInfo, name='stuInfo'),
    url(r'^couInfo/$', views.couInfo, name='couInfo'),
]
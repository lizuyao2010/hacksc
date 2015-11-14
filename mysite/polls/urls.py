from django.conf.urls import url

import views

urlpatterns = [
    url(r'^lexusadduser$', views.lexusadduser, name='lexusadduser'),
]
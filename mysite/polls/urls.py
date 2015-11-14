from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lexusadduser$', views.lexusadduser, name='lexusadduser'),
]
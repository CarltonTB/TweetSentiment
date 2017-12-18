'''
Created on Nov 23, 2017

@author: carltonbrady
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
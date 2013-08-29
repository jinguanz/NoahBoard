__author__ = 'jinguangzhou'
from django.conf.urls import patterns, url

from nb_webapp import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       #url(r'^register/$', views.RegisterView.as_view(), name='Sign up'),
                       url(r'^register/$', views.register, name='Register'),
)

from django.conf.urls import url
from django.contrib import admin
from simplemooc.core import views

urlpatterns =[
	url(r'^$', views.home, name='home')
]
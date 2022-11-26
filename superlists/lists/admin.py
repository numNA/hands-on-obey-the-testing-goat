#from django.contrib import admin

# Register your models here.

from django.conf.urls import url
from lists import views

url_patterns = [
        url(r'^$', views.home_page, name='home'),
]

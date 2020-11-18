from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [

    path('',views.Home, name='home'), 
    re_path(r'^form-detail/(?P<random_url>[-\w]+)/$', views.form_detail, name="form_detail")
]
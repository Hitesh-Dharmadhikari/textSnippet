from django.urls import path

from . import views

urlpatterns = [

    path('',views.Home, name='home'), 
    path(r'^form-detail/(?P<random_url>[-\w]+)/$', views.form_detail, name="form_detail")
]
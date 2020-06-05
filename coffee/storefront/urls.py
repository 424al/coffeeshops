from django.urls import path
from django.conf.urls import url
from . import views
from .views import Test
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^account/login/$', LoginView.as_view(template_name='account/login.html'),
        name='login'),
    path('add/',Test.as_view(),name='test_form'),
    path('',views.homepage, name='mysite'),

]
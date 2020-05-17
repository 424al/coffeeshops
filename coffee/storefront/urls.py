from django.urls import path
from . import views
from .views import Test

urlpatterns = [
    path('add/',Test.as_view(),name='test_form'),
    path('',views.homepage, name='mysite'),

]
from django.urls import path
from django.conf.urls import url
from . import views
from .views import Test, LocationsDirectory,SuperAdminLocationDirectory
from django.contrib.auth.views import LoginView

urlpatterns = [
    #ALLAUTH LOGIN
    url(r'^account/login/$', LoginView.as_view(),name='login'),
    #ADD LOCATION FORM
    path('add/',Test.as_view(),name='test_form'),
    #HOMEPAGE
    path('',views.homepage, name='mysite'),
    #DIRECTORY FOR BUSINESS LOCATIONS THIS IS AN AJAX CALL
    path('storefront_locations', LocationsDirectory.as_view(), name='location_table'),
    #URL WHERE DIRECTORY TABLE LIVES, USE 'management/' FOR ALL SUPERADMIN FUNCTIONS
    path('management/directory/', SuperAdminLocationDirectory.as_view(), name='location_directory')

]
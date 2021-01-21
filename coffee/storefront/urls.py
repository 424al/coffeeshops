from django.urls import path
from django.conf.urls import url
from . import views
from .views import AddLocation, LocationDetailView
from django.contrib.auth.views import LoginView

urlpatterns = [
    #ALLAUTH LOGIN
    # url(r'^account/login/$', LoginView.as_view(),name='login'),
    # ADD LOCATION FORM
    path('add/',AddLocation.as_view(),name='add_location'),

    # HOMEPAGE
    path('',views.homepage, name='homepage'),

    # DetailView of location
    path('<slug>/', LocationDetailView.as_view(), name='location_detailview'),



]
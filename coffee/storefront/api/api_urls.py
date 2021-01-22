from django.urls import path
from .. import views

urlpatterns = [
    path('shops/', views.ShopListCreate.as_view()),

]

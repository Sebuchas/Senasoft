from django.urls import path

from . import views

urlpatterns = [
    path('/', views.special_case_2003),
   
]
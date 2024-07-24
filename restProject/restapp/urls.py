
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.student_detail,name='home'),
    path('stuData/',views.student_detail_all,name='studentData')
]

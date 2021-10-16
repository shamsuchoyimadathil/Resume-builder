from django.urls import path 
from . import views

urlpatterns = [
    path("",views.Main_view.as_view(),name="main"),
    path("resume-builder",views.Resume_builder.as_view(),name="resume-builder"),

]

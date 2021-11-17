from django.urls import path 
from . import views


urlpatterns = [
    path("",views.Main_view.as_view(),name="main"),
    path("resume-builder",views.Resume_builder.as_view(),name="resume-builder"),
    path("detail-resume/<int:id>",views.Resume_detail_view.as_view(),name="detailresume"),
    path("download-pdf",views.GeneratePdf.as_view(),name="to-pdf"),
]
